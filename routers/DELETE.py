from fastapi import APIRouter, HTTPException
from routers.POST import task_list

router = APIRouter(
    prefix="/delete_taks",
    tags=["delete_taks"]
)

@router.delete("/{id}")
async def delete_task(id: int):

    for index, task in enumerate(task_list):
        if task.id == id:
            del task_list[index]
            return {"message": "Tarea eliminada"}

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )