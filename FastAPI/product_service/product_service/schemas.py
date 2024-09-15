from pydantic import BaseModel

class SampleDataCreate(BaseModel):
    name: str
    age: int
    city: str
