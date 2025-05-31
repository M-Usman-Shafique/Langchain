from pydantic import BaseModel, EmailStr
from typing import Any, Optional

class Student(BaseModel):
    age: int = 18
    name: Optional[str] = None
    email: EmailStr

new_student = {"age": 21, "email": "ali@test.com"}

student = Student(**new_student)

print(student)