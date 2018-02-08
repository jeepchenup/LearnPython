# -*- coding: utf-8 -*-

# 面向过程编程
std1 = {'name': 'Steven', 'score': 99}
std2 = {'name': 'Bob', 'score': 80}

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
print_score(std1)
print_score(std2)

# 面向对象编程
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# 面向对象编程 - 类和实例

# 定义一个类是通过class关键字
class Engineer(object):
    
    # __init__方法，就相当于Java中的构造函数
    # 如果没有显示的定义__init__方法，在初始化一个Engineer对象的时候可以不传参数
    # 但是Engineer中，定义了__init__方法，那么初始化一个Engineer对象的时候，必须得传入__init__方法的参数除了`self`
    def __init__(self, name, skill):
        self.__name = name   #私有变量 __name
        self.__skill = skill #私有变量 __skill

    # 数据封装
    def print_skill(self):
        print('%s: %s' % (self.__name, self.__skill))

    # 允许外部访问内部属性
    def get_name(self):
        return self.__name
    
    def get_skill(self):
        return self.__skill

    # 允许外部修改内部属性
    def set_name(self, name):
        self.__name = name
    
    def set_skill(self, skill):
        self.__skill = skill

steven = Engineer('Steven', 'java/python/js')
print(steven, Engineer)
steven.skill = 'java/python/js'
print(steven.skill)
steven.print_skill()

# 面向对象编程 - 访问限制
# 让内部属性不被外部访问，可以把属性的名称前加两个下划线__
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量，只有内部可以访问

# 练习 - 访问限制
class Student(object):
    
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        self.__gender = gender

# 测试
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

# 面向对象编程 - 继承和多态
class Animal(object):
    def run(self):
        print('Animal is running ... ...')

class Dog(Animal):
    def run(self):
        print('Dog is running wawawa')

class Cat(Animal):
    def run(self):
        print('Cat is running miaomiaomiao')

dog = Dog()
cat = Cat()
dog.run()
cat.run()

# 多态
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

# 面向对象编程 - 获取对象信息
# 获取对象信息 - type()
# 判断对象类型 - isinstance()
print(type(123))
print(type('123'))
print(type(None))
print(type(abs))
print(type(Animal()))
print(isinstance([1,2,3], (list, tuple)))
print(isinstance((1,2,3), (list, tuple)))

# dir() - 获取对象的所有属性和方法
print(dir('ABC'))
print(dir(hasattr))

# 面向对象编程 - 实例属性和类属性
# 实例属性就是对象创建出来的时候才初始化的属性，具有独特性
# 类属性不需要创建实例就已经存在的

# 练习 - 实例属性和类属性 
# 为了统计学生人数，可以给Student类增加一个类属性，没创建一个实例，该属性自动增加
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1
# 测试
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')