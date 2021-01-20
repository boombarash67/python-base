profit = int(input("Введите выручку фирмы "))
costs = int(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Коэффициент выручки составил {profit / costs}")
    workers = int(input("Введите количество сотрудников"))
    print(f"прибыль в расчете на одного сотрудника {profit / workers}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")