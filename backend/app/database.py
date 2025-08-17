from sqlmodel import SQLModel, create_engine, Session, select
from .models import *

DATABASE_URL = "mysql+pymysql://chat_user:Password_1743@localhost/chat_app"

engine = create_engine(DATABASE_URL)


def add_message(message: Message):
	with Session(engine) as session:
		session.add(message)
		session.commit()
		session.refresh(message)
		return MessageRead(**message.dict())

def get_by_chatid(chat_id:int, user_id:int):
	with Session(engine) as session:
		statment = select(Message).where(Message.chat_id == chat_id)
		msgs = session.exec(statment).all()
		return [MessageRead(**i.dict()) for i in msgs]

def create_user(user: User):
	with Session(engine) as session:
		session.add(user)
		session.commit()
		session.refresh(user)
		return UserRead(**user.dict())

def fetch_user(user_id:int):
	with Session(engine) as session:
		statement = select(User).where(User.user_id == user_id)
		user = session.exec(statement).first()
		return user

def fetch_user_by_username(username:str):
	with Session(engine) as session:
		statement = select(User).where(User.username == username)
		user = session.exec(statement).first()
		return user

