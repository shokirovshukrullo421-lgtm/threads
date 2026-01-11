from startup.ulash import ulash

def profile(user_id: int) -> None:
    """
    Foydalanuvchi profilini ko'rsatadi:
    - Username
    - Followers va Following
    - Foydalanuvchining tweetlari va ularning like soni
    - Like qilgan foydalanuvchilar

    Shuningdek, foydalanuvchi o'z tweetlarini o'chirishi mumkin.

    Args:
        user_id (int): Profilni ko'rayotgan foydalanuvchi ID si.

    Returns:
        None
    """
    conn = ulash("asd", "admin1112")
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    if not user:
        print("Foydalanuvchi topilmadi.")
        cursor.close()
        conn.close()
        return

    username = user[0]
    print(f"\n=== Profilim @{username} ===")

    cursor.execute("""
        SELECT u.username
        FROM follows f
        JOIN users u ON f.follower_id = u.id
        WHERE f.following_id=%s
    """, (user_id,))
    followers = cursor.fetchall()
    print(f"\nFollowers ({len(followers)}):")
    if followers:
        for follower in followers:
            print(f" - {follower[0]}")
    else:
        print("Hali followers yo'q.")
    cursor.execute("""
        SELECT u.username
        FROM follows f
        JOIN users u ON f.following_id = u.id
        WHERE f.follower_id=%s
    """, (user_id,))
    following = cursor.fetchall()
    print(f"\nFollowing ({len(following)}):")
    if following:
        for followee in following:
            print(f" - {followee[0]}")
    else:
        print("Hali following yo'q.")
    cursor.execute("""
        SELECT t.id, t.content, COUNT(l.user_id) AS like_count
        FROM tweets t
        LEFT JOIN likes l ON t.id = l.tweet_id
        WHERE t.user_id=%s
        GROUP BY t.id
        ORDER BY t.created_at DESC
    """, (user_id,))
    tweets = cursor.fetchall()
    if not tweets:
        print("\nHali tweetlar mavjud emas.")
    else:
        print("\nSizning tweetlaringiz va like'lar:")
        for tweet in tweets:
            tweet_id, content, like_count = tweet
            print(f"{tweet_id}. {content} | Likes: {like_count}")
            cursor.execute("""
                SELECT u.username
                FROM likes l
                JOIN users u ON l.user_id = u.id
                WHERE l.tweet_id=%s
            """, (tweet_id,))
            likers = cursor.fetchall()
            if likers:
                liker_names = ", ".join([l[0] for l in likers])
                print(f"    Like qilganlar: {liker_names}")
    while True:
        print("\nAmallar:")
        print("1. Tweet o'chirish")
        print("2. Chiqish")

        choice = input("Tanlov: ")
        if choice == "1":
            tweet_id_del = input("O'chirmoqchi bo'lgan tweet ID: ")
            try:
                cursor.execute(
                    "DELETE FROM tweets WHERE id=%s AND user_id=%s",
                    (tweet_id_del, user_id)
                )
                if cursor.rowcount == 0:
                    print("Tweet topilmadi yoki sizga tegishli emas.")
                else:
                    conn.commit()
                    print("Tweet muvaffaqiyatli o'chirildi!")
            except Exception as e:
                conn.rollback()
                print("Xatolik yuz berdi:", e)
        elif choice == "2":
            break
        else:
            print("Notog'ri tanlov")
    cursor.close()
    conn.close()
