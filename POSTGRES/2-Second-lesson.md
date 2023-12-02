2. Data types and constraints and operators
   RU: Типы данных и ограничения и операторы
   UZ: Ma'lumot turlari va cheklovlar va operatorlar

# Data types 
<!-- https://www.educative.io/answers/what-are-the-data-types-in-postgresql -->

In total there are 49 data types in PostgreSQL. 
The most common ones in count are 10
They are: 
> ------------------------------------------------------------
> - **Boolean**                 (TRUE/FALSE)
>   ex:     CREATE TABLE customers (name TEXT, is_active BOOLEAN)
> ------------------------------------------------------------
> - **Character types**         (CHAR, VARCHAR, TEXT)
    The main difference between CHAR and VARCHAR is that CHAR is fixed length and VARCHAR is variable length.
    The TEXT type is used for storing longer strings. It has no fixed length.

    The difference between fixed length and variable length is that fixed length is faster to process than variable length. And it takes less space.
    The similarity between fixed length and variable length is that they both store strings of any length.

>       CHAR (Fixed length)          maximum characters 255
>           ex: CHAR(10) 'Hello'
>               CREATE TABLE customers (name CHAR(10), address CHAR(10))
>       VARCHAR (Variable length)    maximum characters 65535
>           ex: VARCHAR(10) 'Hello'
>       TEXT (Variable unlimited)    maximum characters 65535
>           ex: TEXT 'Hello'
>               CREATE TABLE customers (name TEXT, address TEXT)
> ------------------------------------------------------------
> - **Numeric types**           (INTEGER, BIGINT, DECIMAL, NUMERIC)
>       INTEGER (Whole numbers)       maximum characters 10
>           ex: INTEGER 2147483647
>       BIGINT  (Large whole numbers) maximum characters 19
>           ex: BIGINT 9223372036854775807
>       DECIMAL (Fixed precision)     maximum characters 131072
>           ex: DECIMAL(3,2) 999.99
>       NUMERIC (Variable precision)  maximum characters 131072
>           ex: NUMERIC(5,2) 999.99
> ------------------------------------------------------------
> - **Date/time types**         (DATE, TIME, TIMESTAMP)
>       DATE (Stores date only)       maximum characters 10
>           ex: DATE '2018-01-01'
>       TIME (Stores time only)       maximum characters 8
>           ex: TIME '12:00:00'
>       TIMESTAMP (Stores date and time) maximum characters 26
>           ex: TIMESTAMP '2018-01-01 12:00:00'
> 
> CREATE TABLE users(last_login TIMESTAMP)
> INSERT INTO ... (last_login) VALUES ('2018-01-01 12:00:00')  || (NOW())
> ------------------------------------------------------------
> - **INTERVAL**                (stores periods of time)
>       SYNTAX:  INTERVAL 'value' unit
>       UNITS:   year, month, day, hour, minute, second, week, decade, century, 
> millennium
>          ex:  '1 year 2 months 2 days ...'
>
> - ex 1:
```sql
SELECT * FROM orders WHERE order_date > NOW() - INTERVAL '30 days';
-- Заказы, сделанные за последние 30 дней
```

> - ex 2:
```sql
CREATE TABLE events (
   id SERIAL PRIMARY KEY,
   event_name VARCHAR(255) NOT NULL,
   start_time TIMESTAMP NOT NULL,
   duration INTERVAL NOT NULL
);
INSERT INTO events (event_name, start_time, duration)
VALUES (
         'Birthday Party', 
         TIMESTAMP '2024-01-01 12:00:00', 
         INTERVAL '2 hours'
      );
```
> ------------------------------------------------------------
> - **Composite types**         (stores groups of columns)
    This is used to store groups of columns.
    In python we have tuples. In PostgreSQL we have composite types.
>       Composite types (stores groups of columns) maximum characters 131072
>           ex: CREATE TYPE address AS (street TEXT, city TEXT, zip INTEGER)   
>               => we can use this type in a table 
>                  ex: CREATE TABLE customers (name TEXT, address address)
>                      INSERT INTO customers VALUES ('John Doe', ('123 Main St.', 'Pittsburgh', 15237))
>           ex: CREATE TABLE customers (name TEXT, address address)
> ------------------------------------------------------------
> > - **Arrays**                  (stores arrays of data)
>       ARRAY (Stores arrays of data) maximum characters 131072
>           ex: ARRAY[1,2,3]
>               ARRAY['John', 'Jane']
>               CREATE TABLE customers (
>                       name TEXT, 
>                       address DEFAULT TEXT['123 Main St.', 'Pittsburgh', '15237']
>               )
> ------------------------------------------------------------
> - **Network address types**   (INET, CIDR, MACADDR)
    This is used to store network IP addresses and MAC addresses.
>           ex: CREATE TABLE customers (name TEXT, ip_address INET)  =>  
>               INET here is the type of the column ip_address
>               and it can store IPv4 and IPv6 addresses
>               This is recognized as needed because there could be cases
>               where we need to store the IP address of a customer because
>               we want to track where they are coming from.
> ------------------------------------------------------------
> - **UUID**                    (stores Universally Unique Identifiers)
    [8 digits]-[4 digits]-[4 digits]-[4 digits]-[12 digits]
    
    The difference between SERIAL and UUID is that SERIAL is a sequential number and UUID is a random number.
    For example, if we have a table of customers and we want to assign a unique ID to each customer, we can use SERIAL.
    If we want to assign a unique ID to each customer and we don't want to expose the number of customers we have, we can use UUID.
>           ex: CREATE TABLE customers (name TEXT, id UUID PRIMARY KEY)
> ------------------------------------------------------------
> - **XML**                     (stores XML data)
    XML looks like HTML but it is not the same. 
    XML is used to store data and HTML is used to display data.
    HTML is designed to be read by humans, while XML is designed to be read by machines.
>           ex: CREATE TABLE customers (name TEXT, info XML)
> ------------------------------------------------------------

# Constraints
    The constraints are used to limit the type of data that can go into a table.
    Constraints can be column level or table level.
    Column level constraints are applied only to one column, while table level constraints are applied to the whole table.
    RU: Ограничения используются для ограничения типа данных, которые могут попасть в таблицу.
    Ограничения могут быть уровня столбца или уровня таблицы.
    Ограничения уровня столбца применяются только к одному столбцу, в то время как ограничения 
    уровня таблицы применяются ко всей таблице.
    
    In total there are 6 constraints in PostgreSQL.
> - **NOT NULL**    => CREATE TABLE customers (name TEXT NOT NULL)
> - **UNIQUE**      => CREATE TABLE customers (name TEXT UNIQUE)
> - **PRIMARY KEY** => CREATE TABLE customers (id SERIAL PRIMARY KEY, name TEXT)
> - **FOREIGN KEY** => CREATE TABLE customers (id SERIAL PRIMARY KEY, name TEXT)
    The difference between PRIMARY KEY and FOREIGN KEY is that 
    PRIMARY KEY is used to uniquely identify a row in a table.
    FOREIGN KEY is used to reference a column in ANOTHER TABLE.
    

> - **CHECK**       => CREATE TABLE customers (name TEXT, age INTEGER CHECK (age >= 18))
> - **EXCLUDE**     => SELECT * FROM users EXCLUDE age = 18;
>                  =>   This constraint is used to exclude data from a table.
>                       For example, if we have a table of customers and we want to exclude customers with the same name and age.
> ------------------------------------------------------------
# Operators in the WHERE clause
> - =	      Equal to   =>  in python we had  == 
> --------------------
> - <	      Less than
> --------------------
> - >	      Greater than
> --------------------
> - <=	      Less than or equal to
> --------------------
> - >=	      Greater than or equal to
> --------------------
> - <>	      Not equal to    =>   in python we use  != 
>         ex: SELECT * FROM customers WHERE name <> 'John'
> --------------------
> - !=	      Not equal to
> --------------------
> - LIKE	  Check if a value matches a pattern (case sensitive)
>         ex: SELECT * FROM customers WHERE name LIKE 'John%' 
>             => this will return all customers with name starting with 
>                 John (% means any number of characters after John)
> --------------------
> - ILIKE	  Check if a value matches a pattern (case insensitive)
>         ex: SELECT * FROM customers WHERE name ILIKE 'John%'
> --------------------
> - AND	      Logical AND
>         ex: SELECT * FROM customers WHERE name ILIKE 'John%' AND age > 18
> --------------------
> - OR	      Logical OR
>         ex: SELECT * FROM customers WHERE name ILIKE 'John%' OR age > 18
> --------------------
> - IN	      Check if a value is between a range of values
>         ex: SELECT * FROM customers WHERE age IN [18, 19, 20] OR age > 30
> --------------------
> - BETWEEN	  Check if a value is between a range of values
>         ex: SELECT * FROM customers WHERE age BETWEEN 18 AND 30
> --------------------
> - IS NULL	  Check if a value is NULL
>         ex: SELECT * FROM customers WHERE age IS NULL
> --------------------
> - NOT	      Makes a negative result e.g. NOT LIKE, NOT IN, NOT BETWEEN
>         ex: SELECT * FROM customers WHERE age NOT BETWEEN 18 AND 30

# Distinct and Limit and their variations
> - **DISTINCT**	  Select only distinct (different) values
>        ex: SELECT DISTINCT name FROM customers  
>            => this will return all distinct names from the customers table
>               which means that if there are two customers with the same name
>               only one of them will be returned
> --------------------
> - **COUNT**	  Count number of rows returned
>       ex: SELECT COUNT(DISTINCT age) FROM customers
>          => this will return the number of distinct ages from the customers table
> --------------------
> - **LIMIT**	  Limit number of rows returned
>       ex: SELECT * FROM customers LIMIT 10
>           => this will return only 10 rows from the customers table
> --------------------
> - **OFFSET**	  Skip number of rows before starting to return the rows
>      ex: SELECT * FROM customers LIMIT 10 OFFSET 10
>         => this will return 10 rows from the customers table starting from the 10th row
> --------------------
> - **FETCH**	  Limit number of rows returned
>          FETCH vs LIMIT
>          LIMIT is the same as FETCH but it is more flexible
>          LIMIT can be used with OFFSET but FETCH cannot 
> 
>     ex: SELECT * FROM customers FETCH FIRST 10 ROWS ONLY
>        => this will return only 10 rows from the customers table
> --------------------