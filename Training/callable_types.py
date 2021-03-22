# def f():
#     print('Hello world')
# d = lambda :'hi'
# print(d())
# print(callable(d))

# class Cat:
#
#     def __call__(self, *args, **kwargs):
#         print('may')
#
#     def say_hello(self):
#         print('hello')
#
# bob = Cat()
# print(bob)
# print(callable(Cat))
# print(callable(bob))
# print(callable(bob.say_hello()))
# bob()

def f():
    n = 0
    while True:
        yield n
        n+=1
print(callable(f))