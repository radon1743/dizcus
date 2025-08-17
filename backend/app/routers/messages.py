from fastapi import APIRouter, Depends, status,HTTPException
from .. models import *
from .. database import *
from app.oauth2 import get_current_user

router = APIRouter(
	prefix="/message",
	tags=['Message']
	)

@router.post("/send",status_code=status.HTTP_201_CREATED)
def send_message(msg: MessageCreate, user_id:int = Depends(get_current_user)):
	# msg.user_id = user_id
	new_msg = add_message(Message(**msg.dict()))
	if not new_msg:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
	else:
		return new_msg


@router.get("/get/{chat_id}" )
def get_messages(chat_id:int, user_id:int = Depends(get_current_user)):
	get_message = get_by_chatid(chat_id, user_id)
	if not get_message:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
	else:
		return get_message
