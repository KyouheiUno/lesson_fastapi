# APIRouterをインポートする
from fastapi import APIRouter
import api.schemas.task as task_schema 
# APIRouterをインスタンス化する
router = APIRouter()

# endpointを定義
@router.get("/tasks", response_model=list[task_schema.Task])
async def list_task():
    return [task_schema.Task(id=1, title="一つ目のタスク")]

@router.post("/tasks")
async def create_task():
    pass

@router.put("/tasks/{task_id}")
async def update_task():
    pass

@router.delete("/tasks/{task_id}")
async def delete_task():
    pass