
# Обработка исключений
s = 'hello'
try:
    s[6]

except IndexError:
    print('IndexError')

else:
    print('good')
finally:
    print('end')