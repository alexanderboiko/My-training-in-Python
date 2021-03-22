

# def f():
#     return [43,65,32]
# def genf():
#     for i in [43,65,32]:
#         yield i
# for i in genf():
#     print(i)

def fact(n):
    pr=1
    for i in range(1, n+1):
        pr = pr*i
        yield pr
for i in fact(10):
    print(i, end= ' ')