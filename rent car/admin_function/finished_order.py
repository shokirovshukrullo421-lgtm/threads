from db_ulash import get_connection
async def finish_order():
    order_id = input("Order ID ni kiriting: ")
    try:
        conn = await get_connection()
    except Exception:
        print(" Database ga ulanib bolmadi")
        return
    try:
        async with conn.transaction():
            order_query = """
                SELECT id, car_id, status
                FROM rentals
                WHERE id = $1
            """
            order = await conn.fetchrow(order_query, int(order_id))
            if not order:
                print(" Bunday order topilmadi")
                return

            if order["status"] != "active":
                print(" Bu order allaqachon yopilgan yoki bekor qilingan")
                return
            car_id = order["car_id"]
            update_order = """
                UPDATE rentals
                SET status = 'finished'
                WHERE id = $1
            """
            await conn.execute(update_order, int(order_id))
            update_car = """
                UPDATE cars
                SET status = 'available'
                WHERE id = $1
            """
            await conn.execute(update_car, car_id)

            print(" Order muvaffaqiyatli yopildi")
            print(" Mashina yana available holatda")

    except ValueError:
        print(" Order ID notogri kiritildi")

    except Exception as e:
        print(" Xatolik yuz berdi, amaliyot bekor qilindi:", e)

    finally:
        try:
            await conn.close()
        except Exception:
            pass
