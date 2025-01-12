from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def index():
    return {"Data":"madhav"}

@app.get("/about")
def index():
    return "Madhav"


# Fetch data according to some id
@app.get("/blog/{id}")
def show(id:int):
    return {'data': id}

@app.get("/blog/{id}/comments")
def comments(id:int):
    return {"data":{"comments":{'1','2','3','4'}}}