from db_ulash import get_connection
import asyncpg

async def show_active_cars():
    try:
        conn = await get_connection()

        query = """
        SELECT id, brand, model, year, price_per_day
        FROM cars
        WHERE is_active = TRUE
        ORDER BY id
        """

        cars = await conn.fetch(query)

        if not cars:
            print("\n Hozircha aktiv mashinalar yoq.\n")
            return

        print("\n Aktiv mashinalar royxati:")
        print("-" * 50)

        for car in cars:
            print(
                f"ID: {car['id']} | "
                f"{car['brand']} {car['model']} | "
                f"Year: {car['year']} | "
                f"Price/day: {car['price_per_day']}"
            )

        print("-" * 50)
    except asyncpg.PostgresError as e:
        print(" Database xatosi:", e)
    except Exception as e:
        print(" Kutilmagan xato:", e)
    finally:
        if 'conn' in locals():
            await conn.close()
