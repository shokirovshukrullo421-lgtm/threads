from admin_function.show_all_cars import show_all_cars
from admin_function.addd_cars import add_new_car
from admin_function.Deactivate_car import deactivate_car
from admin_function.create_order import create_order
from menu.menus import admin_menu
from admin_function.finished_order import finish_order
from admin_function.show_all_users import show_all_users
from admin_function.show_all_orders import show_all_orders
from admin_function.shiw_active_orders import show_active_orders
async def admin_panel():
    while True:
        print(admin_menu)
        choice = input("Tanlang: ")
        if choice == "1":
            await show_all_cars()
        elif choice == "2":
            await add_new_car()
        elif choice == "3":
            await deactivate_car()
        elif choice == "4":
            await create_order()
        elif choice == "5":
            await show_active_orders()
        elif choice == "6":
            await show_all_orders()
            
        elif choice == "7":
            await finish_order()
        elif choice == "8":
            await show_all_users()
        elif choice == "9":
            break
        else:
            print("Notogri tanlov")