from fastapi import FastAPI

from main import testMessage

app = FastAPI()

@app.get("/")
def root():
    return testMessage