from pydantic import BaseModel
from typing import Any

class Student(BaseModel):
    name: str
    age: int = 20

new_student: dict[str, Any] = {"name": "Ali"}

student = Student(**new_student)

print(student)