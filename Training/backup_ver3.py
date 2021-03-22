import os
import time

source = ['E:\\python']

target_dir = 'E:\\Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')
#Запрашиваем коментарий пользователя для имени файла
comment = input('ВВедите коментарий-->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)

zip_command = "zip -gr {0} {1}". format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')