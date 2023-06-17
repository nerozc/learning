def summa_n(n):
    res = 0
    for i in range(1,n+1):
        res += i
    return res
n = int(input("Введите число "))
print(f'Я знаю, что сумма чисел от 1 до {n} равна {summa_n(n)}')