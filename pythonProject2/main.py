from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Define the Employee schema using Pydantic BaseModel
class Employee(BaseModel):
    name: str
    age: int
    department: str


employee_data = {}


@app.post("/employees/create")
def create_employee(employee_id: int, employee: Employee):
    if employee_id in employee_data:
        raise HTTPException(status_code=400, detail="Employee with this ID already exists")

    employee_data[employee_id] = {
        "name": employee.name,
        "age": employee.age,
        "department": employee.department
    }
    return {"message": "Employee created successfully"}


@app.put("/employees/update/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    if employee_id not in employee_data:
        raise HTTPException(status_code=404, detail="Employee not found")

    employee_data[employee_id] = {
        "name": employee.name,
        "age": employee.age,
        "department": employee.department
    }
    return {"message": "Employee updated successfully"}


@app.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: int):
    if employee_id not in employee_data:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"employee_id": employee_id, **employee_data[employee_id]}


@app.get("/employees")
def get_all_employees():
    return {"employees": employee_data}
