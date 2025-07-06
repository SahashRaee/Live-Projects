#@ Calculator Backend with FastAPI 

from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

#@ Input Schema 

class Operation(BaseModel):
    num1: float 
    num2: float 

@app.get("/")
def home():
    return {"message": "Welcome to the Web Calculator"}

@app.post("/Addition")
def add(data : Operation):
    return {"result": data.num1 + data.num2}

@app.post("/Subtraction")
def subtract(data: Operation):
    return {"result": data.num1 - data.num2}

@app.post("/Multiplication")
def multiply(data: Operation):
    return {"reslut": data.num1 *data.num2}

@app.post("/Division")
def divide(data: Operation):
    if data.num1 == 0: 
        return {"error": "Division by zero is not allowed"}
    else:
        return {"result": data.num1/data.num2}
    

