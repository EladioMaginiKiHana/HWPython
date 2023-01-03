#Задача 20:
#В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#В случае с английским алфавитом очки распределяются так:
#A, E, I, O, U, L, N, S, T, R – 1 очко;
#D, G – 2 очка;
#B, C, M, P – 3 очка;
#F, H, V, W, Y – 4 очка;
#K – 5 очков;
#J, X – 8 очков;
#Q, Z – 10 очков.

#А русские буквы оцениваются так:
#А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#Д, К, Л, М, П, У – 2 очка;
#Б, Г, Ё, Ь, Я – 3 очка;
#Й, Ы – 4 очка;
#Ж, З, Х, Ц, Ч – 5 очков;
#Ш, Э, Ю – 8 очков;
#Ф, Щ, Ъ – 10 очков.

#Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

#Ввод: ноутбук
#Вывод: 12

one_points = ['A','E','I','O','U','L','N','S','T','R', 'А','В','Е','И','Н','О','Р','С','Т']
two_points = ['D','G','Д','К','Л','М','П','У']
three_points = ['B','C','M','P','Б','Г','Ё','Ь','Я']
four_points = ['F','H','V','W','Y','Й','Ы']
five_points = ['K','Ж','З','Х','Ц','Ч'] 
eight_points = ['J','X','Ш','Э','Ю']
ten_points = ['Q','Z','Ф','Щ','Ъ']

word = input()
total = 0


for x in range(0, len(word)):
    if word[x].upper() in one_points:
        total += 1
    elif word[x].upper() in two_points:
        total += 2
    elif word[x].upper() in three_points:
        total += 3
    elif word[x].upper() in four_points:
        total += 4
    elif word[x].upper() in five_points:
        total += 5
    elif word[x].upper() in eight_points:
        total += 8
    elif word[x].upper() in ten_points:
        total += 10
    else:
        total += 0

print(total)