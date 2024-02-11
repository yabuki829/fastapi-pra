from fastapi import APIRouter
import api.schemas.task as task_schema
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
async def create_task(task_body:task_schema.TaskCreate):
    print("呼ばれてる？？？？")
    print(task_body)
    return task_schema.TaskCreateResponse(id=1,**task_body.dict())


# タスクの編集
@router.put("/tasks/{task_id}")
async def edit_tasks():
    pass

# タスクの削除
@router.delete("/tasks/{task_id}")
async def delete_task():
    pass


