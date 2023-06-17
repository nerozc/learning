import random
number = random.randint(0,10)
guess = int(input("Введите число"))
if number == guess:
    print("Поздравляю!")
elif ((number - 1) == guess and (number + 1) == guess):
    print("Почти получилось")
else:
    print("Не повезло")