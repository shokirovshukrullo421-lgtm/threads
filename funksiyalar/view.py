from startup.ulash import ulash
from typing import Optional

def view_tweets(user_id: int) -> None:
    """
    Foydalanuvchi uchun tweetlarni ko'rsatadi va ularga like/follow amallarini bajarishga imkon beradi.

    Qadamlar:
    1. Bazaga ulanish (ulash funksiyasi orqali).
    2. Barcha tweetlarni foydalanuvchi va muallif ma'lumotlari bilan olish.
    3. Tweetlar bo'sh bo'lsa, xabar chiqaradi va chiqadi.
    4. Foydalanuvchi tweetlar bo'yicha navbat bilan yuradi:
       - Like / Unlike
       - Follow / Unfollow
       - Keyingi / Oldingi tweet
       - Chiqish
    5. Barcha o'zgarishlar bazaga commit qilinadi yoki xatolik yuz bersa rollback qilinadi.

    Args:
        user_id (int): Amallarni bajaradigan foydalanuvchi ID si.

    Returns:
        None
    """
    conn = ulash("asd", "admin1112")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.id, u.id, u.username, t.content
        FROM tweets t
        JOIN users u ON t.user_id = u.id
        ORDER BY t.created_at DESC
    """)
    tweets = cursor.fetchall()
    if not tweets:
        print("Hali tweetlar mavjud emas.")
        cursor.close()
        conn.close()
        return
    index = 0
    while True:
        tweet = tweets[index]
        tweet_id, author_id, author_name, content = tweet
        print(f"Tweet #{tweet_id} | @{author_name}")
        print(f"{content}")
        print("\nAmallar:")
        print("1. Like / Unlike")
        print("2. Follow / Unfollow")
        print("3. Keyingi tweet")
        print("4. Oldingi tweet")
        print("5. Chiqish")
        choice = input("Tanlov: ")
        if choice == "1":
            try:
                cursor.execute(
                    "INSERT INTO likes (user_id, tweet_id) VALUES (%s, %s)",
                    (user_id, tweet_id)
                )
                conn.commit()
                print("❤️ Like bosildi!")
            except Exception:
                conn.rollback()
                cursor.execute(
                    "DELETE FROM likes WHERE user_id=%s AND tweet_id=%s",
                    (user_id, tweet_id)
                )
                conn.commit()
                print("💔 Like bekor qilindi!")
        elif choice == "2":
            if user_id == author_id:
                print("O'zingizga follow bo'lmaysiz.")
            else:
                try:
                    cursor.execute(
                        "INSERT INTO follows (follower_id, following_id) VALUES (%s, %s)",
                        (user_id, author_id)
                    )
                    conn.commit()
                    print("Follow qilindi!")
                except Exception:
                    conn.rollback()
                    cursor.execute(
                        "DELETE FROM follows WHERE follower_id=%s AND following_id=%s",
                        (user_id, author_id)
                    )
                    conn.commit()
                    print("Follow bekor qilindi!")
        elif choice == "3":
            if index < len(tweets) - 1:
                index += 1
            else:
                print("Bu oxirgi tweet.")
        elif choice == "4":
            if index > 0:
                index -= 1
            else:
                print("Bu birinchi tweet.")
        elif choice == "5":
            break
        else:
            print("Notog'ri tanlov")
    cursor.close()
    conn.close()