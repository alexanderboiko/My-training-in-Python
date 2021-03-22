# import math

# n = 10
# m = 15
# d = math.ceil(m/n)
# print(d)

# a = int(input())
# b = int(input())
# n = int(input())
# cost = n * (100 * a + b)
# print(cost // 100, cost % 100)

# s = int(input())
# print(s+2-(s%2))

# n = int(input())
# hours = n % (60 * 24) // 60
# minutes = n % 60
# print(hours, minutes)

# s = input()
# print(s.count(' ')+1)

# a = 'Bilbo.Baggins@bagend.hobbiton.shire.me'
# print(a.replace('@',''))

# a = input()
# print('*'.join(a))

# s = input()
# vowels = ['a', 'e', 'i', 'o', 'u', 'y']  # Letters to filter out
# s = s.lower()  # Convert string to lower case

# for vowel in vowels:
# s = s.replace(vowel, ""), '.'.join(s)
# print(s)

# a,b = map(int,input().split())
# c,d = map(int,input().split())
# if b==d or a==c:
#   print("Yes")
# else:
#   print("No"if b==d or a==c:
#  print("Yes")
# else:
#   print("No")
# 1 2 3 4 5  || 6 7

# n = 15
# a = 1
# while a<=n:
#   b = a*a
#  if b<=15:
#     print (b)
# a=a+1

# a=[54, 6456, 5636, 6456,666538]
# while len(a)>0:
#   last=a.pop()
#  if last %2!=0:
#     print('no', last)
#    break
# else:
#   print('yes')

# for i in range(1, 11):
#   print(i, i**2)

# s=0
# for i in range(10,100):
#   s=s+i
# print(s)

# n = int(input())
# pr = 1
# for i in range(1,n+1):
#   pr=pr*i
# print(pr)

# from random import randint
# s=0
# for i in range(10):
#   a = randint(1,10)
#  s+=a
# print(a, end=" ")
# print()
# print(s)

# for i in range(1,11):
#  print('*'*i)

# n=int(input())
# s=0
# for i in range(n):
#   a=int(input())
#  s+=a
# print('current s:', s)
# print('total', s)
# print('sredn arifmet=', s/n)

# a = [43, 65, 3, 43, 6, 567, 564,321]
# n = len(a)
# for i in range(n):
#   print(i, a[i])
#  a[i] +=5
# print(a)

# a =[1,2,3,4,32,4,5,3,5]
# b = []
# for i in a:
#   if not i in b:
#      b.append(i)
# print(b)

# a =[1,2,3,4,32,4,5,3,5]
# chet = []
# nechet = []
# n= len(a)
# for i in range(n):
#   if a[i]%2==0:
#      chet.append(i+1)
# else:
#    nechet.append(i+1)
# print(chet)
# print(nechet)

# s ='helLo WOrld'
# for i in s:
#   if i>='a' and i<='z':
# elif 'A'<=i<='Z':
#     print(i, 'BIG')
# else:
#   print(i)

# vowels = 'aeiou'
# s = 'aertiooikjoaikl'
# n = len(s)
# for i in range(n-1):
#     if s[i] in vowels and s[i+1] in vowels:
#         print(s[i], s[i+1])

# a = [3, 4, 3, 3, 5, 4, 6, 3]
# while 3 in a:
#     a.remove(3)
# print(a)

# import math
# a = 20
# b = 21
# c = 22
# d = math.ceil((a+b+c)/2)
# print(d)

# import calendar
# c = calendar.TextCalendar()
# print(c.formatyear(2021))
# 1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)
# 2
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# elem for elem in a if elem in b:
#     # if elem in a if elem in b:
#         print(elem)


# c = [elem for elem in a if elem in b]
# print(c)
# result = list(filter(lambda elem: elem in b, a))
# print(result)

# pizzas = ['paperoni', 'mozarella', '4 cheeze', 'hot']
# for pizza in pizzas:
#     print(f"I like {pizza.title()} pizza.\n")
# print('I really love pizza!')

# numbers = [i*1 for i in range(1,1000001)]
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# for i in range(1, 30):
#     if i % 3 == 0:
#         print(i)

# qube = [value ** 3 for value in range(1, 11)]
# print(qube)
#
# for i in range(1, 11):
#     print(i ** 3)

# sandwich_orders = ['mokko','pastrami', 'kokko', 'pocco','pastrami', 'rocco', 'pastrami']
# finished_sandwiches = []
# print("pastrami ends")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# while sandwich_orders:
#     processing_order = sandwich_orders.pop()
#     print("I made your" + " " + processing_order + " " + "sandwich")
#     finished_sandwiches.append(processing_order)
# for finish_sandwich in finished_sandwiches:
#     print(finish_sandwich.title() + " is done")

# holidays = {}
# active = True
#
# while active:
#     name = input("\nWhat is your name? ")
#     holiday = input("\nWhere do you want spend your holidays? ")
#
#     holidays[name] = holiday
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         active = False
#
# print("\n ____Results____")
# for name, holiday in holidays.items():
#     print(name+ " would like to spend "+ holiday)

# active = True
# while active:
#     age = input("Enter your age: ")
#     if age == "exit":
#         active = False
#     elif int(age) < 3:
#         print("Your price free")
#     elif 3 <= int(age) < 12:
#         print("your price 10")
#     elif int(age) >= 12:
#         print("Your price 15")

# i = 0
# while True:
#     i += 1
#     if i == 100:
#         break
#     print(i)

# def make_shirt(size='L', text='I love Python'):
#     print('\nI have a ' + size +" " + text)
# make_shirt('s', 'jhh')

# def describe_city(city, country='Ukraine'):
#     print(city + ' is in '+ country)
# describe_city('Kyiv')

# def city_country(city, country):
#     a = city + ", " + country
#     return a.title()
# b = city_country('kyiv', 'ukraine')
# print(b)

# def make_album(name, album_name):
#     album = {1: name, 2: album_name}
#
#     return album
#
#
#
#
# while True:
#     print('\nВведите альбом, или для выхода q:')
#     name1 = input('enter name:')
#     if name1 == 'q':
#         break
#     name2 = input('enter album:')
#     if name2 == 'q':
#         break
#
#     mag = make_album(name1, name2)
#
#     print(mag)

# def make_sandwich(*components):
#     print("\n making sandwich with: ")
#     for component in components:
#         print("- " + component)
# make_sandwich('big', 'paperoni', 'sugar', 'becon')

def make_car(brand, model, **parameters):
    car = {}
    car['brand_name'] = brand
    car["model_name"] = model
    for key, value in parameters.items():
        car[key] = value
    return car

car1 = make_car('subaru', 'outback', color='green', tow_packadge=True)
car2 = make_car('bmw', '325I', color='yellow')
print(car1)
print(car2)

