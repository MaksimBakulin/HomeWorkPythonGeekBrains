import random

a = input("Вы играете один? (Y/N): ")
total_numbers_candies = 2021
player_1 = "Первый игрок"
player_2 = "Второй игрок"

def Draw_first_move(player_1, player_2):
    random_num = random.randint(1, 2)
    if random_num == 1:
        return player_1
    else:
        return player_2

if a == "Y":
    player_1 = input("Игрок, введите ваше имя: ")
    player_2 = "Очень умный Бот"
    current_player = Draw_first_move(player_1, player_2)
    print(f"Первым ходит {current_player}")
    while total_numbers_candies > 0:
        if current_player == player_1:
            taken_candy = int(input("Сколько конфет вы возьмете? (1 - 28): "))
            if 0 < taken_candy < 29:
                total_numbers_candies -= taken_candy
                print(f"На столе осталось {total_numbers_candies} конфет.")
                if total_numbers_candies > 0:
                        current_player = player_2
                        print(f"Теперь ходит {player_2}")
            else:
                print("Вы ввели неправильное количество конфет! Будьте внимательнее!")
        else:
            if total_numbers_candies > 56:
                candy_bot = random.randint(1, 28)
                total_numbers_candies -= candy_bot
                print(f"Бот взял {candy_bot} конфет")
                print(f"На столе осталось {total_numbers_candies} конфет.")
                current_player = player_1
            elif 28 < total_numbers_candies < 57:
                candy_bot = total_numbers_candies - 29
                if candy_bot == 0:
                    candy_bot = 1
                    total_numbers_candies -= candy_bot
                    print(f"Бот взял {candy_bot} конфет")
                    print(f"На столе осталось {total_numbers_candies} конфет.")
                    current_player = player_1
                else:
                    total_numbers_candies -= candy_bot
                    print(f"Бот взял {candy_bot} конфет")
                    print(f"На столе осталось {total_numbers_candies} конфет.")
                    current_player = player_1
            else:
                candy_bot = total_numbers_candies
                total_numbers_candies -= candy_bot
                print(f"Бот взял {candy_bot} конфет")
                print(f"На столе осталось {total_numbers_candies} конфет.")
    print(f"Победил игрок - {current_player}")
elif a == "N":
    player_1 = input("Первый игрок, введите ваше имя: ")
    player_2 = input("Второй игрок, введите ваше имя: ")
    current_player = Draw_first_move(player_1, player_2)
    print(f"Первым ходит {current_player}")
    while total_numbers_candies > 0:
        taken_candy = int(input("Сколько конфет вы возьмете? (1 - 28): "))
        if 0 < taken_candy < 29:
            total_numbers_candies -= taken_candy
            print(f"На столе осталось {total_numbers_candies} конфет.")
            if total_numbers_candies > 0:
                if current_player == player_1:
                    current_player = player_2
                    print(f"Теперь ходит {player_2}")
                else:
                    current_player = player_1
                    print(f"Теперь ходит {player_1}")
        else:
            print("Вы ввели неправильное количество конфет! Будьте внимательнее!")
    print(f"Победил игрок - {current_player}")
else:
    print("Введено некорректное значение!!! В меню выбора количества игроков необходимо ввести 'Y' или 'N'!!!")