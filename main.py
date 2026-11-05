
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

import models
import schemas
import crud

from database import engine, get_db


# Create FastAPI application
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Task Management System",
    description="Manage employees and their tasks",
    version="1.0.0"
)


# Frontend configuration
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Home Page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# Add Employee
@app.post("/employees/", response_model=schemas.EmployeeResponse)
def add_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    try:
        return crud.create_employee(db, employee)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Database error"
        )


# View All Employees
@app.get("/employees/", response_model=list[schemas.EmployeeResponse])
def view_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


# Add Task
@app.post("/tasks/", response_model=schemas.TaskResponse)
def add_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):
    employee = db.query(models.Employee).filter(
        models.Employee.Employee_ID == task.Employee_ID
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return crud.create_task(db, task)


# View All Tasks with Employee Details
@app.get("/tasks/")
def view_tasks(db: Session = Depends(get_db)):
    results = crud.get_tasks(db)

    return [
        {
            "Task_ID": task.Task_ID,
            "Employee_ID": task.Employee_ID,
            "Employee_Name": employee_name,
            "Task_Name": task.Task_Name,
            "Task_Status": task.Task_Status,
            "Due_Date": task.Due_Date
        }
        for task, employee_name in results
    ]


# Search Task by Employee ID
@app.get(
    "/tasks/employee/{employee_id}",
    response_model=list[schemas.TaskResponse]
)
def search_task_by_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_tasks_by_employee(db, employee_id)


# Update Task Status
@app.put(
    "/tasks/{task_id}/status",
    response_model=schemas.TaskResponse
)
def update_task_status(
    task_id: int,
    status: schemas.TaskStatusUpdate,
    db: Session = Depends(get_db)
):
    allowed_status = ["Pending", "In Progress", "Completed"]

    if status.Task_Status not in allowed_status:
        raise HTTPException(
            status_code=400,
            detail="Invalid task status"
        )

    updated_task = crud.update_task_status(
        db,
        task_id,
        status.Task_Status
    )

    if not updated_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated_task


# Delete Task
@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    deleted_task = crud.delete_task(db, task_id)

    if not deleted_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }


# Employees Frontend Page
@app.get("/employees-page")
def employees_page(
    request: Request,
    db: Session = Depends(get_db)
):
    employees = crud.get_employees(db)

    return templates.TemplateResponse(
        request=request,
        name="employees.html",
        context={"employees": employees}
    )


# Tasks Frontend Page
@app.get("/tasks-page")
def tasks_page(
    request: Request,
    db: Session = Depends(get_db)
):
    tasks = view_tasks(db)

    return templates.TemplateResponse(
        request=request,
        name="tasks.html",
        context={"tasks": tasks}
    )


# General Exception Handling
@app.exception_handler(Exception)
async def general_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal Server Error"
        }
    )
