import asyncpg
from db_ulash import get_connection

async def login():
    username = input("Username: ")
    password = input("Password: ")

    try:
        conn = await get_connection() 

        user = await conn.fetchrow(
            "SELECT id, username, role, password FROM users WHERE username=$1",
            username
        )
        if not user:
            print(" Bunday user yoq!")
            return None
        if password != user["password"]:
            print(" Parol notori!")
            return None
        print(f"{user['username']} login qilindi")
        return {"id": user["id"], "username": user["username"], "role": user["role"]}
    finally:
        if 'conn' in locals():
            await conn.close()
