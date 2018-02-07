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

# 练习 - map/reduce(1)
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name[:1].upper() + name[:len(name)-1].lower()

# 测试
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 练习 - map/reduce(2)
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def m(x,y):
        return x*y
    return reduce(m, L)
# 测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 练习 - map/reduce(3)
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    L = []
    dotIdx = s.find('.')
    digits = {'0':0,  '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def mult(x,y):
        return x*10 + y

    for ch in s:
        if ch == '.':
            continue
        L.append(digits[ch])

    integer = reduce(mult, L)
    n=0
    while n<dotIdx:
        integer /= 10
        n += 1
    return integer
# 测试
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

# 高阶函数 - filter
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是Flase决定保留还是丢弃元素

# Example 1
# 在一个list中，删掉偶数，只保留基数
L = [1,2,3,4,5,6,7,8,9]
print(L[::2])  # 用切片实现
def is_odd(n): # 用filter实现
    return n % 2 == 1
print(list(filter(is_odd, L)))

# Example 2
# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))

# Example 3
# 获取素数
def _odd_iter(): # 定义一个素数生成器
    n = 1
    while True:
        n = n+2
        yield n
def _not_divisible(n): # 定义一个筛选函数
    return lambda x: x%n > 0
def primes(): # 定义一个生成器，不断返回下一个素数
    yield 2
    it = _odd_iter() # 初始化序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)
for n in primes():
    if n<1000:
        print(n)
    else:
        break

# 练习 - filter
# 筛选回数
def is_palindrome(n):
    return str(n) == str(n)[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# 高阶函数 - sorted
print(sorted([36,5,-12,9,-21]))

# sorted()函数还可以接收一个key函数来实现自定义的排序
# Example 1, 按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# Example 2, 忽略大小写的排序
print(sorted(['bob','about','Zoo','Credit'], key=str.lower))

# Example 3, 降序
print(sorted(['bob','about','Zoo','Credit'], key=str.lower, reverse=True))

# 练习 - sorted()
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
print(sorted(L, key=by_name))
def by_sore(t):
    return t[1]
print(sorted(L, key=by_sore))

# 函数式编程 - 返回函数
# 将函数作为结果值返回

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f())

# 练习 - 返回函数
# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    sum = 0
    def counter():
        nonlocal sum
        sum += 1
        return sum
    return counter
# 测试
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# 函数式编程 - 匿名函数
# lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
f = lambda x: x*x
print(f(5))

# 可以将匿名函数作为返回值返回
def build(x,y):
    return lambda: x*x + y*y

# 练习 - 匿名函数
# 匿名函数改造下面的代码
def is_odd(n):
    return n%2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L)

L = list(filter(lambda n: n%2 == 1, range(1,20)))
print(L)

# 函数式编程 - 装饰器
# 函数对象有一个__name__属性，可以获取函数的名字
def now():
    print('2018-02-06')
print(now.__name__)

# 定义一个装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 使用装饰器
@log
def now():
    print('2018-02-06')
now()

# 自定义log的文本
def log(txt):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (txt, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2018-02-06')
now()

# functools.wraps
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*arg, **kw)
    return wrapper

# 练习 - 装饰器
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time
def metric(func):
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (func.__name__, time.strftime('%Y-%m-%d',time.localtime(time.time()))))
        return func(*args, **kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功！')