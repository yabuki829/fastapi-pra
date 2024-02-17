from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import api.schemas.task as task_schema
import api.cruds.task as task_crud
from api.db import get_db
router = APIRouter()


# タスクの一覧表示
@router.get("/tasks",response_model=list[task_schema.Task])
async def list_tasks(db: Session = Depends(get_db)):
    task_list = task_crud.get_task_with_done(db)
    return task_list

# async def list_tasks():

#     return [
#         task_schema.Task(id=1,title="seoの勉強をする"),
#         task_schema.Task(id=2,title="fastapiの勉強をする"),
#         task_schema.Task(id=3,title="情報セキュリティーマネジメントの勉強をする"),
#         task_schema.Task(id=4,title="基本情報技術者試験の勉強をする"),
#         task_schema.Task(id=5,title="fastapiの勉強をする"),
#     ]

# タスクの作成
@router.post("/tasks",response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db: Session = Depends(get_db)):
    task = task_crud.create_task(db, task_body)
    return task

# タスクの編集
@router.put("/tasks/{task_id}",response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate, db: Session = Depends(get_db)):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task_crud.update_task(db, task_body, original=task)

# タスクの削除
@router.delete("/tasks/{task_id}",response_model=None)
async def delete_task(task_id:int,db: Session = Depends(get_db)):
    task = await task_crud.get_task(db,task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task_crud.delete_task(db,original=task)
    



