from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int

new_student = {"name": "Ali", "age": 15}

student = Student(**new_student)

print(student)