# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )

# Output: 9

import random


def create_list(lenght, min_value, max_value):
    new_list = []

    for x in range(0, lenght):
        new_list.append(random.randrange(min_value, max_value + 1))

    return new_list


bushes = int(input('enter the number of bushes: '))
garden = create_list(bushes, 5, 35)
harvest = []

for x in range(0, len(garden)):
    if x == 0:
        harvest.append(garden[-1] + garden[x] + garden[x+1])
    elif x != len(garden) - 1:
        harvest.append(garden[x-1] + garden[x] + garden[x+1])
    elif x == len(garden) - 1:
        harvest.append(garden[x-1] + garden[x] + garden[0])

print(f'Maximum harvest at a time: {max(harvest)}\nIt`s a the {harvest.index(max(harvest)) + 1}'
      + f' bush: {garden[harvest.index(max(harvest)) - 1]} {garden[harvest.index(max(harvest))]} {garden[harvest.index(max(harvest)) + 1]}')
print(garden)