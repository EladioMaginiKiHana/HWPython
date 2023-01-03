# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random


def create_List(range_Min_Num, range_Max_Num, Length):
    random_Array = []

    for i in range(0, Length):
        random_num = random.randint(range_Min_Num, range_Max_Num + 1)
        random_Array.append(random_num)

    return random_Array


size = int(input('Enter the size of the array: '))
N_check = int(input("What number do you want to find: "))
my_Array = create_List(1, size, size)
set_my_array = set(my_Array)
second_array = set_my_array

for i in range(0, len(set_my_array)):
    if max(set_my_array) > N_check:
        second_array = set_my_array.remove(max(set_my_array))
    elif max(set_my_array) <= N_check:
        print(f'Output: {max(set_my_array)}')
        break
    else:
        print('Your number is the smallest number in the array')
        break

print(set_my_array)
