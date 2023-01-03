#Задача 16:
#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
#Заполните массив случайными натуральными числами от 1 до N/2.
#Выведите, сколько раз X встречается в массиве.

#Ввод: 5
#Ввод: 1

#1 2 1 2 2
#Вывод: 2

import random

def create_List(range_Min_Num, range_Max_Num,Length):
   random_Array = []

   for i in range(0, Length):
       random_num = random.randint(range_Min_Num, range_Max_Num + 1)
       random_Array.append(random_num)

   return random_Array

def search_Elements(array, element):

   counts = 0
   for i in range(0, len(array)):
       if element == array[i]:
           counts += 1

   if counts == 0:
       lever = "Not found"
   else:
       lever = f'The value {element} is contained in the array {counts} times.'

   return print(lever)


size = int(input('Enter the size of the array: '))
N_check = int(input("What number do you want to find: "))
numbers = size // 2

my_Array = create_List(0,numbers,size)
search_Elements(my_Array, N_check)
