from db_ulash import get_connection
async def deactivate_car():
    car_id = input("Mashina ID ni kiriting: ")
    conn = await get_connection()
    try:
        check_query = "SELECT id, status FROM cars WHERE id=$1"
        car = await conn.fetchrow(check_query, int(car_id))
        if not car:
            print(" Bunday mashina topilmadi")
            return

        if car["status"] == "inactive":
            print(" Bu mashina allaqachon inactive")
            return
        query = """
            UPDATE cars
            SET status = 'inactive'
            WHERE id = $1
        """
        await conn.execute(query, int(car_id))
        print(" Mashina muvaffaqiyatli ochirildi (inactive)")
    except ValueError:
        print(" ID notogri kiritildi")
    except Exception as e:
        print("Xatolik:", e)
    finally:
        await conn.close()
