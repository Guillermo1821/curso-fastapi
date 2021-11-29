#Python
from typing import Optional
from fastapi.param_functions import Query

#Pydantic
from pydantic import BaseModel

#FastaPi
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query

app = FastAPI()

#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/")
def home():
    return {"Hello": "World"}


#request and response body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person


#Validaciones query parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: str = Query(...)
    
):
    return {name: age}
