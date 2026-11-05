
USE user_management_db;

-- 1. Create Employee Table
CREATE TABLE IF NOT EXISTS task_employee (
    Employee_ID INT AUTO_INCREMENT PRIMARY KEY,
    Employee_Name VARCHAR(100) NOT NULL,
    Department VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL
);

-- 2. Create Task Table
CREATE TABLE IF NOT EXISTS employee_tasks (
    Task_ID INT AUTO_INCREMENT PRIMARY KEY,
    Employee_ID INT NOT NULL,
    Task_Name VARCHAR(255) NOT NULL,
    Task_Status VARCHAR(50) DEFAULT 'Pending',
    Due_Date DATE NOT NULL,
    FOREIGN KEY (Employee_ID)
        REFERENCES task_employee(Employee_ID)
);

-- 3. Insert Sample Employees
INSERT INTO task_employee
(Employee_Name, Department, Email)
VALUES
('Saranya', 'IT', 'saranya@gmail.com'),
('Arun', 'HR', 'arun@gmail.com'),
('Priya', 'Finance', 'priya@gmail.com'),
('Kumar', 'Development', 'kumar@gmail.com'),
('Divya', 'Testing', 'divya@gmail.com');

-- 4. Insert Sample Tasks
INSERT INTO employee_tasks
(Employee_ID, Task_Name, Task_Status, Due_Date)
SELECT Employee_ID, 'Develop Login Page', 'Pending', '2026-11-10'
FROM task_employee WHERE Email = 'saranya@gmail.com';

INSERT INTO employee_tasks
(Employee_ID, Task_Name, Task_Status, Due_Date)
SELECT Employee_ID, 'Prepare Employee Report', 'In Progress', '2026-11-12'
FROM task_employee WHERE Email = 'arun@gmail.com';

INSERT INTO employee_tasks
(Employee_ID, Task_Name, Task_Status, Due_Date)
SELECT Employee_ID, 'Create Budget Report', 'Completed', '2026-11-15'
FROM task_employee WHERE Email = 'priya@gmail.com';

INSERT INTO employee_tasks
(Employee_ID, Task_Name, Task_Status, Due_Date)
SELECT Employee_ID, 'Develop API', 'Pending', '2026-11-18'
FROM task_employee WHERE Email = 'kumar@gmail.com';

INSERT INTO employee_tasks
(Employee_ID, Task_Name, Task_Status, Due_Date)
SELECT Employee_ID, 'Test Application', 'In Progress', '2026-11-20'
FROM task_employee WHERE Email = 'divya@gmail.com';

-- 5. View Employees
SELECT * FROM task_employee;

-- 6. View Tasks with Employee Details (JOIN)
SELECT
    e.Employee_ID,
    e.Employee_Name,
    e.Department,
    t.Task_ID,
    t.Task_Name,
    t.Task_Status,
    t.Due_Date
FROM task_employee e
INNER JOIN employee_tasks t
ON e.Employee_ID = t.Employee_ID;
