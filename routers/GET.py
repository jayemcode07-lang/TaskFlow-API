from fastapi import APIRouter, HTTPException, status
from routers.POST import task_list

router = APIRouter(
    prefix="/get_taks",
    tags= ["get_taks"],
    responses={404: {"description": "No found"}}
)
@router.get("/get")
async def get_tasks():
    return task_list