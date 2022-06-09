from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


# @app.post("/login")
# async def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
#     user_dict = crud.get_user(db, form_data.username).__dict__

#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = schemas.UserInDB(**user_dict)
#     # hashed_password = crud.get_password_hash(form_data.password)

#     print(user.hashed_password)
#     print(type(user.hashed_password))
#     if not crud.verify_password(form_data.password, user.hashed_password):
#         raise HTTPException(status_code=400, detail="Incorrect password")

#     return {"access_token": user.username, "token_type": "bearer"}


@app.post("/register", response_model=schemas.UserOut)
def create_user(user_in: schemas.UserIn, db: Session = Depends(get_db)):
    user_saved = crud.get_user(db, username=user_in.username)
    if user_saved:
        raise HTTPException(status_code=400, detail="Username already registered.")
    user_saved = crud.save_user(db=db, user_in=user_in)

# zadupcone


@app.post("/login", response_model=schemas.Token)
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = crud.get_user(db, form_data.username).__dict__

    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = schemas.UserInDB(**user_dict)
    # hashed_password = crud.get_password_hash(form_data.password)

    print(user.hashed_password)
    print(type(user.hashed_password))
    if not crud.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    access_token_expires = timedelta(minutes=crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    print(access_token)
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(crud.get_current_user)):

    return current_user
