#Python
from typing import Optional
from fastapi.param_functions import Query

#Pydantic
from pydantic import BaseModel

#FastaPi
from fastapi import FastAPI
from fastapi import Body, Query, Path


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
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person name",
        description="This is the person name, its between 1 and 50 characters"
        ),
    age: str = Query(
        ...,
        title="Person age",
        description="This is the person age, its required"
        )
    
):
    return {name: age}


#validacion: path parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="This is the person ID",
        description="This is the person ID, Its required"
        )
):
    return {person_id: "It exists!"}
