from db_ulash import get_connection
async def show_all_users():
    try:
        conn = await get_connection()
    except Exception:
        print(" Database ga ulanib bolmadi")
        return
    try:
        query = """
            SELECT id, username, role, created_at
            FROM users
            ORDER BY id
        """
        users = await conn.fetch(query)

        if not users:
            print(" Foydalanuvchilar topilmadi")
            return
        for u in users:
            print(
                f"ID: {u['id']} | "
                f"Username: {u['username']} | "
                f"Role: {u['role']} | "
                f"Created: {u['created_at']}"
            )
    except Exception as e:
        print(" Userlarni chiqarishda xatolik:", e)
    finally:
        try:
            await conn.close()
        except Exception:
            pass
