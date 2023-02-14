-- Following SQL code is used for the creation of the store database

CREATE TABLE
    employees(
        id INTEGER PRIMARY KEY,
        employee_code VARCHAR(10) UNIQUE,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        emp_type VARCHAR(50) NOT NULL,
        is_owner VARCHAR(5) NOT NULL,
        is_shiftleader VARCHAR(5) NOT NULL,
        start_date VARCHAR(20) NOT NULL,
        active VARCHAR(3) NOT NULL
    );

CREATE TABLE 
    members(
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(20),
        email VARCHAR(150)
    );

CREATE TABLE   
    orders(
        id INTEGER PRIMARY KEY,
        order_date DATE NOT NULL,
        employee_code VARCHAR (5),
        tax_total INTEGER NOT NULL,
        total_price INTEGER NOT NULL,
        member_id INTEGER,
        FOREIGN KEY (employee_code) REFERENCES employees(employee_code),
        FOREIGN KEY (member_id) REFERENCES members(id) 
    );

CREATE TABLE 
    products(
        id INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description VARCHAR(255) NOT NULL,
        stock INTEGER NOT NULL,
        price INTEGER NOT NULL,
        tax INTEGER NOT NULL
    );

CREATE TABLE
    order_details(
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        product_price INTEGER,
        order_id INTEGER,
        subtax INTEGER,
        subtotal Integer,
        FOREIGN KEY (product_id) REFERENCES products(id),
        FOREIGN KEY (order_id) REFERENCES orders(id)
    );

