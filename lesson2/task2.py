my_list = []
count = int(input("Введите количество элементов списка"))
i_number = 0
elem = 0
while i_number < count:
    my_list.append(input("Введите следующее значение списка"))
    i_number += 1
    for el in range(int(len(my_list)/2)):
        my_list[elem], my_list[elem + 1] = my_list[elem + 1], my_list[elem]
        elem += 2
        print(my_list)
