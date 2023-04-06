import mysql.connector
import time
import os


class Retail:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Johnleo1152003.'
        )

        self.cursor = self.db.cursor()

    def database_creation(self):
        # Check if database exists
        self.cursor.execute("SHOW DATABASES")
        database = self.cursor.fetchall()
        db_exist = False

        for db in database:
            if 'retaildb' in db:
                db_exist = True
                break

        # Create database if it does not exist
        if not db_exist:
            print("Creating RetailDB Database...")
            time.sleep(2)

            # Create RetailDB database
            self.cursor.execute("CREATE DATABASE retailDB")

            # Use RetailDB database
            self.cursor.execute("USE RetailDB")

            # Execute CREATE TABLE statements
            self.cursor.execute("CREATE TABLE products ("
                                "product_id INT PRIMARY KEY AUTO_INCREMENT,"
                                "name VARCHAR(255) NOT NULL,"
                                "description TEXT,"
                                "price DECIMAL(10, 2) NOT NULL,"
                                "quantity_in_stock INT NOT NULL);")

            self.cursor.execute("CREATE TABLE customers ("
                                "customer_id INT PRIMARY KEY AUTO_INCREMENT,"
                                "name VARCHAR(255) NOT NULL,"
                                "contact_number VARCHAR(15) NOT NULL,"
                                "email VARCHAR(255),"
                                "address TEXT NOT NULL);")

            self.cursor.execute("CREATE TABLE sales ("
                                "sale_id INT PRIMARY KEY AUTO_INCREMENT,"
                                "sale_date TIMESTAMP NOT NULL,"
                                "customer_id INT,"
                                "product_id INT,"
                                "quantity_sold INT,"
                                "total_amount DECIMAL(10, 2),"
                                "FOREIGN KEY (customer_id) REFERENCES customers (customer_id),"
                                "FOREIGN KEY (product_id) REFERENCES products (product_id));")

            self.cursor.execute("CREATE TABLE admins ("
                                "admin_id INT PRIMARY KEY AUTO_INCREMENT,"
                                "lastname VARCHAR(255) NOT NULL,"
                                "firstname VARCHAR(255) NOT NULL,"
                                "passwd VARCHAR(255));")

            self.cursor.execute("CREATE TABLE inventory ("
                                "inventory_id INT PRIMARY KEY AUTO_INCREMENT,"
                                "product_id INT,"
                                "quantity_in_stock INT,"
                                "FOREIGN KEY (product_id) REFERENCES products (product_id));")

            # Insert data into tables
            products = [("Ballpoint Pen", "Black ink pen with a ball bearing tip", 10.00, 20),
                        ("Pencil", "Standard yellow pencil with eraser", 8.00, 20),
                        ("Eraser", "Soft eraser to remove pencil marks", 5.00, 20),
                        ("Highlighter", "Fluorescent pen for highlighting important text", 50.00, 20),
                        ("Whiteboard Marker",
                        "Dry-erase marker for writing on whiteboards", 75.00, 20),
                        ("Notebook", "Spiral-bound pad of paper for taking notes", 20.00, 20),
                        ("Ruler", "12-inch straight edge for measuring length", 15.00, 20),
                        ("Scissors", "Sharp tool for cutting paper or other materials", 10.00, 20),
                        ("Glue Stick", "Adhesive stick for attaching paper or other lightweight materials", 15.00, 20),
                        ("Calculator", "Electronic device for performing mathematical calculations", 200.00, 20)]

            for product in products:
                self.cursor.execute(
                    "INSERT INTO products (name, description, price, quantity_in_stock) VALUES (%s, %s, %s, %s)", product)

            self.cursor.execute(
                'INSERT INTO admins (lastname, firstname, passwd) VALUES ("Echevaria", "John Leo", "Johnleo115")')

            # Commit changes and close self.cursor and connection
            self.db.commit()

            os.system('cls')
            print("RetailDB Database created")
            time.sleep(2)

        else:
            print("RetailDB Database already exists")
            time.sleep(2)

    def log_in(self):

        self.cursor.execute("USE RetailDB")

        # Log in to the system
        print("Log in to the system\n")

        # Admin or Customer
        user_type = input("Admin or Customer: ").lower()

        while True:
            os.system('cls')
            if user_type == "admin":
                admin = int(input("Admin ID: "))
                password = input("Password: ")

                # Check if username and password are correct
                self.cursor.execute(
                    f"SELECT * FROM admins WHERE admin_id = {admin} AND BINARY passwd = '{password}'")
                user = self.cursor.fetchone()

                if user:
                    print("\nLog in successful")
                    return "admin"
                else:
                    print("\nLog in failed")

            elif user_type == "customer":
                customer_status = input(
                    "Existing member or new member (Type: Existing/New): ").lower()
                if customer_status == "existing":
                    customer_id = int(input("Customer ID: "))
                    self.cursor.execute(
                        f"SELECT * FROM customers WHERE customer_id = {customer_id}")
                    customer = self.cursor.fetchone()

                    if customer:
                        print("\nLog in successful")
                        return "customer"
                    else:
                        print("\nLog in failed")

                elif customer_status == "new":
                    customer_name = input("\nName: ")
                    customer_contact = input("Contact number: ")
                    customer_email = input("Email: ")
                    customer_address = input("Address: ")

                    self.cursor.execute(
                        f"INSERT INTO customers (name, contact_number, email, address) VALUES ('{customer_name}', '{customer_contact}', '{customer_email}', '{customer_address}')")

                    self.db.commit()

                    print("\nLog in successful")
                    return "customer"
