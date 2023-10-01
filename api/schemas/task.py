from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int
    title: str | None = Field(None, example="クリーニングをとりに行く")
    done: bool = Field(False, description="完了フラグ")