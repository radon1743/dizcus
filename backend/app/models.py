# from pydantic import BaseModel
from typing import Optional
from pydantic import EmailStr
from sqlmodel import Field, SQLModel, Table

class Message(SQLModel, table=True):
	msg_id: Optional[int] = Field(default=None, primary_key=True)
	user_id: int
	chat_id: int
	text: str
	datetime: str

class MessageCreate(SQLModel):
	user_id: int
	chat_id: int
	text: str
	datetime: str	

class MessageRead(SQLModel):
	chat_id: int
	text: str
	datetime: str	

class User(SQLModel, table=True):
	user_id:int = Field(default=None, primary_key=True)
	username: str
	email: EmailStr
	password: str

class UserCreate(SQLModel):
	username: str
	email: EmailStr
	password: str

class UserRead(SQLModel):
	username: str
	email: EmailStr

class UserLogin(SQLModel):
	username: str
	password: str
	

class Token(SQLModel):
	token:str
	exp:str

class TokenData(SQLModel):
	user_id:Optional[int]