import math
# отсечение дробной части с округлением вверх
a = 20
b = 21
c = 22
d = math.ceil((a+b+c)/2)
print(d)

# отсечение дробной части с округлением вниз
n = math.floor(123.453)
print(n)

# отсечение дробной части
m = math.trunc(342525.354235)
print(m)