# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('test_5.txt', 'w') as file_obj:
    line = input('Введите числа через пробел: ')
    print(f'В файле - {line}')
    file_obj.writelines(line)
    numbers = line.split()
    print("Сумма чисел ", sum(map(int, numbers)))