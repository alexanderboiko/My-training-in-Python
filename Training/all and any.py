# a = ['hello', '', 'world']
# # print(all(a))
# # print(any(a))
a = 100
con_1 = a%2==0
con_2 = a>50
con_3 = a<1000
print(all([con_1,con_2,con_3]))
print(any((con_1,con_2,con_3)))

