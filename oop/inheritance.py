# inheritance
# one class derives the properties of another class

# class Car:

#     @staticmethod
#     def start():
#         print("car start")

#     @staticmethod
#     def stop():
#         print("car stop")


# class Toyota(Car):

#     def __init__(self, name):
#         self.name = name

# class Furtuner(Toyota):
#     def __init__(self, type):
#         self.type = type

# c1 = Toyota('sipee')
# c2 = Toyota('gippee')
# print(c1.name)
# c1.start()
# f1 = Furtuner('electric')
# f1.start()


# types
# single inheritance : single parent and single child
# multi-level inheritance : one base class to child child - base and child properties derived to grand-child class
# multiple inheritance : multiple base class to single child

# eg of multiple inheritance
class A:
    var_a = "welcome A"

class B:
    var_b = "welcome B"

class C(A, B):
    var_c = "welcome c"

var_c1 = C()
print(var_c1.var_a)

# related to inheritance
# super method : use to access methods of the parent class
# super() means we are talking about parent class

class Car:

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car start")

    @staticmethod
    def stop():
        print("car stop")


class Toyota(Car):

    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

t1 = Toyota("car name", "electric")
print(t1.type)

