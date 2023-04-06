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
if log_in == 'admin':
    print('Admin')
    # store.admin_menu()
elif log_in == 'customer':
    print('Customer')
    # store.customer_menu()
