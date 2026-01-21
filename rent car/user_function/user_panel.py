from user_function.show_active_cars import show_active_cars
from user_function.my_orders import show_my_orders
from menu.menus import user_menu    
async def user_panel(current_user: dict):
    while True:
        print(user_menu)
        choice = input("Tanlang: ")
        if choice == "1":
            await show_active_cars()
        elif choice == "2":
            await show_my_orders(current_user)
        elif choice == "3":
            print(" Orqaga qaytildi")
            break

        else:
            print("Notogri tanlov, qayta urinib koring")
