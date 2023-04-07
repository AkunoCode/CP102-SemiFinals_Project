from EduMart import Store
import time
import os

os.system('cls')
# Create a Store object
store = Store()

os.system('cls')
# Login as an admin or customer
while True:
    user_type = input('Login as an admin or customer? or "exit": ').lower()
    os.system('cls')

    if user_type == "admin":
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

    elif user_type == "customer":
        customer = customer_login = store.customer_login()
        if customer_login == True:
            os.system('cls')
            while True:
                print('Customer Actions:')
                # Add To Cart, Remove From Cart, Pay, Edit Cart, Edit Profile, Logout
                print("[1] Add To Cart")
                print("[2] Remove From Cart")
                print("[3] Edit Cart")
                print("[4] Pay")
                print("[5] Logout")

                customer_action = int(input("\nEnter an action: "))
                os.system('cls')

                if customer_action == 1:
                    store.add_to_cart()
                    os.system('cls')
                elif customer_action == 2:
                    store.remove_from_cart()
                    os.system('cls')
                elif customer_action == 3:
                    store.edit_cart()
                    os.system('cls')
                elif customer_action == 4:
                    store.customer_buy()
                    os.system('cls')
                elif customer_action == 5:
                    os.system('cls')
                    break

    elif user_type == "exit":
        print("Exiting...")
        time.sleep(2)
        os.system('cls')
        break
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        os.system('cls')
