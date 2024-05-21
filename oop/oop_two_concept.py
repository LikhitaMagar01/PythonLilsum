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