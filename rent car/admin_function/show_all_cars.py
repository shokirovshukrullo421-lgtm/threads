from db_ulash import get_connection
import asyncio
async def show_all_cars():
    conn = await get_connection()
    try:
        query = """
            SELECT id, brand, model, year, color, price_per_day, status
            FROM cars
        """
        cars = await conn.fetch(query)

        if not cars:
            print(" Mashinalar yoq")
            return
        for car in cars:
            print(
                f"ID: {car['id']} | "
                f"{car['brand']} {car['model']} | "
                f"{car['year']} | "
                f"{car['color']} | "
                f"{car['price_per_day']}$/day | "
                f"{car['status']}"
            )

    except Exception as e:
        print("Xatolik:", e)
    finally:
        await conn.close()
