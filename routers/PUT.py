from fastapi import APIRouter, HTTPException
from models.task import Tasks
from services.task_service import task_list

router = APIRouter(
    prefix="/put_taks",
    tags=["put_taks"]
)
@router.put("/{id}")
async def put_taks(id: int, update_task: Tasks):
    for i, task in enumerate(task_list):
        if task.id == id:
            update_task.id = id
            task_list[i] = update_task
            return {"message": "update tasks",
                    "task": update_task
                }
    raise HTTPException(
            status_code=404,
            detail="no found task"
        )
