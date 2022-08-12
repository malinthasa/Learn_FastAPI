from typing import List
from uuid import uuid4, UUID

from fastapi import FastAPI, HTTPException
import asyncio

from models.User import User, Gender, Roles

app = FastAPI()
db: List[User] = [User(id=UUID("bf7c36ec-68ea-4678-a79d-8d2709074524"),
                       first_name='Malintha',
                       last_name="Adikari",
                       gender=Gender.male,
                       roles=[Roles.student]),
                  User(id=UUID("0388e179-4cfd-4a81-a388-6becdfbf266c"),
                       first_name='Sammani',
                       last_name="Gunasinghe",
                       gender=Gender.female,
                       roles=[Roles.user])
                  ]


@app.get("/")
def root():
    return {'response': 'Welcome to learn FastAPI'}


@app.get("/home")
def home():
    return {'response': 'hello world!'}


@app.get("/asynchome")
async def demoAsync():
    await asyncio.sleep(10)
    return {'response': 'Got response after some time :)'}


@app.get("/users")
async def fetch_users():
    return {'response': db}


@app.post("/users")
async def add_user(user: User):
    db.append(user)
    return {'response': {'id': user.id}}


@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user_id == user.id:
            db.remove(user)
            return {'response': 'Users is deleted successfully'}
    raise HTTPException(status_code=404, detail=f'Users does not exist')


@app.put("/users/{user_id}")
async def delete_user(user_update: User, user_id: UUID):
    for user in db:
        if user_id == user.id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.gender is not None:
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {'response': 'Users is updated successfully'}
    raise HTTPException(
        status_code=404,
        detail=f'Users does not exist')
