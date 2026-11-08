from fastapi import APIRouter, HTTPException, status
from models.task import Tasks

router = APIRouter(
    prefix="/post_taks",
    tags= ["post_taks"],
    responses={404: {"description": "No found"}}
)

task_list = []

@router.post("/post/", status_code=201)
async def add_taks(task: Tasks):
    task_list.append(task)
    return {
        "mensaje" : "Task Successfully added", 
        "task" : task
    }
