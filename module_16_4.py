from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users = []


@app.get("/users")
async def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=2, description="Enter username", example="Ян")],
                      age: Annotated[int, Path(ge=1, le=120, description="Enter age", example="20")],
                      user: User) -> str:
    user.id = len(users)
    user.username = username
    user.age = age
    users.append(user)
    return f"User {user.id} {user.username} {user.age} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=0, le=100, description="Enter user id",
                                                   example="1")],
                      username: Annotated[str, Path(min_length=2, description="Enter username", example="Ян")],
                      age: Annotated[int, Path(ge=1, le=120, description="Enter age", example="20")]) -> str:
    try:
        edit_user = users[user_id]
        edit_user.id = user_id
        edit_user.username = username
        edit_user.age = age
        return f"The user {user_id} is updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=0, le=100, description="Enter user id",
                                                   example="1")]) -> str:
    try:
        users.pop(user_id)
        return f"The user {user_id} is deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
