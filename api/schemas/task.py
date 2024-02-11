from pydantic import BaseModel,Field

class TaskBase(BaseModel):
    title: str | None = Field(None,example="情報セキュリティマネジメント試験の勉強をする")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id:int
    class Config:
        orm_mode = True


class Task(TaskBase):
    id:int
    done:bool = Field(False,desctiption="完了フラグ")
    class Config:
        orm_mode = True

