from fastapi import APIRouter, HTTPException, status
from services.task_service import list_tasks


router = APIRouter(
    prefix="/get_taks",
    tags= ["get_taks"],
    responses={404: {"description": "No found"}}
)
@router.get("/get")
async def get_tasks():
    return list_tasks()