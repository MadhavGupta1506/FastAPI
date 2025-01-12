from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def index():
    return {"Data":"madhav"}
@app.get("/about")
def index():
    return "Madhav"