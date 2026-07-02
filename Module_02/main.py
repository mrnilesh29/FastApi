# from fastapi import FastAPI 

# app = FastAPI()

# @app.get("/") 
# def home():
#     return {"message" : "this is home page"}


# @app.get("/users/{user_id}")
# def userid(user_id): 
#     return {
#         "ueser+id" : user_id
#     }
    
    
# @app.get("/username")
# def username(name:str = None , age : int = 0) : 
#     return {"message" : "sucess", 
#             "name" : name , 
#             "age" : age} 
    
    
from fastapi import FastAPI 
from pydantic import BaseModel

class User(BaseModel) : 
    name : str 
    age : int 
    bio : str

app = FastAPI()
@app.post("/create_user")
def create_user(user : User): 
    return {
        "user" : user
    }

