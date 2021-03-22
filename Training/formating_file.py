name = 'Семен'
mid_name = 'Семенович'
balance = '20.23'

# text = """Дорогой {0} {1}, баланс вашего счета {2}""".format(name,mid_name,balance)
# print(text)
text = """Дорогой {n} {m},
баланс вашего счета {b}""".format(n=name,m=mid_name,b=balance)
print(text)