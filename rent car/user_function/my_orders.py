from db_ulash import get_connection
import asyncpg
async def show_my_orders(current_user: dict):
    try:
        conn = await get_connection()
        query = """
        SELECT 
            o.id AS order_id,
            c.brand,
            c.model,
            o.start_date,
            o.end_date,
            o.status
        FROM orders o
        JOIN cars c ON c.id = o.car_id
        WHERE o.user_id = $1
        ORDER BY o.id
        """
        orders = await conn.fetch(query, current_user["id"])

        if not orders:
            print("\nSizda hozircha orderlar yoq.\n")
            return

        print("\n Mening orderlarim:")
        print("-" * 60)

        for o in orders:
            print(
                f"Order ID: {o['order_id']} | "
                f"Car: {o['brand']} {o['model']} | "
                f"{o['start_date']} → {o['end_date']} | "
                f"Status: {o['status']}"
            )

        print("-" * 60)

    except asyncpg.PostgresError as e:
        print(" Database xatosi:", e)

    except KeyError:
        print(" User aniqlanmadi (login qilinmagan).")

    except Exception as e:
        print(" Kutilmagan xato:", e)

    finally:
        if 'conn' in locals():
            await conn.close()
