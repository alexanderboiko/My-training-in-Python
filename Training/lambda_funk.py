heroes = {
    'Spider-Men': 80,
    "Batman": 65,
    "Supermen": 85,
    "Wonder Woman": 70,
    "Flash": 70,
    "Iron man": 65,
    "Thor": 90,
    'Aquaman': 65,
    "Capitan America": 65,
    'Hulk': 87,
}
# for i in sorted(heroes.items(), key=lambda para: (para[1], para[0])):
#     print(i)

# для списков сортировка
# heroes.sort(key= lambda x: x.split(' ')[-1])
# print(heroes)

f = lambda x: 'Like' if x > 100 else 'Subscribe'
# print(f(200))
d = lambda x: 'Like' if x > 100 else ('Subscribe' if x > 0 else 'Follow me')
print(d(0))
