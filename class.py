# create a Class, define Constructors  & Calling the class and its methods
# functions/methods in call -  has "self" argument by default - no need pass any value for this while calling it
# Class 1 -- without Constructors
class A:
    def sum(self,a,b):
        c=a+b
        print(c)

    def url(self):
        web="www.test.com"
        return web
    def mul(self,a,b):
        mul=a*b
        return mul

# for Calling the class - defined object of the class and pass class name
# after that - call the class function/methods.
obj = A()
s = obj.sum(12,12)
e=obj.url()
print(e)

mul = obj.mul(2,4)
print(mul)

# Class 2  - with Constructors
class A:
    # first method in a call is contructur
    # it is always named as "__init__"
    # In contructur, define the part of code that need to be execute at the start

    def __init__(self,a,b):
        print("This is Class Constructor")
        c=a+b
        print(c)

    def add(self, a, b):
        print(a + b)

    def sub(self, a, b):
        return a - b

# no need to call the constuctor method,
# it is by default called on creating the class object
obj = A(23,23)
obj.add(23, 11)
x =obj.sub(11, 3)
print(x)
