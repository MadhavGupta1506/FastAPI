from fastapi import FastAPI
from typing import Optional
app= FastAPI()

@app.get("/")
def index():
    return {"Data":"madhav"}


# Getting all the Blogs
# @app.get()
# def index():
#     return {"data":"All Blogs"}


# Getting limited blogs
@app.get("/blog")
# Using query parameters
def index(limit,published:bool,sort:Optional[str]=None):
    if(published):
        return {"data":f"{limit} Blogs from data base"}
    return {"data":"all Blogs from data base"}

@app.get("/blog/unpublished")
def unpublished():
    return {'data':"unpublished"}

# Fetch data according to some id
@app.get("/blog/{id}")
def show(id:int):
    return {'data': id}

@app.get("/blog/{id}/comments")
def comments(id:int,limit=10):
    # return limit
    return {id:{"comments":("1","2","3")}}
