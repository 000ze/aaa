# 1、字符创创建迭代器对象
str1 = 'liangdianshui'
iter1 = iter(str1)

# 2、list对象创建迭代器
list1 = [1, 2, 3, 4]
iter2 = iter(list1)

# 3、tuple(元祖) 对象创建迭代器
tuple1 = (1, 2, 3, 4)
iter3 = iter(tuple1)

# for 循环遍历迭代器对象
for x in iter2:
    print(x, end=" ")

print('\n------------------------')

# next() 函数遍历迭代器
while True:
    try:
        print(next(iter1), end=" ")
    except StopIteration:
        break

print('\n')
# list生成器对象
# -*- coding: UTF-8 -*-
lsit1 = [x + x for x in range(1, 11)]
print(lsit1)
lsit2 = ['%dx%d=%2d' % (x, y, x * y) for x in range(1, 11) for y in range(1, 11) if x % 2 == 0 if y % 2 == 0]
print(len(lsit2))
print(lsit2)
x = 1
y = 2
print('%dx%d=%3d' % (x, y, x * y))
gen = (x * x for x in range(10))
print(gen)
for num in gen:
    print(num, end=" ")
print('\n')


def my_function():
    for i in range(10):
        print(i, end=" ")


my_function()


def my_function2():
    for i in range(10):
        yield i


print(my_function2())


def odd():
    print('step 1')
    yield (1)
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()
print(o)
print(next(o))
print(next(o))
print(next(o))


# -*- coding: UTF-8 -*-
def triangles( n ):         # 杨辉三角形
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [ L [ i -1 ] + L [ i ] for i in range (len(L))]

n= 0
for t in triangles( 10 ):   # 直接修改函数名即可运行
    print(t)
    n = n + 1
    if n == 10:
        break

# print('\n'.join([' '.join('%dx%d=%2d' % (x, y, x * y) for x in range(1, y + 1)) for y in range(1, 10)]))
