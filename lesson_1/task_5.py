#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.

profit = int(input("Введите значение выручки фирмы "))
costs = int(input("Введите значение издержек фирмы "))
if profit > costs:
    print("Фирма работает в плюс!")
    rent = ((profit - costs)/profit)
    print("Рентабельность выручки " + "%.2f" % rent)
    empl = int(input("Введите количество сотрудников фирмы "))
    profit_per_empl = (((profit - costs)/empl))
    print("Прибыль фирмы на одного сотрудника " + "%.2f" % profit_per_empl)
elif (profit < costs):
    print("Фирма работает в минус :-(")
elif (profit == costs):
    print("Издержки и прибыль равны. Фирма сработала в ноль.")