CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO Employees (id, name, salary) VALUES
(1, 'Arjun', 50000.00),
(2, 'Priya', 60000.00),
(3, 'Ravi', 55000.00),
(4, 'Sneha', 70000.00),
(5, 'Anil', 65000.00),
(6, 'Veena', 48000.00),
(7, 'Rajesh', 72000.00),
(8, 'Kavita', 53000.00),
(9, 'Suresh', 62000.00),
(10, 'Meena', 58000.00);

SELECT * FROM Employees;

ALTER TABLE Employees
ADD COLUMN age INT;

UPDATE Employees SET age = 28 WHERE id = 1;
UPDATE Employees SET age = 32 WHERE id = 2;
UPDATE Employees SET age = 25 WHERE id = 3;
UPDATE Employees SET age = 30 WHERE id = 4;
UPDATE Employees SET age = 29 WHERE id = 5;
UPDATE Employees SET age = 26 WHERE id = 6;
UPDATE Employees SET age = 35 WHERE id = 7;
UPDATE Employees SET age = 60 WHERE id = 8;
UPDATE Employees SET age = 31 WHERE id = 9;
UPDATE Employees SET age = 33 WHERE id = 10;

SELECT * FROM Employees;

SELECT MAX(salary) AS MaxSalary FROM Employees;

SELECT MIN(salary) AS MinSalary FROM Employees;

SELECT AVG(salary) AS AverageSalary FROM Employees;

DELETE FROM Employees
WHERE age >= 60;
