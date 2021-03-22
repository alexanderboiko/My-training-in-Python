#[выражение for val in коллекция]
# a = [i**2 for i in range(10)]
# print(a)

import random
# a = [random.randint(-10,10) for i in range(10)]
# print(a)
# b = [abs(elem) for elem in a]
# print(b)

# a = [random.randint(-10,10) for i in range(10)]
# print(a)
# b = [elem for elem in a if elem%2==0]
# print(b)

# a = input().split()
# a = [int(i) for i in a]
# print(a)

# n = 5
# m = 4
#
# a = [[0]*m for i in range(n)]
# for i in a:
#     print(i)

# a = [i*j for i in [2,3,4,5] for j in [1,2,3] if i*j>=10]
# print(a)

#Генератор списка
a = [i**2 for i in range(1,6)]
print(a)
c = (i for i in range(100000000))
for i in c:
    print(i)
# Выражения генераторы
b = (i**2 for i in range(1,6))
for i in b:
    print(i)