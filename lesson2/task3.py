month_num = int(input("Введите номер месяца от 1 до 12"))
season_list = ["Зима", "Весна", "Лето", "Осень"]
season_dict = {1 : "Зима", 2 : "Весна", 3 : "Лето", 4 : "Осень"}
if month_num == 12 or month_num == 1 or month_num == 2:
    print(season_list[0])
    print(season_dict.get(1))
elif month_num == 3 or month_num == 4 or month_num == 5:
    print(season_list[1])
    print(season_dict.get(2))
elif month_num == 6 or month_num == 7 or month_num == 8:
    print(season_list[2])
    print(season_dict.get(3))
elif month_num == 9 or month_num ==10 or month_num == 11:
    print(season_list[3])
    print(season_dict.get(4))
else:
    print("Вы ввели неверное число")



