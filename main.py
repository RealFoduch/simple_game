 # Игра "Угадай число от 0 до 100"

import random

number = random.randint(0, 100)

while True:

    answer = input("Введите число: ")
    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("Введить корректное число!")
        continue

    user_answer = int(answer)

    if user_answer > number:
        print("Загаданное число меньше")
    elif user_answer < number:
        print("Загаданное число больше")
    else:
        print("Вы угадали число!")
        break