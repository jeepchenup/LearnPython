#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

print('hello, python!')

# 遇到都到会输出一个空格
print('The quick brown fox', 'jumps over', 'the lazy dog')

# 输出表达式结果
print('100 + 200 = ', 100+200)

# 输入
name = input('please enter your name:')
print('hello',name)

# 转义字符
print("I\'m ok.")

# r'' 表示''内部的字符串默认不转义
print(r'\\\t\\')

# \n换行
print("line1\nline2\nline3")

# 布尔值
print(True,False)

# and & or & not
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(not True)
print(not False)

# 变量名必须是大小写英文、数组和_的组合，且不能用数字开头
a = 1
_a = 2

# 除法的结果是浮点数
print(10/3)

# 取整除法
print(10//3)

# 取余
print(10%3)

# ord()函数获取字符的整数表示
print(ord('A'),ord('中'))

# chr()函数把编码转换为对应的字符
print(chr(65),chr(20013))

# 当数据涉及到要在网络上传输，或者保存到磁盘上面的时候，需要将string变成以字节单位的bytes
# 带b前缀的单引号或者双引号表示，同时引号内的每一个字符都占一个字节
x = b'ABC' 
print(x)

# encode()方法可以通过传入指定的编码，来编码成bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# decode()方法可以通过传入指定的编码，来吧bytes转成string
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 计算[string | bytes]的长度
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

# 格式化 %
# 不确定使用什么类型转换，%s永远起作用，它会把任何数据类型转换为字符串
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 100000))

# %%表示%
print('growth rate: %d %%' % 7)

# 格式化 format()方法
print('Hello, {0}, 成绩提升了 {1:.1f}%, {2:.2f}'.format('小明', 17.125, 17.125))

# 练习
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
r = (85-72)/72
print(r)
print('小明的成绩提升了%.1f %%' % r)

# 数组
classmates = ['Michael', 'Bob', 'Tracy']

# 读取数组最后一个元素
print(classmates[len(classmates)-1])
print(classmates[-1])

# 在数组后面添加元素
classmates.append('Adam')
print(classmates)

# 删除数组末尾的元素
classmates.pop()
print(classmates)

# 删除指定的元素
classmates.pop(1)
print(classmates)

# 赋值元素到指定的下标
classmates[1] = 'Sarah'
print(classmates)

# 把元素插入到指定的位置
classmates.insert(1, 'Jack')
print(classmates)

# 元组tuple
# 一旦初始化了就不能修改
classmates = ('Michael', 'Bob', 'Tracy')

# list & tuple练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple
print(L[0][0])
# 打印Python
print(L[1][1])
# 打印Lisa
print(L[2][2])

# 判断语句
age = 3
print('your age is', age)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 判断练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
bmi = 80.5/(1.75*1.75)
if bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过瘦')

# for...in循环
names = ['Michael', 'Bob', 'Traacy']
for name in names:
    print(name)

# while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n-2
print(sum)

# 练习循环
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
# L = ['Bart', 'Lisa', 'Adam']
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello, %s!' % name)

# 跳出循环 break
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n+1
print('END')

# 跳过当前这次循环 continue
n = 0
while n < 10:
    n = n + 1
    if n%2 == 0:
        continue
    print(n)

# dict | => map
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 判断key是否存在dict中 => in
print('Michael' in d)
print('Steven' in d)

# 判断key是否存在dict中 => get
print(d.get('steven', 'steven 不存在'))

# 删除dict中的key-value
print(d.pop('Bob'))

# Set
# 要创建一个Set需要传入一个list作为输入集合
# set中没有重复的key
s = set([1,2,3])
print(s)

# 重复的元素在set中自动被过滤
s = set([1,1,2,2,3,3])
print(s)

# 添加元素到set
s.add(4)
print(s)

# 删除set中的元素
s.remove(4)
print(s)

# 对两个Set做交集，并集 => &, |
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)

# str是不可变对象
a = 'abc'
print(a.replace('a', 'A'))
print(a)

print(hex(255), hex(1000))

# 自定义函数
def my_abs(x):
    if x>= 0:
        return x
    else:
        return -x
print(my_abs(-1))

# 定义一个空的函数
def nop():
    pass

# 重定义my_abs，只允许int，float参数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# print(my_abs('s'))
print(my_abs(-2))

# 定义一个计算次方函数
# 必选参数在前，默认参数在后
# 默认参数必须指向不变对象，不然多次调用之后默认值会被修改
def power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s
print(power(2))
print(power(2,4))

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())

# 定义一个可变参数的函数
def calc(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + power(num)
    return sum
print(calc(1,2))

def person(name, age, **kw):
    print('name:', name, "age:", age, "other:", kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city':'Beijing', 'job':'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)

# 练习
def product(*args):
    sum = 1
    for arg in args:
        sum = sum * arg
    return sum

print(product(1,2,3,4,5,6))