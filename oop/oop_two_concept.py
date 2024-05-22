# del keyword : to delete

class Student:

    def __init__(self, name):
        self.name = name

s1 = Student('hella')
print(s1.name)
del s1.name
# print(s1.name)


# private attribute and methods using two underscore in attribute and methods
# in order to hide
# public attribute
class Account:
    def __init__(self, acc_no, acc_pwd):
        self.acc_no = acc_no
        self.acc_pwd = acc_pwd

acc1 = Account(234,'53ff')
print(acc1.acc_pwd, acc1.acc_no, '\n')

# private attribute using two underscore
class Account:
    def __init__(self, acc_no, acc_pwd):
        self.acc_no = acc_no
        self.__acc_pwd = acc_pwd

    def reset_pwd(self, val):
        self.__acc_pwd = val
        print("your new pwd is", self.__acc_pwd)

    def __dear_user(self, name):
        print('hello ', name)

    def greet(self, name):
        self.__dear_user(name)

acc1 = Account(234,'53ff')
# print(acc1.__acc_pwd, acc1.acc_no)
acc1.reset_pwd('dd33')
# acc1.__dear_user()
acc1.greet('arri')


# class method
# receives the class as implicit first argument

# class Person:
#     name = "Anonymous"

#     def changeName(self, name):
#         self.name = name

# p1 = Person()
# p1.changeName("rahul")
# print(p1.name)

# to change the name attribute of class
class Person:
    name = "Anonymous"

    # def changeName(self, name):
    #     Person.name = name
        # or
        # self.__class__ = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("rahul")
print(p1.name)
print(Person.name)


# property decorator
# when an attribute value is depend on function
class Student:

    def __init__(self, a_mark, b_mark, c_mark):
        self.a_mark = a_mark
        self.b_mark = b_mark
        self.c_mark = c_mark

    # normal way
    # def calculate_percentage(self):
    #     self.percent = str((self.a_mark + self.b_mark + self.c_mark) / 3) + "%"

    # property way
    # the percent method is return as an attribute or a variable of the obj s1.
    @property
    def percent(self):
        return str((self.a_mark + self.b_mark + self.c_mark / 3)) + "%"

s1 = Student(98, 97, 99)
s1.a_mark = 110
# s1.calculate_percentage()
print(s1.percent)