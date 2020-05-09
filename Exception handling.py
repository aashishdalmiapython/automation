# try is used when we think - our code can throw an error
# put the code inside try block
try:
    input1 = input("Enter first number -- ")
    input2 = input("Enter second number --")
    sum = int(input1)+int(input2)
    print("sum is", sum)
    state= "Pass"
# except part is required,if try is used
# this part will execute if there is any exception
except:
    print("There is an error in input")
    state="Fail"
# finally is not mandatory
# this part will execute in both the case - exception & without exception
finally:
    print("Test case status is", state)