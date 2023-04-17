CREATE DATABASE edumartdb;

USE edumartdb;

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    quantity_in_stock INT NOT NULL
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    email VARCHAR(255),
    passwd VARCHAR(255) NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE payment_method (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    payment_method VARCHAR(255) NOT NULL,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    sale_date TIMESTAMP NOT NULL,
    customer_id INT,
    product_id INT,
    quantity_sold INT,
    total_amount DECIMAL(10, 2),
    payment_method INT,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
    FOREIGN KEY (product_id) REFERENCES products (product_id),
    FOREIGN KEY (payment_method) REFERENCES payment_method (payment_id)
);

CREATE TABLE admins (
    admin_id INT PRIMARY KEY AUTO_INCREMENT,
    lastname VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    passwd VARCHAR(255)
);

INSERT INTO products (name, description, price, quantity_in_stock) VALUES 
('Ballpen', 'Black ink pen with a ball bearing tip', 10.00, 20),
('Pencil', 'Standard yellow pencil with eraser', 8.00, 20),
('Eraser', 'Soft eraser to remove pencil marks', 5.00, 20),
('Highlighter', 'Fluorescent pen for highlighting important text', 50.00, 20),
('Marker', 'Dry-erase marker for writing on whiteboards', 75.00, 20),
('Notebook', 'Spiral-bound pad of paper for taking notes', 20.00, 20),
('Ruler', '12-inch straight edge for measuring length', 15.00, 20),
('Scissors', 'Sharp tool for cutting paper or other materials', 10.00, 20),
('Glue Stick', 'Adhesive stick for attaching paper or other lightweight materials', 15.00, 20),
('Calculator', 'Electronic device for performing mathematical calculations', 200.00, 20);

INSERT INTO payment_method (payment_method) VALUES 
('Cash'), ('Credit Card'), ('Debit Card'), ('GCash');

INSERT INTO admins (lastname, firstname, passwd) VALUES
('Echevaria','John Leo','Johnleo115');
