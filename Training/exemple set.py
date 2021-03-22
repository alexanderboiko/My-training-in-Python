# создание
# a = [1,2,3,3,4,2,5,1]
# a = list(set(a))
# print(a)

# добавление элемента
# a = {54,32,54,3,4,2}
# a.add(9)
# a.add(4)
# a.update([5,6,7,3])
# a.update(range(5,10))
# print(a)

# удаление
# a = {54,32,54,3,4,2}
# a.discard(4)
# a.remove(54)
# a.clear()
# print(a.pop())
# print(a)

# операции над множествами
# a = {54,32,54,3,4,2}
# print(len(a))
# print(4 in a, 7 not in a)

# a = {4,3,2,1}
# b = {3,4,5,6,7}
# c = {10,11,12}
# print(a.intersection(b))
# a.intersection_update(b)
# a&=b
# print(a.union(b))
# a = a.union(b)
# print(a)
# b-=a
# print(b)
# print(a^b)
# print(a==b)

text = input()
a = set()
while text !='':
    slova = text.split()
    a.update(slova)
    text = input()
print(len(a))