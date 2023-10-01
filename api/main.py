from fastapi import FastAPI # FastAPIをインポートする
from api.routers import task, done

app = FastAPI() # FastAPIのインスタンスを生成
app.include_router(task.router)
app.include_router(done.router)