# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seas_list = ["winter", "spring", "summer", "autumn"]
seas_dict = {1 : "winter", 2 : "spring", 3 : "summer", 4 : "autumn"}

user_month = int(input("Введите месяц числом от 1 до 12 "))
if user_month == 1 or user_month == 2 or user_month == 12:
    print(seas_list[0])
    print(seas_dict.get(1))
elif user_month == 3 or user_month == 4 or user_month == 5:
    print(seas_list[1])
    print(seas_dict.get(2))
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(seas_list[2])
    print(seas_dict.get(3))
elif user_month == 9 or user_month == 10 or user_month == 11:
    print(seas_list[3])
    print(seas_dict.get(4))