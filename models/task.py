from pydantic import BaseModel

class Tasks(BaseModel):
    id: str | None = None
    title = str
    description = str
    