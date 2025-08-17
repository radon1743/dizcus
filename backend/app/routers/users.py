from fastapi import APIRouter, status, HTTPException
from .. models import *
from .. database import *
from .. utils import *

router = APIRouter(
	prefix="/user",
	tags=['User']
	)

@router.get("/hello")
def hello_user():
	return {"hello":"user"}


@router.post("/create", response_model=UserRead)
def add_user(user:UserCreate):
	user.password = hash(user.password)
	usr = create_user(User(**user.dict()))

	if not usr:
		raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)
	else:
		return usr

@router.get("/get/{user_id}", response_model=UserRead)
def get_user(user_id:int):
	user = fetch_user(user_id)
	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
	else:
		return user