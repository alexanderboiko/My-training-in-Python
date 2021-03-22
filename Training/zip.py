import os
import time
import zipfile
#1Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['E:\\python',]
#для имен с пробелами нужно использовать двойные кавычки

#2резервные копии должны хранится в основном каталоге резерва
target_dir = 'E:\\Backup'
#3файлы помещаються в архив
#4именем архива служит текущая дата и время
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#5используем команду зип  для помещения файлов в зип архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

#запускаем создание резервной копии
my_zip = zipfile.ZipFile(source, 'w')
my_zip.write(target, compress_type=zipfile.ZIP_DEFLATED)
my_zip.close()