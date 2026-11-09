from fastapi import FastAPI
from routers import POST, GET, DELETE, PUT


app = FastAPI()
app.include_router(POST.router)
app.include_router(GET.router)
app.include_router(DELETE.router)
app.include_router(PUT.router)
