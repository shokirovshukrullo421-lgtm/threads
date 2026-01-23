import asyncio
from menu.menus import auth_menu, admin_menu, user_menu
from f_yalar.login import login
from f_yalar.register import register
from admin_function.adminpanel import admin_panel
from user_function.user_panel import user_panel
from log.logger import logger
async def main():
    logger.info("Dastur ishga tushdi")
    while True:
        print(auth_menu)
        choice = input("Tanlang: ")
        if choice == "1":
            logger.info("Register menyusi tanlandi")
            await register()
        elif choice == "2":
            logger.info("Login menyusi tanlandi")
            user = await login()
            if user:
                if user['role'] == 'admin':
                    logger.info(f"Admin panelga kirdi | user_id={user['id']}")
                    print("\nAdmin menyusi")
                    print(admin_menu)
                    await admin_panel()
                else:
                    logger.info(f"User panelga kirdi | user_id={user['id']}")
                    print("\nFoydalanuvchi menyusiga xush kelibsiz!")
                    print(user_menu)
                    await user_panel(user)
        elif choice == "3":
            logger.info("Dastur yopildi")
            print("\nDastur tugatildi")
            break
        else:
            logger.warning(f"Notogri tanlov | choice={choice}")
            print("Notogri tanlov, qayta urinib koring\n")

if __name__ == "__main__":
    asyncio.run(main())
