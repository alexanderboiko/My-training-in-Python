
# g = 'grey'
# def colors(param ='r'):
#
#     y = 'yellow'
#     g = 'green'
#     def red():
#         nonlocal y
#         r = 'red'
#         print(r,y, g)
#         y = 'was changed'
#
#     def blue():
#         b = 'blue'
#         print(b,y,g)
#
#     if param =='r':
#         red()
#     elif param =='b':
#         blue()
#     else:
#         print(' I do not know this color')
#
#     red()
#     blue()
# colors()

g = 'grey'
def colors(param ='r'):

    y = 'yellow'
    g = 'green'
    def red():
        r = 'red'
        print(r)

    def blue():
        b = 'blue'
        print(b)

    if param =='r':
        red()
    elif param =='b':
        blue()
    else:
        print(' I do not know this color')


colors('g')