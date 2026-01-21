from db_ulash import get_connection
async def show_active_orders():
    try:
        conn = await get_connection()
    except Exception:
        print(" Database ga ulanib bolmadi")
        return
    try:
        query = """
            SELECT
                r.id,
                u.username,
                c.brand,
                c.model,
                r.start_date,
                r.end_date,
                r.total_price
            FROM rentals r
            JOIN users u ON u.id = r.user_id
            JOIN cars c ON c.id = r.car_id
            WHERE r.status = 'active'
            ORDER BY r.start_date
        """

        orders = await conn.fetch(query)

        if not orders:
            print("Hozircha active orderlar yoq")
            return
        for o in orders:
            print(
                f"Order ID: {o['id']} | "
                f"User: {o['username']} | "
                f"Car: {o['brand']} {o['model']} | "
                f"From: {o['start_date']} → {o['end_date']} | "
                f"Total: {o['total_price']}$"
            )

    except Exception as e:
        print(" Orderlarni chiqarishda xatolik:", e)

    finally:
        try:
            await conn.close()
        except Exception:
            pass
