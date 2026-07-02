from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()
class Address(BaseModel): 
    city:str 
    pincode:int 
    state : str 
    country : str

class user(BaseModel) :
    name : str 
    age : int 
    email : str 
    address : Address
    phone_no:int 
    

    
@app.post("/create_users")
def create_users(child : user) : 
    return {
        "message" :" user created sucessfully", 
        "data" : child 
    }



