from db_ulash import get_connection

async def add_new_car():
    brand = input("Brand: ")
    model = input("Model: ")
    year = input("Year: ")
    color = input("Color: ")
    price_per_day = input("Price per day: ")
    conn = await get_connection()
    try:
        query = """
            INSERT INTO cars (brand, model, year, color, price_per_day, status)
            VALUES ($1, $2, $3, $4, $5, 'available')
        """
        await conn.execute(
            query,
            brand,
            model,
            int(year),
            color,
            float(price_per_day)
        )
        print(" Mashina muvaffaqiyatli qoshildi")
    except ValueError:
        print(" Year yoki price notogri formatda")
    except Exception as e:
        print("Xatolik:", e)
    finally:
        await conn.close()
