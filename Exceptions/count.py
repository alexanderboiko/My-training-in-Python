filename = 'earth.txt'
with open(filename) as f_obj:
    contents = f_obj.read()
    words = contents.lower()

    print(words.count('the'))