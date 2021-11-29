#Python
from typing import Optional
from fastapi.param_functions import Query
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field, EmailStr

#FastaPi
from fastapi import FastAPI
from fastapi import Body, Query, Path
from pydantic.networks import EmailStr


app = FastAPI()

#Models
class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"



class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=30
        )
    state: str = Field(
        min_length=1,
        max_length=30
    )
    country: str = Field(
        ...,
        min_length=1,
        max_length=30
    )


class Person(BaseModel):
    first_name: str = Field(
        ..., 
        min_length=1, 
        max_length=50)
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        le=115
        )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)
    email: EmailStr = Field(
        ...,
        title="Email user",
        description="This is the email user")
    
    class Config:
        shcema_extra = {
            "example":{
                "first_name": "guillermo",
                "last_name": "Chacon",
                "age": 24,
                "hair_color": "black",
                "is_married": False
            }
        }


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
        description="This is the person name, its between 1 and 50 characters",
        example="Rocio"
        ),
    age: str = Query(
        ...,
        title="Person age",
        description="This is the person age, its required",
        example=22
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
        description="This is the person ID, Its required",
        example=123
        )
):
    return {person_id: "It exists!"}


#validaciones: request body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0,
        example=123
    ),
    person: Person = Body(...),
    Location: Location = Body(...)
):
    results = person.dict()
    results.update(Location.dict())

    return results
