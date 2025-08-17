from fastapi import FastAPI

from .routers import messages, auth, users

from . import database
from . import models 
from fastapi.middleware.cors import CORSMiddleware


from sqlmodel import SQLModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SQLModel.metadata.create_all(database.engine)

app.include_router(auth.router)
app.include_router(messages.router)
app.include_router(users.router)


@app.get("/")
def main():
	return {"msg" : "hello world"}
