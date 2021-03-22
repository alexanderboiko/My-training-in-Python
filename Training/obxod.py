# import os
#
# path = 'E:\\python'
# print(os.listdir(path))
# for i in (os.listdir(path)):
#     print(i, type (i), path+'\\'+i, os.path.isdir(path+'\\'+i))

import os
path ='E:\\Backup'
def obxodFile(path, level=1, name='Новая папка'):
    print('Level=',level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            print('Заходим', path +'\\'+i)
            obxodFile(path+'\\'+i,level+1)
            print('Возвращаемся в', path)
        if name == name:
            print(path+'\\'+name)
obxodFile(path)