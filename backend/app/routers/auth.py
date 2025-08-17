from os import access
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.database import fetch_user_by_username
from app.models import UserCreate, UserRead, User, UserLogin
from .. utils import *
from .. oauth2 import * 


router = APIRouter(tags=['Auth'])

@router.post("/login")
def login(user_details: OAuth2PasswordRequestForm = Depends()):
	user = fetch_user_by_username(user_details.username)

	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Creadentials")

	if not verify(user_details.password, user.password):
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Creadentials")

	data = {"user_id": user.user_id}
	access_token = create_token(data)

	return {"access_token":access_token, "token_type":"bearer"}

