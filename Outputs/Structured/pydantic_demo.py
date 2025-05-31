from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    age: int = 18
    name: Optional[str] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=5, default=3, description="A decimal value presenting the CGPA of a student")

new_student = {"age": 21, "email": "ali@test.com", "cgpa": 4.99}

student = Student(**new_student)

# Pydantic model:
print(student.email)

# Convert to dict:
dict_student = dict(student)
print(dict_student["age"])