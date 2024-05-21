
#  car is class
#  collection of data / attributes and methods / functions
class Car:
    #  attributes
    color = "blue"

# car1 is object / instance
car1 = Car()
# print(car1.color)


#  constructor
#  __init__ constructor call when object / class is initiated
#  always gets initiated
#  data that is store in the class / object is attributes. eg: fullname
class Flower:
    shop_name = 'Bloomish'
    #  the presedence of obj.attr > class.attr. eg: anonymous is not printed, here obj.fullname i.e. rose and lotus is printed
    fullname="anonymous"
    #  self is itself like here flower1 is self

    # defult constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, fullname, type):
        print('adding new flower in flower db', self)
        self.fullname = fullname
        self.type = type

    def greet(self):
        print('welcome floweris')

    def flower_type(self):
        return self.type

#  the bracket in class Flower() is use to call constructor
flower1 = Flower('rose', 1)
# flower1.greet()
# print(flower1.flower_type())
# print(flower1.fullname, flower1.type)
flower2 = Flower('lotus', 2)
# print(flower2.flower_type())
# print(flower2.fullname, flower2.type)

# attributes / data
#  class.attr which is common for all objects from the class variable initialized in class. eg: Flower.shop_name
#  obj.attr which is different in different obj : self.attr => self is reference for obj instance. eg: obj.name or self.name
#  the presedence of obj.attr > class.attr. eg: anonymous is not printed, here obj.fullname i.e. rose and lotus is printed

#  Write a program that create a class student that takes name and marks of 3 subjects as arguments in constructor. Then, create a method to print the average.
# ans:
class Student:
    def __init__(self, full_name, sub_marks):
        self.full_name = full_name
        self.sub_marks = sub_marks

    def average_marks(self):
        sum = 0
        for value in self.sub_marks:
            sum += value
        print('your average marks is', sum/3)

    # it is static method which doesn't require self / object
    # converts normal method to static method; decorators
    @staticmethod
    def greet():
        print("namaste")

s1 = Student('ragini',[99, 98, 97])
s1.average_marks()
s1.greet()

# Write a project that create class Account with two attributes - balance and account no. then create methods for debit, credit and print the balance.
# ans
class Account:

    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, val):
        self.balance -= val
        self.receipt()

    def credit(self, val):
        self.balance += val
        self.receipt()

    def receipt(self):
        print("your current balance is", self.balance)

a1 = Account(5000, 101)
a1.debit(2000)
a1.credit(1000)