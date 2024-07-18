from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal
import models

app = FastAPI()


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class Person(OurBaseModel):
    id : int
    firstname : str
    lastname : str
    isMale : bool

db = SessionLocal()

# @app.get('/', response_model=list[Person],status_code=200)
# def getAll_Person():
#     getAllPersons = db.query(models.Person).all()
#     return getAllPersons

@app.get('/addperson', response_model=Person,status_code=201)
def add_Person(person:Person):
    newPerson = models.Person(
        id = person.id,
        firstname = person.firstname,
        lastname = person.lastname,
        isMale = person.isMale

    )
    db.add(newPerson)
    db.commit()
    return newPerson






