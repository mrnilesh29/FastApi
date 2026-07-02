from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def hello(): 
    return "hello i am Nilesh Shah"

@app.get("/users/{user_id}")
def user(user_id : int): 
    return f"hello my id is = {user_id}"