from startup.ulash import ulash
from typing import Optional 

def register() -> None:
    """
    Yangi foydalanuvchini ryxatdan otkazadi.
    Qadamlar:
    1. Bazaga ulanish (ulash funksiyasi orqali).
    2. Foydalanuvchidan login, email va parol sorash.
    3. 'users' jadvaliga yangi foydalanuvchini qoshish.
    4. Agar login yoki email mavjud bolsa, xato xabar chiqaradi.
    Returns:
        None
    """
    conn = ulash("asd", "admin1112")
    cursor = conn.cursor()
    username = input("Yangi login: ")
    email = input("Email: ")
    password = input("Parol: ")
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, password)
        )
        conn.commit()
        print("Royxatdan otish muvaffaqiyatli!")
    except Exception:
        conn.rollback()
        print("Bunday login yoki email mavjud.")
    finally:
        cursor.close()
        conn.close()