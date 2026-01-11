from startup.ulash import ulash

def write_tweet(user_id: int) -> None:
    """
    Foydalanuvchi yangi tweet yozadi va bazaga qoshadi.

    Qadamlar:
    1. Bazaga ulanish (ulash funksiyasi orqali).
    2. Foydalanuvchidan tweet matnini sorash (280 ta belgidan oshmasligi kerak).
    3. Tweetni 'tweets' jadvaliga qoshish.
    4. Agar xatolik yuz bersa, rollback qilinadi va xato xabar chiqadi.

    Args:
        user_id (int): Tweetni yozayotgan foydalanuvchi ID si.

    Returns:
        None
    """
    conn = ulash("asd", "admin1112")
    cursor = conn.cursor()
    print("\n=== Yangi Tweet yozish ===")
    content = input("Tweet matni (280 ta belgi bilan cheklangan): ")
    if len(content) > 280:
        print("Tweet juda uzun. 280 ta belgidan oshmasligi kerak.")
        cursor.close()
        conn.close()
        return

    try:
        cursor.execute(
            "INSERT INTO tweets (user_id, content) VALUES (%s, %s)",
            (user_id, content)
        )
        conn.commit()
        print("Tweet muvaffaqiyatli qo‘shildi!")
    except Exception as e:
        conn.rollback()
        print("Tweet qo‘shishda xatolik yuz berdi:", e)
    finally:
        cursor.close()
        conn.close()