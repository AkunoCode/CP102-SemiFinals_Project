# CP102 SemiFinal Term Project - CRUD Operations with Python and MySQL (EduMart)

This is a Python program for managing the EduMart school supplies store using MySQL database with mysql.connector module. The program contains a Store class with various methods for managing the store's products, customers, sales, and admins.

This project is a requirement for the course "Computer Programming 2" (CP102) in the 2nd semester of academic year 2022-2023 in Manuel S. Enverga University Foundation. The goal of this project is to create a Python program that performs CRUD operations in a database using Structured Query Language (SQL).

## Project Outcome
The outcome of this project is a Python program that can:

* Create a new record in the database
* Retrieve an existing record from the database
* Update an existing record in the database
* Delete an existing record from the database
* The program will interact with the database using SQL commands, which will be executed using a Python SQL library (mysql.connector).

## Files in the Repository
- `EduMart.py`: The Python program that contains the `Store` class with the various methods for managing the store's products, customers, sales, and admins.

| Methods in EduMart.py | Description |
| --- | --- |
| `database()` | Checks if the edumartdb database exists and creates it if it doesn't. It also creates the tables for product, customer, payment_method, sales, and admins, and inserts initial values to the product and payment_method tables. It also prompts the user to create an admin account by asking for their last name, first name, and password. Returns the name of the database. |
| `admin_login()` | Allows an admin to log in with their account info from the database. |
| `customer_login()` | Allows a customer to log in with their account info from the database. |
| `customer_register()` | Prompts the user to input information to create a new customer account. |
| `view_product()` | Prints the products in a table format. |
| `view_sales()` | Prints the sales in a table format. Only accessible by admins. |
| `view_customers()` | Prints the customers in a table format. Only accessible by admins. |
| `view_admins()` | Prints the admins in a table format. Only accessible by admins. |
| `add_product()` | Prompts the user to input information to create a new product to be inserted in the products table in the database. Only accessible by admins. |
| `add_admin()` | Creates new admin by prompting the user to input information. Only accessible by admins. |
| `remove_product()` | Allows admins to remove a product from the products table in the database. |
| `update_product()` | Allows admins to update a product's information in the products table in the database. |
| `restock_product()` | Allows admins to restock a product's quantity in the products table in the database. |
| `customer_edit()` | Allows customers to change their information in the customers table in the database. |
| `customer_buy()` | Calls the `view_product()` method to display the products to the user and asks them for the product_id and quantity. The price will automatically be calculated and the user will be prompted to choose a payment method. After confirming the info, it will be inserted into the sales table in the database, and the quantity will be deducted from the stocks of the product table. |
| `custom_search()` | Allows the customer to search for products based on matching text or matching price range |

- `Main.py`: The main program that allows users to log in as either an admin or a customer and perform various actions.
- `EduMartDB.sql`: The mysql script for the EduMartDB. Same program is already included inside the EduMart class.
- `EduMartDB_Model.png`: ER Diagram for EduMartDB Schema

<p align="center">
  <img src="https://github.com/AkunoCode/CP102-SemiFinals_Project/blob/main/EduMartDB_Model.png?raw=true" alt="ER diagram for EduMartDB schema">
</p>

## Usage
To use the program, simply run `Main.py`. The program will prompt the user to log in as either an admin or a customer, and then perform various actions depending on the user's choice.
