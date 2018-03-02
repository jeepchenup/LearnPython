# -*- coding: utf-8 -*-

# 面向对象高级编程 - 使用__slots__
# __slots__ 给实例绑定属性或者方法
class Student(object):
    pass

s = Student()
s.name = "steven"
print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s) # 将set_age方法绑定到实例s上面，只对当前的实例起作用
s.set_age(25)
print(s.age)

# __slots__还可以给class绑定方法
def set_scroe(self, scroe):
    self.scroe = scroe

Student.set_scroe = MethodType(set_scroe, Student)
Student.set_scroe(2)
print(Student.scroe)

# 可以通过__slots__限制实例的属性

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Steven'
s.age = 25
# s.score = 99 # 这里会报错，因为Student类已经被限定属性绑定
# 但是Student的继承类定义score属性不会出错
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 1000

# 面向对象高级编程 - 使用@property
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# 通过上面的修改能够限制设置对Student实例的score属性的设置
s = Student()
s.set_score(60)
print(s._score, s.get_score())
# 但是这种写法是有缺陷的，我们可以通过直接对'_score'修改
s._score = 9999
print(s.get_score())

# @property的作用就是检查传入参数

class Student(object):

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0~100!")
        self._score = value
s = Student()
s.score = 60 # 实际转化为s.set_score(60)
print(s.score)
# s.score = 999 # 会报错

class Student(object):

    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self, value):
        self._birth = value
    
    @property
    def age(self):
        # age 属性只设置了读的方法
        return 2017 - self._birth

s = Student()
s.birth = 1993
print(s.age)
# s.age = 100 会报错

# 练习 - 使用@property
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen:

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
    
    @property
    def resolution(self):
        return self._width * self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

# 面向对象高级编程 - 定制类

# __str__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student objext(name: %s)' % self.name
print(Student('colin'))

# __iter__
# 用于迭代循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

# __getitem__
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a

print(Fib()[10])

# 判断切片
class Fib(object):

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        elif isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

f = Fib()
print(f[0:5])

# __getattr__

class Student(object):
    def __init__(self):
        self.name = "colin"

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

# 当调用一个不存在的属性的时候，在python的机制中会试图去调用__getattr__方法
s = Student()
print(s.name)
print(s.score) # 虽然初始化Student类时没有定义score属性，这个时候python会试图去调用__getattr__(self, 'score')

# 利用__getattr__，写一个链式调用
class Chain(object):

    def __init__(self, path=''):
        self.path = path
    
    def __getattr__(self, path):
        return Chain('%s %s' % (self.path, path))
    
    def __str__(self):
        return self.path
    
    __repr__ = __str__

print(Chain().status.user.timeline.list)

# __call__
# 一个对象可以有自己的属性和方法
class Student(object):
    def __init__(self, name):
        self.name = name
    
    def __call__(self):
        return ('My name is %s' % self.name)

s = Student('steven')
print(s())

# callable() 可以判断对象或者函数是否可调用自身
print(callable(Student('name')))
print(callable(max))
print(callable([1,2,3]))

# 面向对象高级编程 - 使用枚举类
from enum import Enum 
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum import Enum, unique

# Enum 默认从1开始计数，可以通过继承Enum来自定义
# @unique可以帮助我们检查保证没有重复值
from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(day1.value)
print(Weekday(1))

# 练习 - 枚举类
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：

from enum import Enum, unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('success')
else:
    print('fail')

# 面向对象高级编程 - 使用元类
# python是动态语言，这意味着函数和类的定义不是在编译时定义的，而是在运行时动态创建的
class Hello(object):
    def hello(self, name='word'):
        print('Hello, %s.' % name)
h = Hello()
h.hello()
print(type(Hello), type(h))