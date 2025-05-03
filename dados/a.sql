CREATE DATABASE vendas_dashboard;
USE vendas_dashboard;

CREATE TABLE vendas (
    OrderID INT PRIMARY KEY,
    Date DATE,
    Category VARCHAR(50),
    Amount DECIMAL(10, 2),
    Units INT
);
