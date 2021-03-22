filenames = ['cats.txt', 'dogs..txt']

for filename in filenames:
    try:
        with open(filename) as f_obj:
            contends = f_obj.read()
    except FileNotFoundError:
        pass
        # print('Файл ' + filename+ ' не найден')
    else:
        print(contends)