import mysql.connector
import time
import os


class Store:
    def __init__(self, dbuser='root', dbpass='Johnleo1152003.'):
        self.db = mysql.connector.connect(
            host='localhost',
            user=dbuser,
            passwd=dbpass
        )
        # Create a cursor
        self.cursor = self.db.cursor()

        # Set the database
        self.cursor.execute(f"USE {self.database()}")

    def database(self):
        """This function will check if the database exists./n
        If it does, it will return the name of the database./n
        If it doesn't, it will create the database and return the name of the database"""

        # Get the list of databases
        self.cursor.execute("SHOW DATABASES")
        database = self.cursor.fetchall()

        # Check if the database exists
        for db in database:
            if 'edumartdb' in db:
                # Set the database
                self.cursor.execute("USE edumartdb")
                # Get the list of tables in the database
                self.cursor.execute("SHOW TABLES")
                tables = self.cursor.fetchall()

                # Check if all the necessary tables exist
                if len(tables) == 5:
                    os.system('cls')
                    print("Opening EduMart Database...")
                    time.sleep(3)
                    return 'edumartdb'
                else:
                    os.system('cls')
                    # Drop the database
                    print("EduMart Database is corrupted. Rebuilding EduMart Database...")
                    time.sleep(3)

                    self.cursor.execute("DROP DATABASE edumartdb")
        else:
            os.system('cls')
            # Create the database
            print("EduMart Database not found. Creating EduMart Database...")
            time.sleep(3)

            self.cursor.execute("CREATE DATABASE edumartdb")

            # Set the database
            self.cursor.execute("USE edumartdb")

            # Create the tables
            os.system('cls')
            print("Creating Tables...")
            time.sleep(3)

            # Products table
            self.cursor.execute("CREATE TABLE products ("
                                "product_id INT PRIMARY KEY AUTO_INCREMENT,"
                                "name VARCHAR(255) NOT NULL,"
                                "price DECIMAL(10, 2) NOT NULL,"
                                "quantity_in_stock INT NOT NULL);")

            # Customers table
            self.cursor.execute("CREATE TABLE customers ("
                                "customer_id INT PRIMARY KEY AUTO_INCREMENT,"
                                "name VARCHAR(255) NOT NULL,"
                                "contact_number VARCHAR(15) NOT NULL,"
                                "email VARCHAR(255),"
                                "passwd VARCHAR(255) NOT NULL,"
                                "address TEXT NOT NULL);")

            # Payment Method table
            self.cursor.execute("CREATE TABLE payment_method ("
                                "payment_id INT PRIMARY KEY AUTO_INCREMENT,"
                                "payment_method VARCHAR(255) NOT NULL);")

            # Sales table
            self.cursor.execute("CREATE TABLE sales ("
                                "sale_id INT PRIMARY KEY AUTO_INCREMENT,"
                                "sale_date TIMESTAMP NOT NULL,"
                                "customer_id INT,"
                                "product_id INT,"
                                "quantity_sold INT,"
                                "total_amount DECIMAL(10, 2),"
                                "payment_method INT,"
                                "FOREIGN KEY (customer_id) REFERENCES customers (customer_id),"
                                "FOREIGN KEY (product_id) REFERENCES products (product_id),"
                                "FOREIGN KEY (payment_method) REFERENCES payment_method (payment_ID));")

            # Admins table
            self.cursor.execute("CREATE TABLE admins ("
                                "admin_id INT PRIMARY KEY AUTO_INCREMENT,"
                                "lastname VARCHAR(255) NOT NULL,"
                                "firstname VARCHAR(255) NOT NULL,"
                                "passwd VARCHAR(255));")

            # Insert data into the tables
            os.system('cls')
            print("Inserting Data...")
            time.sleep(3)

            products = [("Ballpen", 10.00, 20),
                        ("Pencil", 8.00, 20),
                        ("Eraser", 5.00, 20),
                        ("Highlighter", 50.00, 20),
                        ("Marker", 75.00, 20),
                        ("Notebook", 20.00, 20),
                        ("Ruler", 15.00, 20),
                        ("Scissors", 10.00, 20),
                        ("Glue Stick", 15.00, 20),
                        ("Calculator", 200.00, 20)]

            for product in products:
                self.cursor.execute(
                    "INSERT INTO products (name, price, quantity_in_stock) VALUES (%s, %s, %s)", product)

            # Inserting payment methods
            payment_methods = [("Cash"), ("Credit Card"),
                               ("Debit Card"), ("GCash")]

            for payment_method in payment_methods:
                self.cursor.execute(
                    "INSERT INTO payment_method (payment_method) VALUES (%s)", (payment_method,))

            # Creating the admin account
            os.system('cls')
            print("Creating Admin Account...\n")
            time.sleep(3)

            # Asking for input for admin data
            lastname = input("Enter your last name: ")
            firstname = input("Enter your first name: ")
            passwd = input("Enter your password: ")

            # Inserting the admin data into the database
            self.cursor.execute(
                "INSERT INTO admins (lastname, firstname, passwd) VALUES (%s, %s, %s)", (lastname, firstname, passwd))

            # Committing the changes
            self.db.commit()

            os.system('cls')
            print("Admin account created successfully!\n")

            print("Your login credentials are as follows:\n")
            print("Admin ID: 1")
            print("Password: " + passwd + "\n")

            input("\nPress Enter to continue...\n")

            return 'edumartdb'

    def admin_login(self):
        """This function will ask for the admin ID and password./n
        If the ID and password are correct, it will return True./n
        If the ID and password are incorrect, it will return False"""

        # Asking for input for admin ID and password
        os.system('cls')
        while True:
            admin_id = input("Enter your Admin ID: ")
            passwd = input("Enter your password: ")

            # Checking if the admin ID and password are correct
            self.cursor.execute(
                f"SELECT * FROM admins WHERE admin_id = {admin_id} AND passwd = '{passwd}'")
            admin = self.cursor.fetchall()

            if admin:
                print("Login successful!\n")
                input("\nPress Enter to continue...\n")
                os.system('cls')
                return True
            else:
                print("Invalid Admin ID or Password. Please try again.\n")
                input("\nPress Enter to continue...\n")
                os.system('cls')

    def customer_login(self):
        """This function will ask for the customer ID and password./n
        If the ID and password are correct, it will return True./n
        If the ID and password are incorrect, it will return False"""

        # Asking for input for customer ID and password
        customer_id = input("Enter your Customer ID: ")
        passwd = input("Enter your password: ")

        # Checking if the customer ID and password are correct
        self.cursor.execute(
            f"SELECT * FROM customers WHERE customer_id = {customer_id} AND passwd = '{passwd}'")
        customer = self.cursor.fetchall()

        if customer:
            self.customer_id = customer_id
            return True
        else:
            print("Invalid Admin ID or Password. Please try again.\n")
            input("\nPress Enter to continue...\n")
            os.system('cls')

    def customer_register(self):
        """This function will ask for the customer's details./n
        It will then insert the customer's details into the database"""

        # Asking for input for customer details
        name = input("Enter your name: ")
        contact_number = input("Enter your contact number: ")
        email = input("Enter your email address: ")
        passwd = input("Enter your password: ")
        address = input("Enter your address: ")

        # Inserting the customer details into the database
        self.cursor.execute(
            f"INSERT INTO customers (name, contact_number, email, passwd, address) VALUES ('{name}', '{contact_number}', '{email}', '{passwd}', '{address}')")

        # Committing the changes
        self.db.commit()

        # Declaring the customer ID by finding matching email and password
        self.cursor.execute(
            f"SELECT customer_id FROM customers WHERE email = '{email}' AND passwd = '{passwd}'")
        customer_id = self.cursor.fetchall()

        self.customer_id = customer_id[0][0]

        print("\nCustomer registered successfully!\n")
        print("Your Customer ID is " + str(self.customer_id) + ".\n")

        input("\nPress Enter to continue...\n")

        return True

    def view_products(self):
        """This function will display all the products in the database"""

        # Displaying all the products in the database
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()

        print("Product ID\tName\t\t\t\tPrice\t\tQuantity in Stock")

        for product in products:
            # To ensure even spacing between the columns
            if len(product[1]) >= 8:
                space = "\t\t\t"
            else:
                space = "\t\t\t\t"

            print(
                f"{product[0]}\t\t{product[1]}{space}{product[2]}\t\t{product[3]}")

        input("\nPress Enter to continue...\n")

    def view_sales(self):
        """This function will display all the sales in the database"""

        # Displaying all the sales in the database
        self.cursor.execute("SELECT * FROM sales")
        sales = self.cursor.fetchall()

        print(
            "Sale ID\t\tSale Date\t\tCustomer ID\tProduct ID\tQuantity Sold\tTotal Amount")

        for sale in sales:
            print(
                f"{sale[0]}\t\t{sale[1]}\t{sale[2]}\t\t{sale[3]}\t\t{sale[4]}\t\t{sale[5]}")

        input("\nPress Enter to continue...\n")

    def view_customers(self):
        """This function will display all the customers in the database"""

        # Displaying all the customers in the database
        self.cursor.execute("SELECT * FROM customers")
        customers = self.cursor.fetchall()

        print("Customer ID\tName\t\t\t\tContact Number\t\tEmail")

        for customer in customers:
            # To ensure even spacing between the columns
            if len(customer[1]) >= 8:
                space = "\t\t\t"
            else:
                space = "\t\t\t\t"

            print(
                f"{customer[0]}\t\t{customer[1]}{space}{customer[2]}\t\t{customer[3]}")

        input("\nPress Enter to continue...\n")

    def view_admins(self):
        """This function will display all the admins in the database"""

        # Displaying all the admins in the database
        self.cursor.execute("SELECT * FROM admins")
        admins = self.cursor.fetchall()

        print("Admin ID\tName\t\t\t\tContact Number\t\tEmail")

        for admin in admins:
            # To ensure even spacing between the columns
            if len(admin[1]) >= 8:
                space = "\t\t\t"
            else:
                space = "\t\t\t\t"

            print(
                f"{admin[0]}\t\t{admin[1]}{space}{admin[2]}\t\t{admin[3]}")

        input("\nPress Enter to continue...\n")

    def add_product(self):
        """This function will ask for the product details./n
        It will then insert the product's details into the database"""

        self.view_products()

        # Asking for input for product details
        name = input("Enter the product name: ")
        price = input("Enter the product price: ")
        quantity_in_stock = input("Enter the quantity in stock: ")

        # Inserting the product details into the database
        self.cursor.execute(
            f"INSERT INTO products (name, price, quantity_in_stock) VALUES ('{name}', {price}, {quantity_in_stock})")

        # Committing the changes
        self.db.commit()

        print("Product added successfully!")

        input("\nPress Enter to continue...\n")

    def add_admin(self):
        """This function will ask for the admin details./n
        It will then insert the admin's details into the database"""

        # Asking for input for admin details
        fname = input("Enter the admin first name: ")
        lname = input("Enter the admin last name: ")
        passwd = input("Enter the admin password: ")

        # Inserting the admin details into the database
        self.cursor.execute(
            f"INSERT INTO admins (firstname, lastname, passwd) VALUES ('{fname}', '{lname}', '{passwd}')")

        # Committing the changes
        self.db.commit()

        print("\nAdmin added successfully!\n")

        # Printing admin ID
        self.cursor.execute(
            f"SELECT admin_id FROM admins WHERE firstname = '{fname}' AND lastname = '{lname}'")
        admin_id = self.cursor.fetchall()

        print("Your Admin ID is " + str(admin_id[0][0]) + ".\n")

        input("\nPress Enter to continue...\n")

    def remove_product(self):
        """This function will ask for the product ID./n
        It will then delete the product from the database"""

        # Show the products in the database
        self.view_products()

        # Asking for input for product ID
        product_id = input("Enter the product ID: ")

        # Deleting the product from the database
        self.cursor.execute(
            f"DELETE FROM products WHERE product_id = {product_id}")

        # Committing the changes
        self.db.commit()

        print("Product removed successfully!")

        input("\nPress Enter to continue...\n")

    def update_product(self):
        """This function will ask for the product ID./n
        It will then update the product's details in the database"""

        # Show the products in the database
        self.view_products()

        # Asking for input for product ID
        product_id = input("Enter the product ID: ")

        print("Leave the field blank if you do not want to update it.\n")

        # Asking for input for product details
        name = input("Enter the product name: ")
        price = input("Enter the product price: ")
        quantity_in_stock = input("Enter the quantity in stock: ")

        query_list = []
        params = []

        # Checking if there is empty input
        if name != "":
            query_list.append("name = %s")
            params.append(name)
        if price != "":
            query_list.append("price = %s")
            params.append(price)
        if quantity_in_stock != "":
            query_list.append("quantity_in_stock = %s")
            params.append(quantity_in_stock)
        
        # Executing
        query = "UPDATE products SET " + ", ".join(query_list) + " WHERE product_id = %s"
        params.append(product_id)
        params = tuple(params)
        self.cursor.execute(query, params)

        # Committing the changes
        self.db.commit()

        print("Product updated successfully!")

        input("\nPress Enter to continue...\n")

    def restock_product(self):
        """This function will reset the quantity in stock of all products to 20"""

        # Updating the quantity in stock of all products to 20
        self.cursor.execute("UPDATE products SET quantity_in_stock = 20")

        # Committing the changes
        self.db.commit()

        print("All products have been restocked successfully!")

        input("\nPress Enter to continue...\n")

    def customer_edit(self):
        """This function will edit the customer's details"""

        print("Leave the field blank if you do not want to change it.\n")
        # Asking for input for customer details
        name = input("Enter new customer name: ")
        contact = input("Enter new customer contact number: ")
        email = input("Enter new customer email: ")
        passwd = input("Enter new customer password: ")
        address = input("Enter new customer address: ")

        query_list = []
        params = []

        # Checking if the fields are empty
        if name != "":
            query_list.append("name = %s")
            params.append(name)
        if contact != "":
            query_list.append("contact_number = %s")
            params.append(contact)
        if email != "":
            query_list.append("email = %s")
            params.append(email)
        if passwd != "":
            query_list.append("passwd = %s")
            params.append(passwd)
        if address != "":
            query_list.append("address = %s")
            params.append(address)
        
        # Updating the customer details in the database
        self.cursor.execute(
            f"UPDATE customers SET {', '.join(query_list)} WHERE customer_id = {self.customer_id}", params)

        # Committing the changes
        self.db.commit()

        print("Customer updated successfully!")

        input("\nPress Enter to continue...\n")

    def customer_buy(self):
        """This function will show the items available and ask for the product ID and quantity./n
        It will automatically calculate the total price of the product and deduct it from the stock./n
        It will also ask for the payment method and confirm the payment"""
        
        # Printing the products
        self.view_products()

        # Asking for input for product ID
        product_id = input("Enter the product ID: ")

        # Asking for input for quantity
        while True:
            quantity = input("Enter the quantity: ")

            # Checking if there is enough stock
            self.cursor.execute(
                f"SELECT quantity_in_stock FROM products WHERE product_id = {product_id}")
            quantity_in_stock = self.cursor.fetchone()[0]

            if int(quantity) > quantity_in_stock:
                print("There is not enough stock!")
            else:
                break

        # Asking for input for payment method
        os.system("cls")
        while True:
            print("Payment Methods: ")
            print("[1] Cash")
            print("[2] Credit Card")
            print("[3] Debit Card")
            print("[4] GCash")
            method = int(input("\nEnter the payment method: "))
            if method not in range(1, 5):
                print("Invalid input!")
            else:
                payment_method = method
                break

        price = self.cursor.execute(f"SELECT price FROM products WHERE product_id = {product_id}")
        price = self.cursor.fetchone()[0]
        total = int(quantity) * price
        
        # Confirming payment
        os.system("cls")
        print(f"Total Price: {total}")
        print(f"Payment Method: {payment_method}")
        while True:
            confirm = input("Confirm payment? [Y/N]: ").upper()

            if confirm == "Y":
                # Adding into the sales table
                self.cursor.execute(
                    f"INSERT INTO sales (sale_date, customer_id, product_id, quantity_sold, total_amount, payment_method) VALUES (CURRENT_TIMESTAMP, {self.customer_id}, {product_id}, {quantity}, {total}, {payment_method})")
                # Deducting in stocks
                self.cursor.execute(
                    f"UPDATE products SET quantity_in_stock = quantity_in_stock - {quantity} WHERE product_id = {product_id}")
                self.db.commit()
                break
            elif confirm == "N":
                self.db.rollback()
                return
            else:
                print("Invalid input!")
                time.sleep(2)


        print("\nPurchase successful!")

        input("\nPress Enter to continue...")

    def custom_search(self):
        """This function can do an advanced search on the products table either by name or price_range"""

        print("Search by: ")
        print("[1] Name")
        print("[2] Price Range")

        search_by = int(input("\nEnter the search method: "))
        while True:
            if search_by == 1:
                name = input("Enter the product name: ")
                condition = f"Products that contain '{name}'"
                self.cursor.execute(
                    f"SELECT * FROM products WHERE name LIKE '%{name}%'")
                products = self.cursor.fetchall()
                break
            elif search_by == 2:
                min_range = input("Enter the minimum price range: ")
                max_range = input("Enter the maximum price range: ")
                condition = f'Products with prices between {min_range} and {max_range}'
                self.cursor.execute(
                    f"SELECT * FROM products WHERE price BETWEEN {min_range} AND {max_range}")
                products = self.cursor.fetchall()
                break
            else:
                print("Invalid input!")
                time.sleep(2)
        if products:
            print("\nProducts found!\n")
            time.sleep(2)
            os.system("cls")
            print(f"Search Condition: {condition}")
            print("\nProduct ID\tName\t\t\t\tPrice\t\tQuantity in Stock")
            for product in products:
                # To ensure even spacing between the columns
                if len(product[1]) >= 8:
                    space = "\t\t\t"
                else:
                    space = "\t\t\t\t"
                print(f"{product[0]}\t\t{product[1]}{space}{product[2]}\t\t{product[3]}")

            input("\nPress Enter to continue...")
        else:
            print(f"Search Condition: {condition}")
            print("No products found!")
            input("\nPress Enter to continue...")

