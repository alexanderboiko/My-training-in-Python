print('Give me two numbers, and I + them')
print("enter 'q' to quit")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    try:
        answer = int(first_number)+int(second_number)
    except ValueError:
        print("Вводите только цифры!")
    else:
        print(answer)