# a, b, *c = [True,'hello', 9, '54', 3, 67]
# print(a,b,c)

# s = [4,10]
# # print(list(range(1,5)))
# # print(list(range(*s)))

# def f(a,b,c,d):
#     print(a,b,c,d)
#
# f(1,2,3,4)
# e=('hello', True, 78,[3,4,5])
#
# f(*e)

# def f(*args):
#     s=0
#     for i in args:
#         s+=i
#     return s
# print(f(1,2))
#
# def f(*args,**kwargs):
#     print(args,kwargs)
#
# f(5,4,2,34,5,a=5,b=8,d='hello')

def f (*args,**kwargs):
    print(args,kwargs)

def outPrint (*args, sep='#', end='&'):
    print(args,sep,end)

outPrint(1,2,3,4,5,sep='90')
outPrint(1,2)

a = [3,4,5,6,7]
print(*a)
