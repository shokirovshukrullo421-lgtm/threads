from startup.ulash import ulash
from typing import Optional  

def login() -> Optional[int]:
    """
    Foydalanuvchini tizimga kirishga urinadi va uning ID sini qaytaradi.
    Qadamlar:
    1. Bazaga ulanish (ulash funksiyasi orqali).
    2. Foydalanuvchidan login va parol so'rash.
    3. 'users' jadvalidan foydalanuvchini tekshirish.
    4. Foydalanuvchi topilsa, ID sini qaytaradi; topilmasa None.
    Returns:
        int | None: Foydalanuvchining ID si yoki None.
    """
    conn = ulash("asd", "admin1112")  
    cursor = conn.cursor()

    username = input("Login: ")
    password = input("Parol: ")
    
    cursor.execute(
        "SELECT id FROM users WHERE username=%s AND password_hash=%s",
        (username, password)
    )
    
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        print("Tizimga muvaffaqiyatli kirdingiz!")
        return user[0]
    else:
        print("Login yoki parol notogri.")
        return None