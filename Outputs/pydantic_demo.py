from pydantic import BaseModel, EmailStr, Field
from typing import Any, Optional

class Student(BaseModel):
    age: int = 18
    name: Optional[str] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=5)

new_student = {"age": 21, "email": "ali@test.com", "cgpa": 4.99}

student = Student(**new_student)

print(student)