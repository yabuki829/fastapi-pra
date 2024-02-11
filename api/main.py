
from fastapi import FastAPI
from api.routers import task,done


app = FastAPI()

app.include_router(task.router)
app.include_router(done.router)

# hallo というエンドポイントの作成
@app.get("/hello")
async def hello():
    mes = "hello world !!"
    return {"message":mes}


# todoアプリに必要なもの
