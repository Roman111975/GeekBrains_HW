# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения
# используйте цикл while и арифметические операции.
n = int(input("Введите целое положительное число"))
r = -1
while n > 10:
    d = n % 10
    n //= 10
    if d > r:
        r = d
print("Самое большое целое число это", r)
