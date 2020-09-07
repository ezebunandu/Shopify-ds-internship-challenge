# DROP TABLES
customers_table_drop = "DROP TABLE IF EXISTS Customers"
categories_table_drop = "DROP TABLE IF EXISTS Categories"
employees_table_drop = "DROP TABLE IF EXISTS Employees"
orderDetails_table_drop = "DROP TABLE IF EXISTS OrderDetails"
orders_table_drop = "DROP TABLE IF EXISTS Orders"
products_table_drop = "DROP TABLE IF EXISTS Products"
shippers_table_drop = "DROP TABLE IF EXISTS Shippers"
suppliers_table_drop = "DROP TABLE IF EXISTS Suppliers"

# CREATE TABLES
customers_table_create = ("""CREATE TABLE IF NOT EXISTS Customers
    (
        CustomerID INTEGER PRIMARY KEY,
        CustomerName TEXT,
        ContactName TEXT,
        Address TEXT,
        City TEXT,
        PostalCode TEXT,
        Country TEXT); """)

categories_table_create = ("""
    CREATE TABLE IF NOT EXISTS Categories (
        CategoryID INTEGER PRIMARY KEY,
        CategoryName TEXT,
        Description TEXT);""")

employees_table_create = ("""
    CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INTEGER PRIMARY KEY,
        LastName TEXT,
        FirstName TEXT,
        BirthDate TEXT,
        Photo TEXT,
        Notes TEXT);""")

orderDetails_table_create = ("""CREATE TABLE IF NOT EXISTS OrderDetails (
        OrderDetailID INTEGER PRIMARY KEY,
        OrderID INTEGER,
        ProductID INTEGER,
        Quantity INTEGER);""")

orders_table_create = ("""CREATE TABLE IF NOT EXISTS Orders(
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    EmployeeID INTEGER,
    OrderDate TEXT,
    ShipperID INTEGER);""")


products_table_create = ("""CREATE TABLE IF NOT EXISTS Products(
    ProductID INTEGER PRIMARY KEY,
    ProductName TEXT,
    SupplierID INTEGER,
    CategoryID INTEGER,
    Unit TEXT,
    Price Numeric);""")

shippers_table_create = ("""CREATE TABLE IF NOT EXISTS Shippers(
    ShipperID INTEGER PRIMARY KEY,
    ShipperName TEXT,
    Phone TEXT);""")

suppliers_table_create = ("""CREATE TABLE IF NOT EXISTS Suppliers (
    SupplierID INTEGER PRIMARY KEY,
    SupplierName TEXT,
    ContactName TEXT,
    Address TEXT,
    City TEXT,
    PostalCode TEXT,
    Country TEXT,
    Phone TEXT);""")

# INSERT RECORDS
customers_table_insert = ("""
INSERT INTO
    Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) 
VALUES
    (?, ?, ?, ?, ?, ?, ?);""")

categories_table_insert = ("""
INSERT INTO
    Categories (CategoryID, CategoryName, Description) 
VALUES
    (?, ?, ?);""")

employees_table_insert = ("""
INSERT INTO
    Employees (EmployeeID, LastName, FirstName, BirthDate, Photo, Notes) 
VALUES
    (?, ?, ?, ?, ?, ?);""")

orderDetails_table_insert = ("""
INSERT INTO
    OrderDetails(OrderDetailID, OrderID, ProductID, Quantity) 
VALUES
    (?, ?, ?, ?);""")

orders_table_insert = ("""
INSERT INTO
    Orders (OrderID, CustomerID, EmployeeID, OrderDate, ShipperID) 
VALUES
    (?, ?, ?, ?, ?);""")

products_table_insert = ("""
INSERT INTO
    Products(ProductID, ProductName, SupplierID, CategoryID, Unit, Price) 
VALUES
    (?, ?, ?, ?, ?, ?);""")

shippers_table_insert = ("""
INSERT INTO
    Shippers(ShipperID, ShipperName, Phone) 
VALUES
    (?, ?, ?);""")

suppliers_table_insert = ("""
INSERT INTO
    Suppliers(SupplierID, SupplierName, ContactName, Address, City, PostalCode, Country, Phone) 
VALUES
    (?, ?, ?, ?, ?, ?, ?, ?);""")

# QUERY LISTS
create_table_queries = [customers_table_create, categories_table_create, employees_table_create, orderDetails_table_create,
                       orders_table_create, products_table_create, shippers_table_create, suppliers_table_create]
drop_table_queries = [customers_table_drop, categories_table_drop, employees_table_drop, orderDetails_table_drop, orders_table_drop,
                     products_table_drop, shippers_table_drop, suppliers_table_drop]

insert_queries = [customers_table_insert, categories_table_insert, employees_table_insert, orderDetails_table_insert,
                 orders_table_insert, products_table_insert, shippers_table_insert, suppliers_table_insert]