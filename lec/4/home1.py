# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12

import random


def create_list(lenght, min_value, max_value):
    new_list = []

    for x in range(0, lenght):
        new_list.append(random.randrange(min_value, max_value + 1))

    return new_list


def searching_for_identical_values(first_list, second_list):
    identical_values_list = []

    for x in second_list:
        for y in range(0, len(first_list)):
            if x in first_list:
                identical_values_list.append(x)
                break

    return sorted(list(set(identical_values_list)))


lenght_first_array = int(input('Enter the length of the first array: '))
first_array = create_list(lenght_first_array, 0, 10)

lenght_second_array = int(input('Enter the length of the second array: '))
second_array = create_list(lenght_second_array, 0, 10)

new_array = searching_for_identical_values(first_array, second_array)
print(new_array)
