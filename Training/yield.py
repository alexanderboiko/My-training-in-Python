# yield показывает что функция-генератор
# генератор ленивый, одноразовый
# после выполнения  yield стает на паузу


squares = (e ** 2 for e in range(0, 11, 2))


def squares2():
    for e in range(0, 11, 2):
        yield e ** 2


gen = squares2()
print(gen)

for i in gen:
    print(i)

def pause():
    print('Generator working')
    while True:
        print(a)
        yield a

a = 10
gen = pause()
print(next(gen))