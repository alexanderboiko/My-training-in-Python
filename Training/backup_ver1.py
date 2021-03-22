import os
import time

#1Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['E:\\python', 'D:\\Drivers']
#для имен с пробелами нужно использовать двойные кавычки

#2резервные копии должны хранится в основном каталоге резерва
target_dir = 'E:\\Backup'
#3файлы помещаються в архив
#4именем архива служит текущая дата и время
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#5используем команду зип  для помещения файлов в зип архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

#запускаем создание резервной копии
if os.system(zip_command) == 0:
	print('Резервная копия успешно создана в', target)
else:
	print('Создание резервной копии НЕ УДАЛОСЬ')