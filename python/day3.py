# -*- coding: utf-8 -*-

# 高阶函数 - map/reduce

# 通过map()实现f(x) = x * x
def f(x):
    return x * x
r = map(f, [1,2,3,4,5,6,7,8,9])
print(list(r))

# 将数组里面的元素全部转换成字符串
print(list(map(str, [1,2,3,4,5,6,7,8,9])))

# reduce
# reduce(f, [x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
from functools import reduce
def add(x,y):
    return x+y
print("sum:",reduce(add,[1,2,3,4,5,6,7,8,9]))

# 将list元素转换成整数
def fn(x,y):
    return x*10+y
print("integer:", reduce(fn, [1,2,3,4]))

# 将str转换成int
def char2num(s):
    digits = {'0':0,  '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(char2num, '12345'))) 

# 练习 - map/reduce
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name[:1].upper() + name[:len(name)-1].lower()

# 测试
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)