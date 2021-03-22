#определение функции
# def sayHello():
#     print('hello')
#     print('world')
# sayHello()
# print('pause')
# sayHello()

# def square(x):
#     print('квадрат', x,'=', x**2)
#
#
#
# def multiply(a,b):
#     print(a*b)
#
# def even(a):
#     if a%2==0:
#         print(a,'chetnoe')
#     else:
#         print(a,'nechetnoe')
# for i in range(20,31):
#     even(i)

# def factorial(n):
#     pr=1
#     for i in range(2,n+1):
#         pr=pr*i
#     print(pr)
#
# factorial(10)

# a = abs(-7)
# b = max(4,abs(-90),5,6,min(80,87),6,4,2)
# print(a,b)

# def square(x):
#     return x**2
# a = square(square(3))
# print(a)

# def even(x):
#     return x%2==0
#
# for i in range(1,11):
#     print(i, even(i))

# def factorial(x):
#     pr =1
#     for i in range(2, x+1):
#         pr=pr*i
#     return pr
#
# def sochet(n,k):
#     return factorial(n)/(factorial(k)*factorial(n-k))
# print(sochet(5,3))

def sqAndPer(a,b):
    mas=[]
    mas.append(a*b)
    mas.append(2*(a+b))
    return mas

print(sqAndPer(4,5))