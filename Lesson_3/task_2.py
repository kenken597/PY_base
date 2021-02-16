# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user (*args):
    name = input("Input your name ")
    surname = input("Input your surname ")
    age = int(input("Input year of birth "))
    city = input("Input city where you living for ")
    email = input("Input your email ")
    phone = int(input("Input your phone number "))
    print(f'{name} {surname} {age} {city} {email} {phone}')


user()