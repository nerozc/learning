import random
animals = []
discr = []
for i in range(3):
    for j in range(i):
        i = input("Введите название животного ")
        j = input("Введите описание животного ")
        animals.append(i)
        discr.append(j)
for i in range(3):
    print(random.choice(animals)+' '+ random.choice(discr))