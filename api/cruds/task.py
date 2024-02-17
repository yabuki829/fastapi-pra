from sqlalchemy.orm import Session

import api.models.task as task_model
import api.schemas.task as task_schema

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

# ルーター(controllerやViewに当たる部分)の肥大化を避けるためdbに対するCRID操作はcrudsにかく
# CRUD　とは（Create/Read/Update/Delete）のこと
# データベースに新しいタスクを作成し、そのタスクを返す関数
async def create_task( db: AsyncSession, task_create: task_schema.TaskCreate) -> task_model.Task:
    # インスタンスの作成
    task = task_model.Task(**task_create.model_dump())
    db.add(task)
    await db.commit()
    await db.refresh(task)

    return task



# doneタスクを全て取得する
async def get_task_with_done(db:AsyncSession) -> list[tuple[int,str,bool]]:
    result:Result = await (
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

async def get_task(db: AsyncSession, task_id: int) -> Optional[task_model.Task]:
    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task: Optional[Tuple[task_model.Task]] = result.first()
    return task[0] if task is not None else None

# 元タスクと新しいタスクを受け取り、titleを変更したあと、変更後のタスクを返す
async def update_task(db:AsyncSession,task_create: task_schema.TaskCreate,original: task_model.Task) -> task_model.Task:
    original.title = task_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)

    return original


    

# delete
async def delete_task(db:AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)
    await db.commit()

