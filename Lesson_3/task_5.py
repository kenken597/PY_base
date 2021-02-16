# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.


def sum_numbers():
    sum_result = 0
    exit = False
    while exit == False:
        number = input("Input numbers or enter NO for end ").split()
        result = 0
        for i in range(len(number)):
            if number[i] == 'NO' or number[i] == "no":
                exit = True
                break
            else:
                result += int(number[i])
        sum_result += result
        print(f'Actual sum {sum_result}')
    print(f'Final sum {sum_result}')

sum_numbers()