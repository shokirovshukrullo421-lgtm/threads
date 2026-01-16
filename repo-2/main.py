import random
from main import check_guess  # vaqtincha bo‘sh bo‘lsa ham chaqiriladi

def start_game():
    secret_number = random.randint(1, 100)
    attempts = 5

    print("Men 1 dan 100 gacha son o'yladim. Topib ko'r!")

    for _ in range(attempts):
        guess = int(input("Son kiriting: "))
        if check_guess(guess, secret_number):
            print("Tabriklaymiz, siz yutdingiz!")
            return

    print(f"Afsus, siz yutqazdingiz. To'g'ri son: {secret_number}")

def main():
    start_game()

if __name__ == "__main__":
    main()