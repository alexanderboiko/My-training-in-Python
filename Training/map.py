# a = [-1,2,-3,4,-5]
# b = list(map(abs,a))
# c = [abs(i) for i in a]
# print(c)

# def f (x):
#     return x**2
#
# a = ['hello', 'good morning', 'hi']
# b = list(map(len, a))
# print(b)
#
# s = list(map(int,input().split()))
# print(s)

a = ['hello', 'good morning', 'hi']
b = list(map(lambda x: x+'!', a))
print(b)