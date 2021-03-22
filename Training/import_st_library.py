
# from importlib import reload
import pprint
# import math as m
from math import e, pi, factorial as fact
def say_hello(name):
    print(f"hello, {name}")


def summa(*args):
    return sum (args)

def factorial(n):
    print('my func')
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr

my_str = "YOU'RE BREATHTAKING!"
my_num1 = 2
my_num2 = 3

pprint.pprint(locals())
pprint.pprint(e)
pprint.pprint(pi)
pprint.pprint(factorial(10))
pprint.pprint(fact(10))