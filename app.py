from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API com FastAPI e MongoDB",
    description="API CRUD simples utilizando o mongodb"
)
app.include_router(user)
