from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI(
    title ='Поиск на Wikipedia'
)

@app.get('/pages/{text}')
def search(text: str, pages: int):
    return wikipedia.summary(text, sentences = pages),wikipedia.page(text).url

class Wiki (BaseModel):
    text: str
    pages: int

@app.post('/')
def Search(wiki: Wiki):
    return wikipedia.summary(wiki.text, sentences=wiki.pages),wikipedia.page(wiki.text).url
