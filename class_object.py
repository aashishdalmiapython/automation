# Using class - methods in differnt file.

# import the filename(module) whose method you want to call
import Classfile1
# define object = filename.classname()
obj=Classfile1.A()
url=obj.url()
print((url))

print(obj.mul(2,5))

# define object = filename.classname(arguments of constucture)
obj2=Classfile1.B(2,3)
obj2.add(5,7)
sub= obj2.sub(6,4)
print(sub)

obj3=Classfile1.c()
x = obj3.diff(23,26)
print(x)