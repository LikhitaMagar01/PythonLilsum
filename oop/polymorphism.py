# polymorphism : many forms
# same method can be done by various ways

# operator overloading:
# when same operator is allowed to have different meaning according to the context

#  eg of operator overloading: many forms of + operator
# print(1 + 3) : add by + operator
# print("hello" + "world") : concatenate by + operator
# print([1,2,3] + [4,5,6]) :  merge by + operator

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print("your complex number is ", str(self.real) + "i" + str(self.img) + "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


num1 = Complex(33, 44)
num1.showNumber()
num2  = Complex(44, 55)
num2.showNumber()

num3 = num1 -num2
num3.showNumber()