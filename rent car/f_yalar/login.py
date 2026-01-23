import asyncpg
from db_ulash import get_connection
from log.logger import logger

async def login():
    username = input("Username: ")
    password = input("Password: ")
    conn = None
    try:
        conn = await get_connection()
        logger.info(f"Login urinish | username={username}")

        user = await conn.fetchrow(
            "SELECT id, username, role, password FROM users WHERE username=$1",
            username
        )
        if not user:
            logger.warning(f"Login muvaffaqiyatsiz | username topilmadi: {username}")
            print(" Bunday user yoq")
            return None

        if password != user["password"]:
            logger.warning(f"Login muvaffaqiyatsiz | notogri parol | username={username}")
            print(" Parol notogri!")
            return None

        logger.info(f"Login muvaffaqiyatli | user_id={user['id']} | role={user['role']}")
        print(f" {user['username']} login qilindi")

        return {
            "id": user["id"],
            "username": user["username"],
            "role": user["role"]
        }

    except Exception:
        logger.exception(f"Login jarayonida xatolik | username={username}")
        print(" Login jarayonida xatolik yuz berdi")
        return None

    finally:
        if conn:
            await conn.close()
            logger.info("Database ulanish yopildi (login)")
