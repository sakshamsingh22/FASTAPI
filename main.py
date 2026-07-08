#  DAY 1
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello, World!"} 
 

#about route
@app.get("/about")
def about():
    return {"message": "This is the about page!"} 
@app.get("/user")
def user():
    return {
        "users": ["Alice", "Bob", "Charlie"]
           }