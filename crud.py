from sqlalchemy.orm import Session
from sqlalchemy import select

import models
import schemas


# Add Employee
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        Employee_Name=employee.Employee_Name,
        Department=employee.Department,
        Email=employee.Email
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


# View All Employees
def get_employees(db: Session):
    return db.query(models.Employee).all()


# Add Task
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        Employee_ID=task.Employee_ID,
        Task_Name=task.Task_Name,
        Task_Status=task.Task_Status,
        Due_Date=task.Due_Date
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# View All Tasks with Employee Details (JOIN)
def get_tasks(db: Session):
    return (
        db.query(models.Task, models.Employee.Employee_Name)
        .join(
            models.Employee,
            models.Task.Employee_ID == models.Employee.Employee_ID
        )
        .all()
    )


# Search Tasks by Employee ID
def get_tasks_by_employee(db: Session, employee_id: int):
    return db.query(models.Task).filter(
        models.Task.Employee_ID == employee_id
    ).all()


# Update Task Status
def update_task_status(db: Session, task_id: int, status: str):
    task = db.query(models.Task).filter(
        models.Task.Task_ID == task_id
    ).first()

    if task:
        task.Task_Status = status
        db.commit()
        db.refresh(task)

    return task


# Delete Task
def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(
        models.Task.Task_ID == task_id
    ).first()

    if task:
        db.delete(task)
        db.commit()

    return task