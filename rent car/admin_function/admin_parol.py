import asyncio
from menu.menus import admin_menu
from log.logger import logger

logger = logger(__name__)

ADMIN_NOMI = "admin"
ADMIN_PAROL = "admin123"

async def admin():
    logger.info("Admin menyusiga kirildi")

    logger.info("Admin menyusi chiqarildi")
    print("Admin menyusiga xush kelibsiz!")
    print(admin_menu)
