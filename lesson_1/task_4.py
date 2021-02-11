# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_num = int(input("Введите целое положительное число "))
number_list = []
while user_num > 0:
    number_list.append(user_num % 10)
    user_num //= 10
big_number = max(number_list)
print(big_number)