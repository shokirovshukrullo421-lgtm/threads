import asyncpg
from db_ulash import get_connection
from log.logger import logger

async def register():
    print("\n--- REGISTER ---")
    username = input("Username: ")
    password = input("Password: ")

    conn = None
    try:
        conn = await get_connection()
        logger.info(f"Register urinish | username={username}")

        existing = await conn.fetchrow(
            "SELECT id FROM users WHERE username = $1",
            username
        )

        if existing:
            logger.warning(f"Register rad etildi | username band: {username}")
            print(" Bunday username allaqachon mavjud!")
            return

        await conn.execute(
            "INSERT INTO users (username, password, role) VALUES ($1, $2, 'user')",
            username,
            password
        )

        logger.info(f"Yangi user royxatdan otdi | username={username}")
        print(" Muvaffaqiyatli royxatdan otildi!")

    except asyncpg.PostgresError:
        logger.exception("Database xatosi (register)")
        print(" Database xatosi yuz berdi")

    except Exception:
        logger.exception(f"Kutilmagan xato (register) | username={username}")
        print(" Kutilmagan xato yuz berdi")

    finally:
        if conn:
            await conn.close()
            logger.info("Database ulanish yopildi (register)")
