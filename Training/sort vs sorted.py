# sort- метод списка vs sorted - встроенная функция
a = [4, -10, 43, -300, 54, 89, -34]
b = 'hello world'
c = ('hi', 'zero', 'abracadabra', 'pikachu')
# a.sort()
# print(a)
# a = sorted(a)
# print(a)
# b = sorted(b)
# print(b)
# c = sorted(c)
# print(c)
c = sorted(c, reverse=False)
print(c)