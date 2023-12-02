3. Syntax items - Continue of the second lesson


```sql
CREATE TABLE Customers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);
CREATE TABLE Orders (
  id SERIAL PRIMARY KEY,
  order_date DATE NOT NULL,
  total DECIMAL(10,2) NOT NULL,
  customer_id INTEGER NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES Customers (id)
);
INSERT INTO Customers (name, email)
VALUES ('John Doe', 'test@mail.com');

INSERT INTO Orders (order_date, total, customer_id)
VALUES ('2022-01-01', 100.00, 1);

INSERT INTO Orders (order_date, total, customer_id)
VALUES ('2022-02-01', 150.00, 1);

SELECT * FROM Customers;
SELECT * FROM Orders;
```

<!-- [==============================================================================] -->


```sql
-- Let's say we have two tables: Students and Courses. 
-- Each student can enroll in multiple courses, so we want to create a 
-- relationship between the two tables using the FOREIGN KEY constraint.

CREATE TABLE Students (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);

CREATE TABLE Courses (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  instructor VARCHAR(255) NOT NULL
);

CREATE TABLE Enrollments (
  id SERIAL PRIMARY KEY,
  student_id INTEGER NOT NULL,
  course_id INTEGER NOT NULL,
  FOREIGN KEY (student_id) REFERENCES Students (id),
  FOREIGN KEY (course_id) REFERENCES Courses (id)
);

INSERT INTO Courses (name, instructor) 
VALUES ('Math', 'Mr. Smith'),
       ('Science', 'Mrs. Smith'),
       ('English', 'Mr. Jones');

INSERT INTO Students (name, email)
VALUES ('John Smith', 'test@mail.com'),
        ('Matthew', 'test2@mail.com');

SELECT * FROM students;

INSERT INTO Enrollments (student_id, course_id)
VALUES 
      (1, 1),
      (1, 2),
      (1, 3);
SELECT * FROM Enrollments;

-- This means that the student with an id of 1 is enrolled in the course with an id of 1
```

<!-- [==============================================================================] -->
**MONEY**
Working with money
In postgres, the money type is a fixed-point number with two decimal places. It is useful for storing monetary amounts. The money type is not precise, because it rounds to the nearest cent. For example, 
1.005 is stored as 1.01.

To use the money type, you must specify the amount in the following format: '$100.00'. The dollar sign is required. You can also use the following format: '100.00 USD'. The currency code is optional.

To create a table with the money type, you use the following syntax:
```sql
-- 1.000001  =>  1.01

INSERT INTO laptops (id, ip_address, price)
VALUES ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd312a11', '192.168.0.138', '$200');

SELECT * FROM laptops;
-- [==============================================================================] 

**SUBSTRING()** - Extracts a substring from a string
```sql
SYNTAX:  SELECT SUBSTRING(column_name, start_position, length) FROM table_name;

SELECT SUBSTRING(name, 1, 3) AS FirstName FROM students;
This will return the first 3 characters of the first name column
So if: first_name = 'John'
The result will be: 'Joh'
```
<!-- -------------------------------------------------------------------------------- -->
**MAX()** - Returns the maximum value in a set of values
```sql
SELECT MAX(price) FROM products;
```
<!-- -------------------------------------------------------------------------------- -->
**MIN()** - Returns the minimum value in a set of values
```sql
SELECT MIN(price) FROM products;
```
<!-- -------------------------------------------------------------------------------- -->
**AVG()** - Returns the average value in a set of values
```sql
SELECT AVG(price) FROM products;
```
<!-- -------------------------------------------------------------------------------- -->
**SUM()** - Returns the sum of all or distinct values in a set of values
```sql
SELECT SUM(price) FROM products;
```
<!-- -------------------------------------------------------------------------------- -->
**COUNT()** - Returns the number of rows that matches a specified criteria
**COUNT(DISTINCT)** - Returns the number of distinct rows that matches a specified criteria
```sql
SELECT COUNT(*) FROM products;
SELECT COUNT(DISTINCT price) FROM products;
```
<!-- -------------------------------------------------------------------------------- -->
**ROUND()** - Rounds a number to a specified number of decimal places
```sql
SYNTAX:  SELECT ROUND(column_name, number_of_decimal_places) FROM table_name;

SELECT ROUND(price, 2) FROM products;
-- This will return the price column rounded to 2 decimal places
-- ex:
--    price  = 10.1234
--    result = 10.12
```
<!-- -------------------------------------------------------------------------------- -->
**CONCAT()** - Adds two or more expressions together
```sql
SELECT CONCAT(first_name, ' ', last_name) AS Full_Name FROM customers;
```
<!-- -------------------------------------------------------------------------------- -->
**UNION**  - Combines the result of two or more SELECT statements

    The queries in the union must follow these rules:
      They must have the same number of columns
      The columns must have the same data types
      The columns must be in the same order
      
      NOTE: The UNION operator selects only distinct values by default. 
            To allow duplicate values, use the UNION ALL operator.
```sql
-- SELECT * FROM customers;
-- SELECT * FROM students;

SELECT name, email FROM customers
UNION
SELECT name, email FROM students;
```
<!-- -------------------------------------------------------------------------------- -->
**UNION ALL** - Combines the result of two or more SELECT statements, 
                but it does not remove duplicate rows
```sql
SELECT first_name, last_name FROM customers
UNION ALL
SELECT first_name, last_name FROM employees;
```
<!-- -------------------------------------------------------------------------------- -->
**ORDER BY**  - Sorts the result set in ascending or descending order
```sql
SELECT * FROM customers ORDER BY first_name;
SELECT * FROM customers ORDER BY first_name DESC;
```
<!-- -------------------------------------------------------------------------------- -->
**GROUP BY** - Groups rows that have the same values into summary rows
```sql
SELECT * FROM customers GROUP BY first_name;

<!-- -------------------------------------------------------------------------------- -->
*Merging two or more columns*

```sql
-- Lets say we have a table with the following data:

-- Customers TABLE
-- ___________________________________________________
-- -- id | name  | surname | full_name | email
-- -- 1  | John  | test1   |          | John@test.com
-- -- 2  | Mary  | test2   |          | Mary@test.com
-- -- 3  | Peter | test3   |          | Peter@test.com
-- ___________________________________________________

-- We want to add a new column called full_name and populate it with the first name and last name
-- We can do this using the CONCAT() function

-- ALTER TABLE customers ADD COLUMN full_name VARCHAR(255);
-- UPDATE customers SET full_name = CONCAT(name, ', email: ', email);

```