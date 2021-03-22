a = [5, 6, 7, 8]
b = [100, 200, 300, 40]
c = 'abcd'

# for i in range(4):
#     print(a[i], b[i])

rez = list(zip(a, b, c))
# print(list(rez))
# for t1, t2, t3 in zip (a,b,c):
#     print(t1, t2, t3)
# print(rez)
col1, col2, col3 = zip(*rez)
print(col1, col2, col3)