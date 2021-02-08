# 2. Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_list = []
space = 0
while space != " ":
    space = input("Введите любой элемент ")
    user_list.append(space)
user_list.pop(-1)
print(user_list)
empt = 0
for i in range(int(len(user_list) // 2)):
    user_list[empt], user_list[empt + 1] = user_list[empt + 1], user_list[empt]
    empt += 2
print(user_list)
