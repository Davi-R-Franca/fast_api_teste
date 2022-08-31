from fastapi import APIRouter, status
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson import ObjectId

user = APIRouter()


@user.get('/users', response_model=list[User])
async def get_all_users():
    return usersEntity(conn.local.user.find())


@user.get('/user/{id}', response_model=User)
async def get_user_by_id(id: str):
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.post('/user/create', response_model=User)
async def create_user(use: User):
    new_user = dict(use)
    idt = conn.local.user.insert_one(new_user).inserted_id
    usuario = conn.local.user.find_one({"_id": idt})
    return userEntity(usuario)


@user.put('/user/update/{id}', response_model=User)
async def update_user(id: str, use: User):
    conn.local.user.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(use)}
    )
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.delete('/user/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    userEntity(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
    return "Usuario deletado"
