import random
class Warrior:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        health = 100
    def attack(self, hiter):
            hit.health -= 20
warrior1 = input('Имя воина ')
warrior2 = input('Имя воина ')
warriors = [Warrior(warrior1), Warrior(warrior2)]
while True:
    q = input('Введите старт для начала прогрыммы,выход для выхода ').lower()
    if q == 'старт':
        a = random.randint(0, 1)
        attacker = warriors[a]
        hit = warriors[a-1]
        attacker.attack(hit)
        print(f'{attacker.name}ударил {hit.name}')
        print(f'У {hit.name} осталось здоровья {hit.health}')
        if hit.health <= 0:
            print(attacker.name, 'победил!!!')
            break
    elif q == 'выход':
        break
    else:
        print('Ошибка')