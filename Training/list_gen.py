squares = [e * e for e in range(10) if e % 2 == 0]

text = "hello world"
words = [word.capitalize() for word in text.split()]

ints = [-1, -2, 0, 3, -4]
positives = [e for e in ints if e > 0]

if __name__ == '__main__':
    print(positives)
    print(squares)
    print(words)