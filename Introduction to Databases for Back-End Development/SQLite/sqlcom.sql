DROP TABLE Customers;

CREATE TABLE Customers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    sex CHARACTER(1)
);

ALTER TABLE Customers ADD country VARCHAR(50);
ALTER TABLE Customers ADD nationality VARCHAR(100);
ALTER TABLE Customers DROP COLUMN nationality;
-- ALTER TABLE Customers MODIFY country VARCHAR(100);  SQLite doesnt support modify

INSERT INTO Customers (name, age, sex, country) VALUES 
    ("Alex", 20, 'M', "UK"),
    ("Robert", 25, 'M', "Germany"),
    ("Julia", 18, 'W', "Spain");

SELECT * FROM Customers;

select 5 + 5;