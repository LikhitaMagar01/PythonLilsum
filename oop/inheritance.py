# inheritance
# one class derives the properties of another class

class Car:

    @staticmethod
    def start():
        print("car start")

    @staticmethod
    def stop():
        print("car stop")


class Toyota(Car):

    def __init__(self, name):
        self.name = name

c1 = Toyota('sipee')
c2 = Toyota('gippee')
print(c1.name)
c1.start()