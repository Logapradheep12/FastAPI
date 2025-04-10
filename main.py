

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return "Heyyyy"



@app.get("/index_1")
def index_1():
    return "What's going on there"



@app.get("/index_1/json")
def json():
    return {"data":{"name": "Pradheep"}}



@app.get("/index_1/json/json_1")
def json():
    return {"data":{"Json data's are there"}}



@app.get("/blog/unpublished")
def blog():
    return {"Data" : "All Unpublished Blogs"}



# fetch /blog with id = id

@app.get("/blog/{id}")
def json(id: int):
    return {"Data" : id}



# fetch comments /blog with id = id

@app.get("/blog/{id}/comment")
def json(id):
    return {"Data" : {"1","2"}}




# only get 10 API In the blog

@app.get("/blog")
def json(limit):
    return {"Data" : f'{limit} of Blog Values'}



# request blog

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]
    
    
@app.post('/blog1')
def post_blog(blog : Blog):
    return {'data' : f'Blog is created and its title {blog.title}. then its {blog.body}'}
    
    
# Debugging


