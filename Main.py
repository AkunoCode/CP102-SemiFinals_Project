from EduMart import Store
import time
import os

os.system('cls')
# Create a Store object
store = Store()

# Login as an admin or customer
while True:
    os.system('cls')
    print('Welcome to EduMart!')
    print('\nPlease login to continue.')
    print('\nLogin as: ')
    print('[1] Admin')
    print('[2] Customer')
    print('[3] Exit')
    user_type = input('\nChoose an action: ')
    os.system('cls')

    if user_type == "1":
        admin = admin_login = store.admin_login()
        if admin_login == True:
            os.system('cls')
            while True:
                print('Admin Actions:')
                # View Products, View Sales, View Customers, View Admins, Add Product, Add Admin,
                # Remove Product, Update Product, Restock Product
                print("[1] View Products")
                print("[2] View Sales")
                print("[3] View Customers")
                print("[4] View Admins")
                print("[5] Add Product")
                print("[6] Add Admin")
                print("[7] Remove Product")
                print("[8] Update Product")
                print("[9] Restock Product")
                print("[10] Logout")

                admin_action = int(input("\nEnter an action: "))
                os.system('cls')

                if admin_action == 1:
                    store.view_products()
                    os.system('cls')
                elif admin_action == 2:
                    store.view_sales()
                    os.system('cls')
                elif admin_action == 3:
                    store.view_customers()
                    os.system('cls')
                elif admin_action == 4:
                    store.view_admins()
                    os.system('cls')
                elif admin_action == 5:
                    store.add_product()
                    os.system('cls')
                elif admin_action == 6:
                    store.add_admin()
                    os.system('cls')
                elif admin_action == 7:
                    store.remove_product()
                    os.system('cls')
                elif admin_action == 8:
                    store.update_product()
                    os.system('cls')
                elif admin_action == 9:
                    store.restock_product()
                    os.system('cls')
                elif admin_action == 10:
                    os.system('cls')
                    break

    elif user_type == "2":
        while True:
            os.system('cls')
            type = input("Are you registered? (Y/N): ").lower()
            if type == "y":
                customer_login = store.customer_login()
                break
            elif type == "n":
                store.customer_register()
            else:
                print("Invalid input. Please try again.")
                time.sleep(2)
                os.system('cls')
        if customer_login == True:
            os.system('cls')
            while True:
                print('Customer Actions:')
                # Add To Cart, Remove From Cart, Pay, Edit Cart, Edit Profile, Logout
                print("[1] Buy Product")
                print("[2] Edit Account")
                print("[3] Logout")

                customer_action = int(input("\nEnter an action: "))
                os.system('cls')

            
                if customer_action == 1:
                    store.customer_buy()
                    os.system('cls')
                elif customer_action == 2:
                    store.customer_edit()
                    os.system('cls')
                elif customer_action == 3:
                    os.system('cls')
                    break

    elif user_type == "3":
        print("Exiting...")
        time.sleep(2)
        os.system('cls')
        break
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        os.system('cls')
