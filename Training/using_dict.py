# 'ab' сокращение от address book
ab = {  'Swaroop'  : 'swaroop@swaroopch.com',
        'Larry'    : 'larry@wall.org' ,
        'Matsumoto': 'matz@ruby-lang.org',
        'Spammer'  : 'spammer@hotmail.com'
     }
print("Адрес Swaroop'a:", ab['Swaroop'])

#удаление пары ключ-значение

del ab['Spammer']

print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

for name, address in ab.items():
	print('контакт {0} с адресом {1}'.format(name, address))

#добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
	print('\nАдрес Guido:', ab['Guido'])