
from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date
from typing import Optional


class EmployeeCreate(BaseModel):
    Employee_Name: str
    Department: str
    Email: EmailStr


class EmployeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    Employee_ID: int
    Employee_Name: str
    Department: str
    Email: EmailStr


class TaskCreate(BaseModel):
    Employee_ID: int
    Task_Name: str
    Task_Status: str = "Pending"
    Due_Date: date


class TaskStatusUpdate(BaseModel):
    Task_Status: str


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    Task_ID: int
    Employee_ID: int
    Task_Name: str
    Task_Status: Optional[str] = "Pending"
    Due_Date: date
