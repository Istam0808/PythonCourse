1. Introduction and Creating first table

# Create table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255) NOT NULL UNIQUE DEFAULT '12345' 
);
```
___
# Insert data
```sql
INSERT INTO users (name, email, password) 
VALUES ('John Doe', 'test@gmail.com', '12345');
```
___
# Select data
```sql
SELECT * FROM users;
```
___
# Update data
```sql
UPDATE users SET name = 'Jane Doe' WHERE id = 1
```
___
# Alter table
```sql
ALTER TABLE users ADD COLUMN age INT
```
___
# Delete data
```sql
DELETE FROM users WHERE id = 1
```
___
# 
```sql
    VARCHAR     => is used to store strings and text
    INT         => is used to store integers
    SERIAL      => is used to auto increment the value
    PRIMARY KEY => is used to set the primary key (it is identical to normal id)
    NULL        => is used to set the field as empty
    NOT NULL    => is used to set the field as required
    UNIQUE      => is used to set the field as unique
    DEFAULT     => is used to set the default value (ex: DEFAULT '...')
```