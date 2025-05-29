from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    age: int = 20
    name: Optional[str] = None

new_student = {}

student = Student(**new_student)

print(student)