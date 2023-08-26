from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .model import *

qa = Qamodel()
print('model init...')
qa.init()
print("done.")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
async def ping():
    return "ok"


@app.get("/question/{question}")
async def get_answer(question):
    return {"message": qa.get_first_answer(question)}
