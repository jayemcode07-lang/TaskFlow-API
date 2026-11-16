from fastapi import APIRouter, HTTPException, status
from models.task import Tasks
from services.task_service import task_create

router = APIRouter(
    prefix="/post_taks",
    tags= ["post_taks"],
    responses={404: {"description": "No found"}}
)

@router.post("/post/", status_code=201)
async def add_taks(task: Tasks):
    new_task = task_create(task)
    return {
        "mensaje" : "Task Successfully added", 
        "task" : new_task
    }
