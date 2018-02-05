# -*- coding: utf-8 -*-

# 递归函数
def fact(n):
    if n==1:
        return 1
    return n* fact(n-1)
print(fact(10))

# 尾递归优化，解决内存溢出
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num * product)
print(fact(10))

# 高级特性-切片

# 获取list前3个元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
# 如果第一个索引是0，则可以省略写成下面这种方式
print(L[:3])

# L[a:b:c] 从list L中，从下标为a，开始取前b个数，每隔c个数，取一个数，从a下标开始计算
L = list(range(100))
print(L[1:10:3])

# tuple也是一种list，唯一区别是tuple不可变。
print((0,1,2,3,4,5)[:3])

# 字符串也可以被看成一种list
print('ABCDEF'[:3])

# 高级特性-迭代

# 输出的顺序不一定是按照 a,b,c
# 因为dict的储存不是按照list的方式顺序排列
d = {'a': 1, 'b':2, 'c':3}
for key in d:
    print(key)

# 迭代输出value
for value in d.values():
    print(value)

# 迭代输出key - value
for k,v in d.items():
    print(k,"-",v)

# 迭代输出字符
for chart in 'ABC':
    print(chart)

# 只要isinstance(Object, Iterable) 返回的值为True的对象就可以被迭代
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

# 获取list下标
for i, value in enumerate(['A','B','C']):
    print(i,'-',value)

for x, y in [(1,1), (2,4), (3,9)]:
    print(x,y)

# 练习
# 查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if(len(L) == 0):
        return (None, None)
    elif(len(L) == 1):
        return (L[0], L[0])
    else:
        for i, value in enumerate(L):
            j = i+1
            for j, value in enumerate(L):
                if(L[i]>L[j]):
                    temp = L[i]
                    L[i] = L[j]
                    L[j] = temp
        return (L[len(L)-1], L[0])
# 检测
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 高级特性 - 列表生成式

print(list(range(1,11)))

# 生成[1*1,2*2,...,10*10]
L = []
for v in range(1,11):
    L.append(v * v)
print(L)

# 简化写法
print([v*v for v in range(1,11)])

# 筛选出仅偶数的平方
[print([v*v for v in range(1,11) if v % 2 == 0])]

# 两层循环
print([n+m for n in 'ABC' for m in 'XYZ'])

# 列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])

d = {'x':'A', 'y':'B', 'z':'C'}
print([k + '=' + v for k, v in d.items()])

# 把list中所有的字符串变成小写
L = ['Hello', 'World']
print([s.lower() for s in L])

# 练习
L = ['Hello', 'World', 18, 'Apple', None]
def toLower(L):
    return [s.lower() for s in L if isinstance(s, str)]
L2 = toLower(L)
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# 高级特性 - 生成器
# 生成器的存在就是为了防止内存溢出
g = (x * x for x in range(10))
print(isinstance(g, Iterable))

# 迭代生成器
for n in g:
    print(n)

# 斐波拉契数列
def fib(max):
    n, a, b = 0,0,1
    while n < max:
        print(b)
        a, b = b, a+b # 赋值语句
        n = n+1
    return 'done'
fib(6)

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'
for n in fib(6):
    print(n) # 这样是捕获不到return语句返回的'done'

# 修改成下面的写法
def readGenerator(g):
    while True:
        try:
            x = next(g)
            print('g:', x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break
readGenerator(fib(6))

# 练习 - 打印出杨辉三角
def triangles():
    n = 0
    M = [1]
    L = [1]
    while True:
        yield(L)
        n += 1
        if n == 1:
            L = [1,1]
        elif n>=2:
            L = [1]
            for i in range(1,n):
                L.append(M[i-1] + M[i])
            L.append(1)
        M = L

# 测试
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

# 高级特性 - 迭代器
# 可以被next()函数调用并不断返回下一个值的对象被称为迭代器: Iterator
# 可以通过isinstance()判断一个对象是否是Iterator对象
# 生成器都是Iterator对象
# list、dict、str虽然是可迭代的，但是不是Iterator对象

from collections import Iterator
print(isinstance([], Iterator)) # list
print(isinstance({}, Iterator)) # dict
print(isinstance('ABC', Iterator)) # str

# 可以通过iter()函数将list、dict、str等可被迭代的对象转换成Iterator对象
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('ABC'), Iterator))