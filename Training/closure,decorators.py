#Замыкания
# def main_func():
#
#     def inner_func():
#         print(('hello my friend'))
#     inner_func()
#
# main_func()

#декораторы
def header(func):

    def inner(*args,**kwargs):
        print('h1')
        func(*args,**kwargs)
        print('/h1')

    return inner

def table(func):
    def inner(*args,**kwargs):
        print('table')
        func(*args,**kwargs)
        print('/table')

    return inner
@header #say = header(say)
@table
def say(name, surname, age):
    print('hello', name, surname, age)


say('Vania', 'Ivanov', 32)