import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Johnleo1152003.'
)

cursor = db.cursor()


def database_creation():

    # Check if database exists
    cursor.execute("SHOW DATABASES")
    database = cursor.fetchall()
    db_exist = False

    for db in database:
        if 'retailDB' in db:
            db_exist = True
            break

    # Create database if it does not exist
    if not db_exist:
        cursor.execute("CREATE DATABASE RetailDB")
        create_tables()
        print("RetailDB Database created")
    else:
        print("RetailDB Database already exists")


def create_tables():

    # Use RetailDB database
    cursor.execute("USE RetailDB")

    # Execute CREATE TABLE statements
    cursor.execute("CREATE TABLE products ("
                   "product_id INT PRIMARY KEY AUTO_INCREMENT,"
                   "name VARCHAR(255) NOT NULL,"
                   "description TEXT,"
                   "price DECIMAL(10, 2) NOT NULL,"
                   "quantity_in_stock INT NOT NULL);")

    cursor.execute("CREATE TABLE customers ("
                   "customer_id INT PRIMARY KEY AUTO_INCREMENT,"
                   "name VARCHAR(255) NOT NULL,"
                   "contact_number VARCHAR(15) NOT NULL,"
                   "email VARCHAR(255),"
                   "address TEXT NOT NULL);")

    cursor.execute("CREATE TABLE sales ("
                   "sale_id INT PRIMARY KEY AUTO_INCREMENT,"
                   "sale_date TIMESTAMP NOT NULL,"
                   "customer_id INT,"
                   "product_id INT,"
                   "quantity_sold INT,"
                   "total_amount DECIMAL(10, 2),"
                   "FOREIGN KEY (customer_id) REFERENCES customers (customer_id),"
                   "FOREIGN KEY (product_id) REFERENCES products (product_id));")

    cursor.execute("CREATE TABLE admins ("
                   "admin_id INT PRIMARY KEY AUTO_INCREMENT,"
                   "lastname VARCHAR(255) NOT NULL,"
                   "firstname VARCHAR(255) NOT NULL,"
                   "passwd VARCHAR(255));")

    cursor.execute("CREATE TABLE inventory ("
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
        cursor.execute(
            "INSERT INTO products (name, description, price, quantity_in_stock) VALUES (%s, %s, %s, %s)", product)

    # Commit changes and close cursor and connection
    db.commit()
