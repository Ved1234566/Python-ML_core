Create database School;

use school;

CREATE TABLE student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT CHECK (age BETWEEN 17 AND 30),
    department VARCHAR(50) NOT NULL
);

INSERT INTO student (name, email, age, department)
SELECT
    CONCAT('Student_', n),
    CONCAT('student', n, '@college.com'),
    FLOOR(18 + RAND() * 10),
    ELT(FLOOR(1 + RAND() * 4),
        'Computer Science',
        'Mechanical',
        'Electrical',
        'Civil')
FROM (
    SELECT @row := @row + 1 AS n
    FROM information_schema.tables t1,
         information_schema.tables t2,
         (SELECT @row := 0) r
    LIMIT 1000
) numbers;
INSERT INTO student (name, email, age, department)
SELECT
    CONCAT('Student_', n),
    CONCAT('student', n, '@college.com'),
    FLOOR(18 + RAND() * 10),
    ELT(FLOOR(1 + RAND() * 4),
        'Computer Science',
        'Mechanical',
        'Electrical',
        'Civil')
FROM (
    SELECT @row := @row + 1 AS n
    FROM information_schema.tables t1,
         information_schema.tables t2,
         (SELECT @row := 0) r
    LIMIT 1000
) numbers;
INSERT INTO student (name, email, age, department)
SELECT
    CONCAT('Student_', n),
    CONCAT('student', n, '@college.com'),
    FLOOR(18 + RAND() * 10),
    ELT(FLOOR(1 + RAND() * 4),
        'Computer Science',
        'Mechanical',
        'Electrical',
        'Civil')
FROM (
    SELECT @row := @row + 1 AS n
    FROM information_schema.tables t1,
         information_schema.tables t2,
         (SELECT @row := 0) r
    LIMIT 1000
) numbers;

SELECT COUNT(*) FROM student;

select * from student
limit 10;