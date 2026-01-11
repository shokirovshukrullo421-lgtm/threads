from funksiyalar.login import login
from funksiyalar.register import register
from funksiyalar.view import view_tweets
from funksiyalar.write import write_tweet
from funksiyalar.profil import profile
user_id = None
while not user_id:
    print("\n1. Login\n2. Royxatdan otish\n3.chiqish")
    choice = input("Tanlov: ")
    if choice == "1":
        user_id = login()
    elif choice == "2":
        register()
        user_id = login() 
    elif choice == "3":
        print("Chiqildi")
        break 
    else:
        print("Notogri tanlov")
if user_id:
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Tweetlarni ko'rish")
        print("2. Tweet yozish")
        print("3. Profilim (keyin yoziladi)")
        print("4. Chiqish")

        choice = input("Tanlov: ")

        if choice == "1":
            view_tweets(user_id)
        elif choice == "2":
            write_tweet(user_id)
        elif choice == "3":
            profile(user_id)
            print(" Profil funksiyasi hozircha ishlamaydi")
        elif choice == "4":
            print("Chiqildi")
            break
        else:
            print(" Notogri tanlov")