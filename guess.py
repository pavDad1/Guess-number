import random
max_number = 100
max_attempts = 10
while True:
    secret = random.randint(1, max_number)
    attempts = 0

    while True:
        try:
            num = int(input("ваше число: "))
        except ValueError:
            print("пиши число")
            continue
        attempts += 1
        if num < secret:
            print("больше")

        elif num > secret:
            print("меньше")

        else:
            print("нашел за", attempts , "попытки")
            break

        if attempts == max_attempts:
            print("попытки закончились, было загадано", secret)
            break

    again = input("Сыграем еще? (да/нет): ")
    if again.lower() != "да":
        break