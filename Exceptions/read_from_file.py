filename = 'learning_python.txt'

with open(filename) as file_object:
    # contents = file_object.read()
    # print(contents)
    # for line in file_object:
    #     print(line.rstrip())
    lines = file_object.readlines()

    for line in lines:
        print(line.replace('Python', 'C').rstrip())