# -*- coding: utf-8 -*-

# 错误处理
# python里面封装了一个try的机制
try:
    print("try...")
    r = 10/0
    print("result:", r)
except ZeroDivisionError as e:
    print("except:", e)
finally:
    print('finally...')
print('END')

# except能捕获不同类型的错误
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

#如果没有错误发生，可以在except语句块后面加一个else
try:
    print('try...')
    r = 10/int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10/n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('Error!!',e)
        # raise
bar()

# 练习
from functools import reduce

def str2num(s):
    try:
        num = int(s)
    except ValueError:
        num = float(s)
    return num

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

# 调试
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n

# def main():
#     foo('0')
# main()

# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

s = '0'
n = int(s)
print(10 / n)