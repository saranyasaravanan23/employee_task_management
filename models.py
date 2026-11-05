
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Employee(Base):
    __tablename__ = "task_employee"

    Employee_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Employee_Name = Column(String(100), nullable=False)
    Department = Column(String(100), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)

    tasks = relationship("Task", back_populates="employee")


class Task(Base):
    __tablename__ = "employee_tasks"

    Task_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Employee_ID = Column(Integer, ForeignKey("task_employee.Employee_ID"), nullable=False)
    Task_Name = Column(String(255), nullable=False)
    Task_Status = Column(String(50), default="Pending")
    Due_Date = Column(Date, nullable=False)

    employee = relationship("Employee", back_populates="tasks")
