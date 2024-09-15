from sqlmodel import SQLModel, Field
from typing import Optional

class SampleData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    city: str
