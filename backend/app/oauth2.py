from datetime import timedelta, datetime
from jose import JWTError, jwt
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer

# from app.database import fetch_user, fetch_user_by_username
from app.models import TokenData

oauth_scheme = OAuth2PasswordBearer("login")

SECRET_KEY = "my secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60



def create_token(user_details:dict):

	token_data = user_details.copy()
	expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	
	token_data.update({"exp" : expire})

	encoded_token = jwt.encode(token_data, key=SECRET_KEY, algorithm=ALGORITHM)

	return encoded_token


def verify_token(token:str, credentials_exception):
	try :
		decoded_token = jwt.decode(token, algorithms=[ALGORITHM], key=SECRET_KEY)
		id = decoded_token.get("user_id")

		if id is None:
			raise credentials_exception

		data = TokenData(user_id=id)
		return data
	except JWTError:
		raise credentials_exception

def get_current_user(token:str = Depends(oauth_scheme)):
	credentials_exception = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED, 
		detail="Could not validate user details", 
		headers={"WWW-Authenticate": "Bearer"}
		)

	return verify_token(token, credentials_exception)

