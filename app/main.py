from datetime import timedelta
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import get_connection, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register", response_model=schemas.UserOut)
def create_user(user_in: schemas.UserIn, db: Session = Depends(get_connection)):
    user_saved = crud.get_user(db, username=user_in.username)
    if user_saved:
        raise HTTPException(status_code=400, detail="Username already registered.")
    user_saved = crud.save_user(db=db, user_in=user_in)


@app.post("/login", response_model=schemas.Token)
async def login_for_access_token(user_in: schemas.UserIn, db: Session = Depends(get_connection)):
    user_dict = crud.get_user(db, user_in.username).__dict__

    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = schemas.UserInDB(**user_dict)

    if not crud.verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    access_token_expires = timedelta(minutes=crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/")
async def read_users_me(current_user: schemas.User = Depends(crud.get_current_user)):
    return current_user
