from fastapi import FastAPI, HTTPException

app = FastAPI()
@app.get("/")

def hello():
    return {"message": "Hello, World!"}



@app.get("/about")
def about():
    return {"message": "This is the about page."}





