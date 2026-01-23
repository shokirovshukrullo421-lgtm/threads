from db_ulash import get_connection
from log.logger import logger

async def add_new_car():
    brand = input("Brand: ")
    model = input("Model: ")
    year = input("Year: ")
    color = input("Color: ")
    price_per_day = input("Price per day: ")

    conn = await get_connection()
    logger.info("Database ga ulanildi")

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

        logger.info(
            f"Yangi mashina qo‘shildi: {brand} {model}, {year}, {color}, {price_per_day}"
        )

    except ValueError:
        logger.warning(
            f"Notogri format: year={year}, price={price_per_day}"
        )

    except Exception:
        logger.exception("Mashina qoshishda xatolik yuz berdi")

    finally:
        await conn.close()
        logger.info("Database ulanish yopildi")
