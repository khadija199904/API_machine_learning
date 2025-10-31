from typing import Union
from fastapi import FastAPI

app = FastAPI(
    title = 'Welcome to Cardio Risk API'
)
@app.get("/")


@app.get("/patients")

@app.get("/items")
def getItems():
    return ['Item 1', 'Item 2', 'Item 3']

class patient ():
    name:str 
    age : int 
    
@app.post("/")
def postname() :
   return ['khadija']





def add_name(person:patient):
     
    return