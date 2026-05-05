# Серверное программирование

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # переменная для приложения

# запуск в терминале:
# uvicorn [файл]:[переменная для приложения] --host [адрес] --port [порт]

# endpoint(функция на сервере)
@app.get("/hello_endpoint")
def hello():
    return {"message": "Hello World"}

@app.post("/register/{user_name}")
def register(user_name: str):
    return {
        "user": user_name,
            "is_registered": True
    }


# передача параметров

# создание схемы данных

# данные пользователя
class User(BaseModel):
    name: str
    age: int
    email: str

class UserResponse(BaseModel):
    user_name: str
    age: int
    email: str


@app.post("/register")
def register(user: User) -> UserResponse:
    print(user)

    return UserResponse(
        user_name=user.name,
        age=user.age,
        email=user.email
    )
