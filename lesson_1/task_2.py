#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

import datetime

def convert(time):
    return str(datetime.timedelta(seconds = time))

time = int(input('Введите время в секундах '))
print(convert(time))