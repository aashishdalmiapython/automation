import Pymodule # on importing the module - executeable code gets executed

# To call the module_function
Pymodule.sum(5,4)

# To call the class_function
obj = Pymodule.module() # creating class object - executes the class constructor
abc = obj.devide(12,4)
print("Division Result - "  + str(abc))


