import asyncio
from menu.menus import auth_menu, admin_menu, user_menu
from f_yalar.login import login
from f_yalar.register import register
from admin_function import admin_panel
from user_function.user_panel import user_panel
async def main():
    while True:
        print(auth_menu)
        choice = input("Tanlang: ")
        if choice == "1":
            await register()  
        elif choice == "2":
            user = await login()  
            if user:
                if user['role'] == 'admin':
                    print("\nAdmin menyusi")
                    print(admin_menu)
                    await admin_panel()  
                else:
                    print("\nFoydalanuvchi menyusiga xush kelibsiz!")
                    print(user_menu)
                    await user_panel(user)  
        elif choice == "3":
            print("\nDastur tugatildi")
            break
        else:
            print(" Notogri tanlov, qayta urinib koring\n")

if __name__ == "__main__":
    asyncio.run(main())
