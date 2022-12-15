def fibonache(n):
    # 0 1 1 2 3 5 8 

    if n == 0:
        return 1
    if n == 1:
        return 2 
    number0 = 0
    number1 = 1
    count = 2
    while n >= number1:
        if n == number1:
            return count
        temp = number1
        number1 += number0
        number0 = temp
        count += 1
    return -1

import random

from random import randint
n = int(input())
l = [randint(-50, 50) for i in range(1, n)]
count = 0
maxcount = 0
m = []
for el in l:
    if el >= 0:
        count += 1
        m.append(count)
    else:
        if count > maxcount:
            maxcount = count
        count = 0

print(l)
print(maxcount)
from random import randint
n = int(input())
l = [randint(-50, 50) for i in range(1, n)]
count = 0
maxcount = 0
m = []
for el in l:
    if el >= 0:
        count += 1
        m.append(count)
    else:
        if count > maxcount:
            maxcount = count
        count = 0

print(l)
print(maxcount)

def sinoptik(N):
    days=[]
    for _ in range(N):
        days.append(round(random.uniform(-10,50),0))  
    print(days)
    maxPeriod = maxPeriodResult = 0
    i = 0
    while i<N-1:
        if days[i]>0:
            while days[i]>0 and i<N-1:
                maxPeriod+=1
                i+=1
            if maxPeriodResult<maxPeriod: maxPeriodResult=maxPeriod
        maxPeriod=0
        i+=1
    return maxPeriodResult
