# name = 'Семен'
# mid_name = 'Семенович'
# balance = 20.23

# # text = f"""Дорогой {name} {mid_name}, баланс вашего счета {balance}"""
# # print(text)
# text = f"""Дорогой {name.lower()} {mid_name.upper()},
# # баланс вашего счета {balance*2}"""
# print(text)

# d = {
# 'name': 'Семен',
# 'mid_name': 'Семенович',
# 'balance': 20.23
# }
# text = f"""Дорогой {d['name']} {d['mid_name']}, баланс вашего счета {d['balance']}"""
# print(text)

g = {
    'm': 'Дорогой',
    'f': 'Дорогая',
}
a = [
    ['Semen', 'Semenovich', 21.3, 'm'],
    ['Tamara', 'Lvovna', 32.54, 'f'],
    ['Petro', 'Olexeevich', 11.23, 'm'],
]
for name, mid_name, balance, gender in a:
    text = f"""{g[gender]} {name} {mid_name}, баланс вашего счета {balance}"""
    print(text)
