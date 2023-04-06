import datetime
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

            # Insert data into product table
            products = [("Ballpen", "Black ink pen with a ball bearing tip", 10.00, 20),
                        ("Pencil", "Standard yellow pencil with eraser", 8.00, 20),
                        ("Eraser", "Soft eraser to remove pencil marks", 5.00, 20),
                        ("Highlighter", "Fluorescent pen for highlighting important text", 50.00, 20),
                        ("Marker", "Dry-erase marker for writing on whiteboards", 75.00, 20),
                        ("Notebook", "Spiral-bound pad of paper for taking notes", 20.00, 20),
                        ("Ruler", "12-inch straight edge for measuring length", 15.00, 20),
                        ("Scissors", "Sharp tool for cutting paper or other materials", 10.00, 20),
                        ("Glue Stick", "Adhesive stick for attaching paper or other lightweight materials", 15.00, 20),
                        ("Calculator", "Electronic device for performing mathematical calculations", 200.00, 20)]

            for product in products:
                self.cursor.execute(
                    "INSERT INTO products (name, description, price, quantity_in_stock) VALUES (%s, %s, %s, %s)", product)

            # Insert data into admins
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
                    time.sleep(2)
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
                        time.sleep(2)
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
                    time.sleep(2)
                    return "customer"

    def admin_restock(self):
        # Restock items back to its starting quantity
        self.cursor.execute("USE RetailDB")

        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()

        for product in products:
            self.cursor.execute(
                f"UPDATE products SET quantity_in_stock = 20 WHERE product_id = {product[0]}")

        self.db.commit()

        print("Restock successful")
        time.sleep(2)

    def admin_view_inventory(self):
        # View inventory
        self.cursor.execute("USE RetailDB")

        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()

        print("Product ID\tName\t\t\tPrice\t\tQuantity in Stock")

        for product in products:
            if len(product[1]) >= 8:
                space = 2
            else:
                space = 3
            print(
                f"{product[0]}\t\t{product[1]}"+"\t"*space+f"{product[3]}\t\t{product[4]}")

        input("\nPress enter to continue...")
        time.sleep(2)

    def admin_view_sales(self):
        # View sales
        self.cursor.execute("USE RetailDB")

        self.cursor.execute("SELECT * FROM sales")
        sales = self.cursor.fetchall()

        print(
            "Sale ID\t\tSale Date\t\t\tCustomer ID\tProduct ID\tQuantity Sold\tTotal Amount")

        for sale in sales:
            print(
                f"{sale[0]}\t\t{sale[1]}\t\t{sale[2]}\t\t{sale[3]}\t\t{sale[4]}\t\t{sale[5]}")

        input("\nPress enter to continue...")
        time.sleep(2)

    def admin_view_customers(self):
        # View customers
        self.cursor.execute("USE RetailDB")

        self.cursor.execute("SELECT * FROM customers")
        customers = self.cursor.fetchall()

        print("Customer ID\tName\t\t\t\tContact Number\t\tEmail\t\t\tAddress")

        for customer in customers:
            print(
                f"{customer[0]}\t\t{customer[1]}\t\t{customer[2]}\t\t{customer[3]}\t\t{customer[4]}")

        input("\nPress enter to continue...")
        time.sleep(2)

    def admin_view_admins(self):
        # View admins
        self.cursor.execute("USE RetailDB")

        self.cursor.execute("SELECT * FROM admins")
        admins = self.cursor.fetchall()

        print("Admin ID\tName\t\t\t\tPassword")

        for admin in admins:
            print(
                f"{admin[0]}\t\t{admin[1]} {admin[2]}\t\t{admin[3]}")

        input("\nPress enter to continue...")
        time.sleep(2)

    def admin_add_product(self):
        # Add product
        self.cursor.execute("USE RetailDB")

        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()

        print("Product ID\tName\t\t\tPrice\t\tQuantity in Stock")

        for product in products:
            if len(product[1]) >= 8:
                space = 2
            else:
                space = 3
            print(
                f"{product[0]}\t\t{product[1]}"+"\t"*space+f"{product[3]}\t\t{product[4]}")

        product_name = input("\nProduct name: ")
        product_description = input("Product description: ")
        product_price = float(input("Product price: "))
        product_quantity = int(input("Product quantity: "))

        self.cursor.execute(
            f"INSERT INTO products (name, description, price, quantity_in_stock) VALUES ('{product_name}', '{product_description}', {product_price}, {product_quantity})")

        self.db.commit()

        print("Product added")
        time.sleep(2)

    def admin_remove_product(self):
        # Remove product
        self.cursor.execute("USE RetailDB")

        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()

        print("Product ID\tName\t\t\tPrice\t\tQuantity in Stock")

        for product in products:
            if len(product[1]) >= 8:
                space = 2
            else:
                space = 3
            print(
                f"{product[0]}\t\t{product[1]}"+"\t"*space+f"{product[3]}\t\t{product[4]}")

        product_id = int(input("\nProduct ID: "))

        self.cursor.execute(
            f"DELETE FROM products WHERE product_id = {product_id}")

        self.db.commit()

        print("Product removed")
        time.sleep(2)

    def admin_update_product(self):
        # Update product
        self.cursor.execute("USE RetailDB")

        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()

        print("Product ID\tName\t\t\tPrice\t\tQuantity in Stock")

        for product in products:
            if len(product[1]) >= 8:
                space = 2
            else:
                space = 3
            print(
                f"{product[0]}\t\t{product[1]}"+"\t"*space+f"{product[3]}\t\t{product[4]}")

        product_id = int(input("\nProduct ID: "))
        product_name = input("Product name: ")
        product_description = input("Product description: ")
        product_price = float(input("Product price: "))
        product_quantity = int(input("Product quantity: "))

        self.cursor.execute(
            f"UPDATE products SET name = '{product_name}', description = '{product_description}', price = {product_price}, quantity_in_stock = {product_quantity} WHERE product_id = {product_id}")

        self.db.commit()

        print("Product updated")
        time.sleep(2)

        def customer_buy(self):
            # Display the products
            self.cursor.execute("SELECT * FROM products")
            products = self.cursor.fetchall()

            print("Product ID\tName\t\t\tPrice\t\tQuantity in Stock")

            for product in products:
                if len(product[1]) >= 8:
                    space = 2
                else:
                    space = 3
                print(
                    f"{product[0]}\t\t{product[1]}"+"\t"*space+f"{product[3]}\t\t{product[4]}")

            # Get the product ID
            product_id = int(input("\nProduct ID: "))
            # Get the quantity
            quantity = int(input("Quantity: "))
            # Get the customer ID
            customer_id = int(input("Customer ID: "))
            # Get the date
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Get the price by multiplying quantity sold and price
            self.cursor.execute(
                f"SELECT price FROM products WHERE product_id = {product_id}")
            price = quantity * self.cursor.fetchone()[0]

            # Insert the sale into the sales table
            self.cursor.execute("USE RetailDB")
            self.cursor.execute(
                f"INSERT INTO sales (sale_date, customer_id, product_id, quantity_sold, total_amount) VALUES ('{date}', {customer_id}, {product_id}, {quantity}, {price})")

            # Update the quantity in products
            self.cursor.execute(
                f"UPDATE products SET quantity_in_stock = quantity_in_stock - {quantity} WHERE product_id = {product_id}")

            self.db.commit()

            print("Sale complete")
            time.sleep(2)
