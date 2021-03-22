import os
import time
#1 Файлы собираются в список, для имен содержащих пробелы -
# используем двойные кавычки
source = ['E:\\python']

target_dir = 'E:\\Backup'
#Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
#Текущее время служит именем зип архива
now = time.strftime('%H%M%S')
#Создаём каталог если его еще нет
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)
#Имя зип архива
target = today + os.sep + now + '.zip'
#Используем команду зип для помещения файлов в архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
#Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия создана успешно в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')