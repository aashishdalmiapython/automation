# differnt type of arguments:-

####required arguments
# here a and b are required arguments
def sum(a,b):
    c=a+b
    print(c)

sum(34,23)

##### Keyword argument
# while calling the funation assign value to the keys directly
def mysum(a,b):
    c=a+b
    print(c)

mysum(b=34,a=73)

### Default argument
#passing a def value to an argumant while creating the function
# and it should be defined at the end

def mydefsum(a,b=10):
    c=a+b
    print(c)
# we don't need to pass both values while calling them
mydefsum(5)

