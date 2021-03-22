print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist #mylist еще одно имя, указывающее на тот же обьект

del shoplist[0]#я сделал первую покупку и удяляю её из списка

print('shoplist:', shoplist)
print('mylist:', mylist) 
# shoplist, mylist выводят один и тот же список без пункта яблоко, указывая на один и тот же обьект

print('Копирование при помощи полной вырезки')
mylist = shoplist[:] #создаем копию путем полной вырезки
del mylist[0] #удаляем первый элемент

print('shoplist:', shoplist)
print('mylist:', mylist)
#обратите внимание, что теперь списки разные