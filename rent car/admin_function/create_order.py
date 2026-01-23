from db_ulash import get_connection
from datetime import datetime
from log.logger import logger

async def create_order():
    user_id = input("Foydalanuvchi ID: ")
    car_id = input("Mashina ID: ")
    start_date = input("Start date (YYYY-MM-DD): ")
    end_date = input("End date (YYYY-MM-DD): ")

    conn = await get_connection()
    logger.info("Database ga ulanildi (create_order)")

    try:
        car_query = "SELECT id, price_per_day, status FROM cars WHERE id=$1"
        car = await conn.fetchrow(car_query, int(car_id))

        if not car:
            logger.warning(f"Mashina topilmadi | car_id={car_id}")
            print(" Bunday mashina topilmadi")
            return

        if car["status"] != "available":
            logger.warning(
                f"Mashina mavjud emas | car_id={car_id} | status={car['status']}"
            )
            print(" Bu mashina hozir band yoki inactive")
            return

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days = (end - start).days

        if days <= 0:
            logger.warning(
                f"Notogri sana | start={start_date} end={end_date}"
            )
            print(" Sana notogri kiritildi")
            return

        total_price = days * float(car["price_per_day"])

        rental_query = """
            INSERT INTO rentals (user_id, car_id, start_date, end_date, total_price, status)
            VALUES ($1, $2, $3, $4, $5, 'active')
        """
        await conn.execute(
            rental_query,
            int(user_id),
            int(car_id),
            start_date,
            end_date,
            total_price
        )

        update_car = "UPDATE cars SET status='rented' WHERE id=$1"
        await conn.execute(update_car, int(car_id))

        logger.info(
            f"Order yaratildi | user_id={user_id} car_id={car_id} "
            f"days={days} total_price={total_price}"
        )

        print(f"Order yaratildi | Total price: {total_price}$ | Status: active")

    except ValueError:
        logger.warning(
            f"Format xato | user_id={user_id} car_id={car_id} "
            f"start={start_date} end={end_date}"
        )
        print(" ID yoki sana format notogri")

    except Exception:
        logger.exception("Order yaratishda kutilmagan xatolik")

    finally:
        await conn.close()
        logger.info("Database ulanish yopildi (create_order)")
