# coding:utf-8
# 计算器类，实现加减乘除


class Calculator:
    # 类的成员变量
    name = 'My Calculator'

    # 类的成员函数
    # 加法
    def add(self, x, y):
        print(self.name, '--add')
        return x + y

    # 减法
    def minus(self, x, y):
        print(self.name, '--minus')
        return x - y

    # 乘法
    def times(self, x, y):
        print(self.name, '--times')
        return x * y

    # 除法
    def divide(self, x, y):
        print(self.name, '--divide')
        return x / y


# 实例化计算器类
calculator = Calculator()
print(calculator.name)
sum = calculator.add(5, 8)
print('5+8=', sum)


class People:
    # 类变量 公共变量
    name = ''
    age = 0
    sex = '男'
    # 类变量 私有变量
    __site = 'www.xiaowangyun.com'

    # 构造函数 专有函数
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 公共函数获取私有变量
    def get_site(self):
        print('site:', self.__site)

    # 公共函数speak
    def speak(self):
        print('name:', self.name, ' age:', self.age, ' sex:', self.sex)

    # 私有函数speak
    def __speak(self):
        print('name:', self.name, ' age:', self.age, ' sex:', self.sex)


class Student(People):
    school = ''
    grade = ''

    # 派生类的构造函数
    def __init__(self, name, age, sex, school, grade):
        # 调用父类构造函数
        People.__init__(self, name, age, sex)
        self.school = school
        self.grade = grade

    # 重写父类speak方法
    def speak(self):
        print('I am a student. ', 'name:', self.name, ' age:', self.age, ' sex:', self.sex)


# Speaker 类
class Speaker():
    topic = ''
    name = ''

    def __init__(self, name, topic):
        self.name = name
        self.topic = topic


# StudentSpeaker 学生演说家 继承Speaker和Student类
class StudentSpeaker(Speaker, Student):
    temp = ''

    def __init__(self, name, temp, age, sex, topic, school, grade):
        Student.__init__(self, name, age, sex, school, grade)
        Speaker.__init__(self, name, topic)


ss = StudentSpeaker('小望云', '小望云', 2, '女', 'Python入门', 'CUMT', '88')
ss.speak()

# 实例化
xwy = Student('小望云', 2, '女', 'CUMT', '88')
xwy.speak()
xwy.get_site()
print(xwy.name)


# 类的实例化对象访问类的私有方法和私有属性会报错
# print(xwy.__site)
# xwy.__speak()


class Shape():
    name = ''

    def __init__(self, name):
        self.name = name

    def cal_area(self):
        print('我是动物，我会叫')


class Circle():
