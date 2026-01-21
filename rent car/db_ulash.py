import asyncpg
DB_NAME = "rent_car"
DB_USER = "postgres"
DB_PASS = "admin1112"
DB_HOST = "localhost"
DB_PORT = 5432
async def get_connection():
    """
    PostgreSQL ga ulanish funksiyasi
    """
    return await asyncpg.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
