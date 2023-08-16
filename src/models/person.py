from pydantic import BaseModel

class Person(BaseModel):
  age: int
  job: str
  marital: str
  education: str
  balance: float
  housing: str
  duration: int
  campaign: int