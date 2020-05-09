from Inheritance2 import two

class three(two):

    def __init__(self):
        print("this is class three constr...")

    def performlogin(self):
        print("login successful")
    def diff(self,a,b,c):
        print(a-b-c)