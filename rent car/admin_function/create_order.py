from db_ulash import get_connection
from datetime import datetime

async def create_order():
    user_id = input("Foydalanuvchi ID: ")
    car_id = input("Mashina ID: ")
    start_date = input("Start date (YYYY-MM-DD): ")
    end_date = input("End date (YYYY-MM-DD): ")
    conn = await get_connection()
    try:
        car_query = "SELECT id, price_per_day, status FROM cars WHERE id=$1"
        car = await conn.fetchrow(car_query, int(car_id))

        if not car:
            print(" Bunday mashina topilmadi")
            return

        if car["statu"] != "available":
            print("Bu mashina hozir band yoki inactive")
            return
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days = (end - start).days

        if days <= 0:
            print(" Sana notogri kiritildi")
            return
        total_price = days * float(car["price_per_day"])
        rental_query = """
            INSERT INTO rentals (user_id, car_id, start_date, end_date, total_price, status)
            VALUES ($1, $2, $3, $4, $5, 'active')
        """
        await conn.execute(rental_query, int(user_id), int(car_id), start_date, end_date, total_price)
        update_car = "UPDATE cars SET status='rented' WHERE id=$1"
        await conn.execute(update_car, int(car_id))
        print(f" Order yaratildi | Total price: {total_price}$ | Status: active")
    except ValueError:
        print(" ID yoki sana format notogri")
    except Exception as e:
        print("Xatolik:", e)
    finally:
        await conn.close()
