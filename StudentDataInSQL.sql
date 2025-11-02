-- Create a Table of Students
CREATE TABLE Students (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    dob DATE,
    marks INT
);

-- Insert Data into the Table
INSERT INTO Students (roll_no, name, dob, marks) VALUES
(1, 'Mahima', '2005-01-12', 89),
(2, 'Mayank', '2004-11-23', 75),
(3, 'Minakshi', '2005-05-19', 92),
(4, 'Aditya', '2003-07-02', 66);

-- Show All Data
SELECT * FROM Students;

-- Find Students with Marks Above 80
SELECT name, marks FROM Students
WHERE marks > 80;

-- Update Marks of a Student
UPDATE Students
SET marks = 95
WHERE name = 'Mahima';

-- Delete a Student
DELETE FROM Students
WHERE roll_no = 4;

-- Count Number of Students
SELECT COUNT(*) AS total_students FROM Students;

-- Order Students by Marks (Topper First)
SELECT name, marks
FROM Students
ORDER BY marks DESC;
