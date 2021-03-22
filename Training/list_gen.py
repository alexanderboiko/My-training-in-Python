# генератор возвращает обьект а не коллекцию
# генератор ленивый, не выполняет действий и не занимает память пока не потребуется
# генератор проверяет источник при создании!!!
# генератор одноразовый, если исчерпан то бросает StopIteration
# используй генексп вместо компс, кроме случаев когда нужна длина len или индексы

import pprint

squares = [e * e for e in range(10) if e % 2 == 0]

text = "hello world"
words = [word.capitalize() for word in text.split()]

ints = [-1, -2, 0, 3, -4]
positives = [e for e in ints if e > 0]

letters = [letter for word in text.split() for letter in word if letter > 'l']

matrix = [list(range(x, x + 3)) for x in range(3)]

unique_letters = {letter for word in text.split() for letter in word if letter < 'o'}

alphabet = {index: letter for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz', 1)}

positives_gen = (e for e in range(100000000000000000000) if e > 0)
print(positives_gen)
print(next(positives_gen))

if __name__ == '__main__':
    print(positives)
    print(squares)
    print(words)
    print(letters)
    pprint.pprint(matrix, indent=1, width=15)
    print(alphabet)
    print(unique_letters)