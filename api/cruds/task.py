from sqlalchemy.orm import Session

import api.models.task as task_model
import api.schemas.task as task_schema

# ルーター(controllerやViewに当たる部分)の肥大化を避けるためdbに対するCRID操作はcrudsにかく
# CRUD　とは（Create/Read/Update/Delete）のこと
# データベースに新しいタスクを作成し、そのタスクを返す関数
def create_task( db: Session, task_create: task_schema.TaskCreate) -> task_model.Task:
    # インスタンスの作成
    task = task_model.Task(**task_create.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)

    return task

from sqlalchemy import select
from sqlalchemy.engine import Result


# doneタスクを全て取得する
def get_task_with_done(db:Session) -> list[tuple[int,str,bool]]:
    result: Result = (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
            ).outerjoin(task_model.Done)
        )
    )
    return result.all()


from typing import List, Tuple, Optional
# update

async def get_task(db: Session, task_id: int) -> Optional[task_model.Task]:
    result: Result = db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task: Optional[Tuple[task_model.Task]] = result.first()
    return task[0] if task is not None else None

# 元タスクと新しいタスクを受け取り、titleを変更したあと、変更後のタスクを返す
def update_task(db:Session,task_create: task_schema.TaskCreate,original: task_model.Task) -> task_model.Task:
    print("----------------------------------------")
    print(task_create,original)
    print("----------------------------------------")
    original.title = task_create.title
    db.add(original)
    db.commit()
    db.refresh(original)

    return original


    

# delete
def delete_task(db:Session, original: task_model.Task) -> None:
    db.delete(original)
    db.commit()


# done
