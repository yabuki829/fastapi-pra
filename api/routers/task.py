from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
import api.schemas.task as task_schema
import api.cruds.task as task_crud
from api.db import get_db
router = APIRouter()


# タスクの一覧表示
@router.get("/tasks",response_model=list[task_schema.Task])
async def list_tasks():

    return [
        task_schema.Task(id=1,title="seoの勉強をする"),
        task_schema.Task(id=2,title="fastapiの勉強をする"),
        task_schema.Task(id=3,title="情報セキュリティーマネジメントの勉強をする"),
        task_schema.Task(id=4,title="基本情報技術者試験の勉強をする"),
        task_schema.Task(id=5,title="fastapiの勉強をする"),
    ]

# タスクの作成
@router.post("/tasks",response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db: Session = Depends(get_db)):
    return task_crud.create_task(db, task_body)

# タスクの編集
@router.put("/tasks/{task_id}",response_model=task_schema.TaskCreateResponse)
async def edit_tasks(task_id:int,task_body:task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=task_id,**task_body.dict())

# タスクの削除
@router.delete("/tasks/{task_id}",response_model=None)
async def delete_task(task_id:int):
    print("タスクの削除が完了しました。")
    return



