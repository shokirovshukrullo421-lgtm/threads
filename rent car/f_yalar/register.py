import asyncpg
from db_ulash import get_connection
async def register():
    print("\n--- REGISTER ---")
    username = input("Username: ")
    password = input("Password: ")
    try:
        conn = await get_connection()
        existing = await conn.fetchrow(
            "SELECT id FROM users WHERE username = $1",
            username
        )
        if existing:
            print(" Bunday username allaqachon mavjud!")
            return
        await conn.execute(
            "INSERT INTO users (username, password, role) VALUES ($1, $2, 'user')",
            username,
            password
        )
        print("Muvaffaqiyatli royxatdan otildi!")
    except asyncpg.PostgresError as e:
        print(" Database xatosi:", e)
    except Exception as e:
        print(" Kutilmagan xato:", e)
    finally:
        if 'conn' in locals():
            await conn.close()
