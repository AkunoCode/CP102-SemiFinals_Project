import mysql.connector
import datetime
import time
import os


class Store:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Johnleo1152003.'
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
                print("Opening EduMart Database...")
                time.sleep(3)
                return 'edumartdb'
        else:
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
                                "description TEXT,"
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

            # Customer's Cart table through a product ID list
            self.cursor.execute("CREATE TABLE cart ("
                                "cart_id INT PRIMARY KEY AUTO_INCREMENT,"
                                "customer_id INT,"
                                "product_id INT,"
                                "quantity INT,"
                                "price DECIMAL(10, 2),"
                                "FOREIGN KEY (customer_id) REFERENCES customers (customer_id),"
                                "FOREIGN KEY (product_id) REFERENCES products (product_id));")

            # Payment Method table
            self.cursor.execute("CREATE TABLE payment_method ("
                                "payment_id INT PRIMARY KEY AUTO_INCREMENT,"
                                "payment_method VARCHAR(255) NOT NULL,"
                                "customer_id INT,"
                                "FOREIGN KEY (customer_id) REFERENCES customers (customer_id));")

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

            input("Press Enter to continue...\n")

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
                input("Press Enter to continue...\n")
                os.system('cls')
                return True
            else:
                print("Invalid Admin ID or Password. Please try again.\n")
                input("Press Enter to continue...\n")
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
            return False

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

        input("Press Enter to continue...\n")

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
                f"{product[0]}\t\t{product[1]}{space}{product[3]}\t\t{product[4]}")

        input("Press Enter to continue...\n")

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

        input("Press Enter to continue...\n")

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

        input("Press Enter to continue...\n")

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

        input("Press Enter to continue...\n")

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

        input("Press Enter to continue...\n")

    def add_admin(self):
        """This function will ask for the admin details./n
        It will then insert the admin's details into the database"""

        # Asking for input for admin details
        name = input("Enter the admin name: ")
        contact_number = input("Enter the admin contact number: ")
        email = input("Enter the admin email address: ")
        passwd = input("Enter the admin password: ")

        # Inserting the admin details into the database
        self.cursor.execute(
            f"INSERT INTO admins (name, contact_number, email, passwd) VALUES ('{name}', '{contact_number}', '{email}', '{passwd}')")

        # Committing the changes
        self.db.commit()

        print("Admin added successfully!")

        input("Press Enter to continue...\n")

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

        input("Press Enter to continue...\n")

    def update_product(self):
        """This function will ask for the product ID./n
        It will then update the product's details in the database"""

        # Show the products in the database
        self.view_products()

        # Asking for input for product ID
        product_id = input("Enter the product ID: ")

        # Asking for input for product details
        name = input("Enter the product name: ")
        price = input("Enter the product price: ")
        quantity_in_stock = input("Enter the quantity in stock: ")

        # Updating the product details in the database
        self.cursor.execute(
            f"UPDATE products SET name = '{name}', price = {price}, quantity_in_stock = {quantity_in_stock} WHERE product_id = {product_id}")

        # Committing the changes
        self.db.commit()

        print("Product updated successfully!")

        input("Press Enter to continue...\n")

    def restock_product(self):
        """This function will reset the quantity in stock of all products to 20"""

        # Updating the quantity in stock of all products to 20
        self.cursor.execute("UPDATE products SET quantity_in_stock = 20")

        # Committing the changes
        self.db.commit()

        print("All products have been restocked successfully!")

        input("Press Enter to continue...\n")

    def add_to_cart(self):
        """This function will ask for the product ID and quantity and add it into the cart table./n
        It will automatically calculate the total price of the product and add it to the cart table"""
        # Show the products in the database
        self.view_products()

        # Asking for input for product ID
        product_id = input("Enter the product ID: ")

        # Asking for input for quantity and checking if there is enough stock
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

        # Inserting the product details into the database
        self.cursor.execute(
            f"INSERT INTO cart (customer_id, product_id, quantity, price) VALUES ({self.customer_id}, {product_id}, {quantity}, {quantity} * (SELECT price FROM products WHERE product_id = {product_id}))")

        # Committing the changes
        self.db.commit()

        print("Product added to cart successfully!")

        # Updating the quantity in stock of the product
        self.cursor.execute(
            f"UPDATE products SET quantity_in_stock = quantity_in_stock - {quantity} WHERE product_id = {product_id}")

        input("Press Enter to continue...\n")

    def edit_cart(self):
        """This function will ask for the product ID and quantity and update the cart table./n
        It will automatically calculate the total price of the product and update it in the cart table./n
        It will also update the quantity in stock of the product"""

        # printing the cart by joining the products and cart tables
        self.cursor.execute(
            f"SELECT cart.product_id, products.name, cart.quantity, cart.price FROM cart INNER JOIN products ON cart.product_id = products.product_id WHERE customer_id = {self.customer_id}")
        cart = self.cursor.fetchall()

        # Printing the cart
        print("Product ID\tProduct Name\t\t\tQuantity\tPrice")
        for product in cart:
            # Checking if the product name is longer than 8 characters
            if len(product[1]) > 8:
                print(
                    f"{product[0]}\t\t{product[1]}\t{product[2]}\t\t{product[3]}")
            else:
                print(
                    f"{product[0]}\t\t{product[1]}\t\t{product[2]}\t\t{product[3]}")

        # Asking for input for product ID
        product_id = input("Enter the product ID: ")

        # Asking for input for quantity to update the qunatity in cart and add back to stock
        while True:
            quantity = input("Enter the quantity: ")

            # If input quantity is bigger than the quantity in cart this will remove the product from the cart and add back to stock
            # else it will update the quantity in cart and add back to stock
            if int(quantity) >= product[3]:
                self.cursor.execute(
                    f"DELETE FROM cart WHERE customer_id = {self.customer_id} AND product_id = {product_id}")
                print("Product removed from cart successfully!")

                # Updating the quantity in stock of the product
                self.cursor.execute(
                    f"UPDATE products SET quantity_in_stock = quantity_in_stock + {product[3]} WHERE product_id = {product_id}")
                break
            elif int(quantity) <= product[3]:
                self.cursor.execute(
                    f"UPDATE cart SET quantity = {quantity}, price = {quantity} * (SELECT price FROM products WHERE product_id = {product_id}) WHERE customer_id = {self.customer_id} AND product_id = {product_id}")
                print("Product quantity updated successfully!")

                # Updating the quantity in stock of the product
                self.cursor.execute(
                    f"UPDATE products SET quantity_in_stock = quantity_in_stock + {quantity}")
                break

    def customer_buy(self):
        """This function will ask for the customer's payment method./n
        It will then calculate the total price of the cart and display it to the customer./n
        It will then ask for the customer's confirmation to proceed with the purchase./n
        It will then update the quantity in stock of the products in the cart and delete the cart
        Then add to the sales table by looping through the cart table"""

        # Printing the cart and calculating the total price
        self.cursor.execute(
            f"SELECT * FROM cart WHERE customer_id = {self.customer_id}")
        cart = self.cursor.fetchall()

        total_price = 0

        print("Cart: ")
        print("Product ID\tProduct Name\tQuantity\tPrice")
        for product in cart:
            # Ensuring even spacing
            if len(product[2]) < 8:
                space = "\t\t"
            else:
                space = "\t"

            print(
                f"{product[2]}{space}{product[3]}\t\t{product[4]}\t\t{product[5]}")

            total_price += product[5]

        print(f"\nTotal Price: {total_price}")

        # Asking for input for confirmation
        while True:
            confirm = input("\nProceed with purchase? [Y/N]: ").upper()

            if confirm == "Y":
                break
            elif confirm == "N":
                return
            else:
                print("\nInvalid input!")
                time.sleep(2)

        # Asking for input for payment method
        os.system("cls")
        while True:
            print("Payment Methods: ")
            print("[1] Cash")
            print("[2] Credit Card")
            print("[3] Debit Card")
            print("[4] GCash")
            method = input("\nEnter the payment method: ")

            if method == "1":
                payment_method = "Cash"
                break
            elif method == "2":
                payment_method = "Credit Card"
                break
            elif method == "3":
                payment_method = "Debit Card"
                break
            elif method == "4":
                payment_method = "GCash"
                break
            else:
                print("Invalid payment method!")
                time.sleep(2)

        # Confirming payment
        os.system("cls")
        print(f"Payment Method: {payment_method}")
        while True:
            confirm = input("Confirm payment? [Y/N]: ").upper()

            if confirm == "Y":
                break
            elif confirm == "N":
                return
            else:
                print("Invalid input!")
                time.sleep(2)

        # Adding into the sales table
        for product in cart:
            self.cursor.execute(
                f"INSERT INTO sales (customer_id, product_id, quantity, price, payment_method) VALUES ({self.customer_id}, {product[2]}, {product[4]}, {product[5]}, '{payment_method}')")

        print("\nPurchase successful!")

        input("Press Enter to continue...")
