

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Heyyyy"

@app.get("/index_1")
def index_1():
    return "What's going on there"

@app.get("/about")
def json():
    return {"Data":"About Page"}


@app.get("/index_1/json")
def json():
    return {"data":{"name": "Pradheep"}}

@app.get("/index_1/json/json_1")
def json():
    return {"data":{"Json data's are there"}}