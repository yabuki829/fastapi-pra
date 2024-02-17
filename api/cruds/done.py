from typing import Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model


# Doneを取得する
async def get_done(db: AsyncSession, task_id: int) -> Optional[task_model.Done]:
    result = await db.execute(
        select(task_model.Done).filter(task_model.Done.id == task_id)
    )
    done = result.scalars().first()
    return done


# タスクをDoneにする
async def create_done(db: AsyncSession, task_id: int) -> task_model.Done:
    done = task_model.Done(id=task_id)
    db.add(done)
    await db.commit()  # 非同期でコミット
    await db.refresh(done)  # 非同期でリフレッシュ
    return done


async def delete_done(db: AsyncSession, original: task_model.Done) -> None:
    await db.delete(original)
    await db.commit()