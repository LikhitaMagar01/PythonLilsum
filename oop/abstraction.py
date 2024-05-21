# abstraction
# hiding the implementation of class
# showing essential features to the user

class Car:

    def __init__(self):
        self.accelerator = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.accelerator = True
        print('car is started')

c1 = Car()
c1.start()