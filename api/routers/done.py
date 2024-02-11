from fastapi import APIRouter
router = APIRouter()



# taskをdone
@router.put("/tasks/{task_id}/done",response_model=None)
async def done_task(task_id:int):
    return

# doneを取り消し
@router.delete("/tasks/{task_id}/done",response_model=None)
async def cancel_done_task(task_id):
    pass