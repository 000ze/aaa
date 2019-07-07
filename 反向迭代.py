list1 = [1, 2, 3, 4, 5]
for num1 in list1:
    print(num1, end=' ')
print('\n')
list1 = [1, 2, 3, 4, 5]
for num1 in reversed(list1):
    print(num1, end=' ')
print('\n')
a = iter(list1)
while 1:
    try:
        print(next(a), end=' ')
    except StopIteration:
        break
print('\n')
names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]
for name, age in zip(names, ages):
    print(name, age)
print(dict(zip(names, ages)))
'''import sys

print(sys.path)
from sys import *

print(version)
print(executable)'''


def _diamond_vip(lv):
    print('尊敬的钻石会员用户，您好:')
    vip_name = 'Diamond VIP' + str(lv)
    return vip_name


def _gold_vip(lv):
    print('尊敬的黄金会员用户，您好:')
    vip_name = 'Gold VIP' + str(lv)
    return vip_name


def vip_lv_name(lv):
    if lv == 1:
        print(_gold_vip(lv))
    elif lv == 2:
        print(_diamond_vip(lv))


vip_lv_name(1)


class Test(object):
    def prt(self):
        print(self)
        print(self.__class__)
        print(self.__module__)


t = Test()
t.prt()
