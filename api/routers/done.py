from fastapi import APIRouter

# APIRouterをインスタンス化する
router = APIRouter()

@router.put("/tasks/{task_id}/done")
async def mark_task_as_done():
    pass

@router.delete("/tasks/{task_id}/done")
async def unmark_task_as_done():
    pass