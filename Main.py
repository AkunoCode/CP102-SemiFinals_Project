from RetailClass import Retail
import time
import os

# Create an instance of the RetailItem class.
os.system('cls')
store = Retail()

store.database_creation()
os.system('cls')
print("Loading...")
time.sleep(3)

os.system('cls')
log_in = store.log_in()
os.system('cls')
if log_in == 'admin':
    while True:
        print('Admin Actions:')
        # View Inventory, Restock Inventory, View Sales, View Customers, View Admins
        print("[1] View Inventory")
        print("[2] Restock Inventory")
        print("[3] View Sales")
        print("[4] View Customers")
        print("[5] View Admins")
        print("[6] Exit")
        admin_action = input('What would you like to do? ').lower()

        os.system('cls')
        if admin_action == '1':
            store.admin_view_inventory()
        elif admin_action == '2':
            store.admin_restock_inventory()
        elif admin_action == '3':
            store.admin_view_sales()
        elif admin_action == '4':
            store.admin_view_customers()
        elif admin_action == '5':
            store.admin_view_admins()
        elif admin_action == '6':
            print('Exiting...')
            time.sleep(2)
            exit()
        os.system('cls')

elif log_in == 'customer':
    print('Customer')
    # store.customer_menu()
