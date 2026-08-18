from pydantic import BaseModel, Field
from typing import Optional

# class student will inherit from BaseModel
class Student(BaseModel):
    name: str
    age: Optional[int] = None # if not age then it will be None
    grade: str
    gender: str = "Not specified" # default value
    cgpa: float = Field(gt=0, lt=10, default=5.0, description="Cumulative Grade Point Average") # cgpa should be greater than 0 and less than 10, default value is 5.0 and description is provided for the field
    

# new student dictionary
# new_student = {'name': 'John Doe', 'age': 20, 'grade': 'A'} # not working because of the type error

# new_student = {'name': 'John Doe', 'age': 20, 'grade': 'A'}

# new_student = {'name': 'John Doe', 'grade': 'A'}

# pydantic will automatically convert the age to int if it is provided as a string - called python type coercion
# new_student = {'name': 'John Doe', 'age': '20', 'grade': 'A'}

new_student = {'name': 'John Doe', 'age': 20, 'grade': 'A', 'cgpa': 8.5}

# create a new student object using the dictionary
student = Student(**new_student)

print(student)
print(type(student))


student_dict = dict(student) # convert the student object to a dictionary

print(student_dict)