from sqlalchemy.orm import Session

import api.models.task as task_model
import api.schemas.task as task_schema

# ルーター(controllerやViewに当たる部分)の肥大化を避けるためdbに対するCRID操作はcrudsにかく

# データベースに新しいタスクを作成し、そのタスクを返す関数
def create_task( db: Session, task_create: task_schema.TaskCreate) -> task_model.Task:
    # インスタンスの作成
    task = task_model.Task(**task_create.dict())
    db.add(task)
    db.commit()
    db.refresh(task)

    return task