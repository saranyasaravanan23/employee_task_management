# Employee Task Management System

## 1. Project Overview

The Employee Task Management System is a web-based application developed using Python, FastAPI, MySQL, HTML, and CSS.

This project helps manage employee details and their assigned tasks. It allows users to register employees, add tasks, view employee and task records, search tasks by Employee ID, update task status, and delete tasks.

## 2. Technologies Used

- Python
- FastAPI
- MySQL
- SQL
- SQLAlchemy
- HTML
- CSS
- Jinja2

## 3. Project Features

### Employee Management
- Add new employees.
- View all employees.
- Store employee name, department, and email.

### Task Management
- Add tasks for employees.
- View all tasks.
- Search tasks using Employee ID.
- Update task status.
- Delete tasks.

### Additional Features
- MySQL database connectivity.
- SQL JOIN operations.
- Dynamic data display.
- Basic exception handling.
- Frontend and backend integration.

## 4. Database Structure

Database Name: `user_management_db`

### Employee Table

Table Name: `task_employee`

| Column | Data Type |
|---|---|
| Employee_ID | INT |
| Employee_Name | VARCHAR(100) |
| Department | VARCHAR(100) |
| Email | VARCHAR(100) |

### Task Table

Table Name: `employee_tasks`

| Column | Data Type |
|---|---|
| Task_ID | INT |
| Employee_ID | INT |
| Task_Name | VARCHAR(255) |
| Task_Status | VARCHAR(50) |
| Due_Date | DATE |

The Employee_ID in the Task table references the Employee table.

## 5. Project Folder Structure

```text
employee_task_management/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── employees.html
│   └── tasks.html
│
├── static/
│   └── style.css
│
└── README.md
```

## 6. Installation and Setup

### Step 1: Create Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Required Packages

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure MySQL Database

- Start MySQL Server.
- Create or use the configured database.
- Execute the SQL file to create tables and insert sample records.
- Configure the MySQL username, password, and database name in `database.py`.

### Step 5: Run FastAPI Application

```bash
python -m uvicorn main:app --reload
```

## 7. Application URLs

- Home Page: http://127.0.0.1:8000/
- Employee Registration and List: http://127.0.0.1:8000/employees-page
- Add Task and Task List: http://127.0.0.1:8000/tasks-page
- Swagger API Documentation: http://127.0.0.1:8000/docs

## 8. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /employees/ | Add Employee |
| GET | /employees/ | View All Employees |
| POST | /tasks/ | Add Task |
| GET | /tasks/ | View All Tasks |
| GET | /tasks/employee/{employee_id} | Search Task by Employee ID |
| PUT | /tasks/{task_id}/status | Update Task Status |
| DELETE | /tasks/{task_id} | Delete Task |

## 9. Testing

The application APIs and frontend pages are tested using Swagger UI and a web browser.

The following operations are included:
- Employee registration.
- Viewing employee records.
- Adding tasks.
- Viewing task records.
- Searching tasks by Employee ID.
- Updating task status.
- Deleting tasks.

## 10. Conclusion

The Employee Task Management System provides a simple solution for managing employee information and assigned tasks.

The project demonstrates Python programming, SQL database operations, FastAPI development, frontend integration, and database connectivity.