#functions in python

# Function 1 - Not taking any argument and nt retuning any value.
def testfun1():
    "This is first line and can be used for commenting"
    print("This is testing function 1")

#How to call  function
testfun1()

# Function 2:  taking argument but not returning any value
def testfun2(a,b):
    sum=a+b
    print("Sum of 2 numbers is " + str(sum))

testfun2(23,45)


# Function 3:  taking argument and returning value
(2*20)+30

def muti(a,b):
    c=a*b
    return c

def sum(a,b):
    c=a+b
    print(c)
# call multiple function which will return values and pass it in sum funtion as one argument
m = muti(2,20)
sum(m,30)


# Function 4:  taking no argument and returning value
def returndata():
    x="abcd"
    return x

data = returndata()
print(data)