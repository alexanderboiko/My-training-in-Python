# def rec(x):
#     if x<4:
#         print(x)
#         rec(x+1)
#         print(x)
#
# rec(1)

# факториал
# def fact(x):
#     if x==1:
#         return 1
#     return fact(x-1)*x
#
# print(fact(4))
# print(fact(50))

#Fibonacci
# def fib(n):
#     if n ==1 :
#         return 0
#     if  n ==2:
#         return 1
#     return fib(n-1)+fib(n-2)
#
# print(fib(5))
# print(fib(6))
# print(fib(7))

#palindrome
def palindrome(s):
    if len(s)<=1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])
print(palindrome('acф'))