from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def hello(): 
    return "hello i am Nilesh Shah"

@app.get("/users/{user_id}")
def user(user_id : str): 
    return f"hello my id is = {user_id}"

@app.get("/para")
def parameter(name) : 
    return {"Name" : name}


@app.get("/items")
def items(product : str = None , price :int = 0 ): 
    return {"product" : product, 
            "price" : price ,
            }