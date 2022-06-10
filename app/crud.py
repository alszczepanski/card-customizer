from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models
import schemas

from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from database import get_connection

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def hash(password):
    return pwd_context.hash(password)


def get_user(db: Session, username: str):
    if db.query(models.User).filter(models.User.username == username).first():
        s = db.query(models.User).filter(models.User.username == username).first()
        return s
    else:
        'sds'


def save_user(db: Session, user_in: schemas.UserIn):
    hashed_password = hash(user_in.password)
    user_in_db = schemas.UserInDB(**user_in.dict(), hashed_password=hashed_password)
    db_user = models.User()
    db_user.hashed_password = user_in_db.hashed_password
    db_user.username = user_in_db.username
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user_in_db


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(db: Session = Depends(get_connection), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
        print(token_data)
    except JWTError:
        raise credentials_exception
    user = get_user(db, username=(token_data.username))
    print(user)
    if user is None:
        raise credentials_exception
    return { "id": user.id, "username": user.username }

