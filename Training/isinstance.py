# isinstance

s_strok = ''
s_list = []
s_numbers = 0
a = [5, 3, 'hello', [3, 4], ' world', [5], 10.5]
for i in a:
    if isinstance(i,str):
        s_strok = s_strok + i
    elif isinstance(i,list):
        s_list = s_list +i
    elif isinstance(i,(int, float)):
        s_numbers = s_numbers +i

print(s_strok)
print(s_list)
print(s_numbers)
