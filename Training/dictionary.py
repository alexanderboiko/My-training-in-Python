# a = [['moskva',495], ['piter',812], ['penza',8412]]
# d = {
#     #key:value,
#     'moskva': 495,
#     'piter' : 812,
#     'penza' :8412
# }
# r = dict(moskva=495, piter=812, penza=8412)
# t = dict(a)
# q = dict.fromkeys(['a', 'b', 'c'], 100)
# v = dict()
# print(v, type(v))

b = {}
d = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four'
}
print(d.items())
for key, value in d.items():
    print(key, value)
# for para in d.items():
#     print(para)

# print(d.values())
# for value in d.values():
#     print(value)
#print(d.keys())
# for key in d.keys():
#     print(key, d[key])

# print(d.get(1))
# d.setdefault(7,'seven')
# print(d.pop(2))
# print(d)

# person={}
# s = ' Ivanov Ivan Samara SGU 5 4 5 4 5 3 5 '
# s = s.split()
# person['lastname'] = s[0]
# person['first name'] = s[1]
# person['city'] = s[2]
# person['university'] = s[3]
# person['marks'] = []
# for i in s[4:]:
#     person['marks'].append(int(i))
# print(s)
# print(person)