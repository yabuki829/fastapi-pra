from fastapi import APIRouter
router = APIRouter()



# taskをdone
@router.put("/tasks/{task_id}/done")
async def done_task():
    pass

# doneを取り消し
@router.delete("/tasks/{task_id}/done")
async def cancel_done_task():
    pass