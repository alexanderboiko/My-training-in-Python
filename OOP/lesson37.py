# инструкция raise

# try:
#     [1,2,3][15]
# except (KeyError, IndexError) as error:
#     print('LookupError')
#     print(f"Logging error: {error} {repr(error)}")
# except ZeroDivisionError as err:
#     print('ZeroDivisionError')
#     print(f"Logging error: {err} {repr(err)}")

# raise Exception('Big error')

# try:
#     [1, 2, 3][15]
# except (KeyError, IndexError) as error:
#     print(f"Logging error: {error} {repr(error)}")
#     raise TypeError('Ошибка типа') from None
# except ZeroDivisionError as err:
#     print('ZeroDivisionError')
#     print(f"Logging error: {err} {repr(err)}")

try:
    raise ValueError('ошибка значения')
except ValueError as first:
    try:
        raise TypeError('Ошибка типа')
    except TypeError as second:
        raise Exception('Большое исключение') from None
