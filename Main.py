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
        # View Inventory, Restock Inventory, View Sales, View Customers, View Admins, Add Product, Delete Product , Update Product, Exit
        print("[1] View Inventory")
        print("[2] Restock Inventory")
        print("[3] View Sales")
        print("[4] View Customers")
        print("[5] View Admins")
        print("[6] Add Product")
        print("[7] Delete Product")
        print("[8] Update Product")
        print("[9] Exit")
        admin_action = input('What would you like to do? ').lower()

        os.system('cls')
        if admin_action == '1':
            store.admin_view_inventory()
        elif admin_action == '2':
            store.admin_restock()
        elif admin_action == '3':
            store.admin_view_sales()
        elif admin_action == '4':
            store.admin_view_customers()
        elif admin_action == '5':
            store.admin_view_admins()
        elif admin_action == '6':
            store.admin_add_product()
        elif admin_action == '7':
            store.admin_delete_product()
        elif admin_action == '8':
            store.admin_update_product()
        elif admin_action == '9':
            print('Exiting...')
            time.sleep(2)
            exit()
        os.system('cls')

elif log_in == 'customer':
    while True:
        print('Customer Actions:')
        # Buy an item, edit info, exit
        print("[1] Buy an Item")
        print("[2] Edit Info")
        print("[3] Exit")
        customer_action = input('What would you like to do? ').lower()

        os.system('cls')
        if customer_action == '1':
            store.customer_buy()
        elif customer_action == '2':
            store.customer_edit_info()
        elif customer_action == '3':
            print('Exiting...')
            time.sleep(2)
            exit()
        os.system('cls')
