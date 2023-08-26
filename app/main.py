from fastapi import FastAPI
from .model import get_answers

app = FastAPI()


@app.get("/ping")
async def ping():
    return "ok"


@app.get("/question/{question}")
async def get_answer(question):
    return get_answers(question)
