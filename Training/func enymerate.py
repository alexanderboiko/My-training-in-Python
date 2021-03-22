# a = [10,20,30,40]
#
# print(list(enumerate(a)))
#
# for index, value in enumerate(a):
#     print(index, value)

a = [10,20,30,40,50,60]
s = 'hello'
t = ('apple', 'banana', 'mango')
d = {'a':1, 'b': 2, 'c':3}
for index, value in enumerate(a,1):
    print(index,value)