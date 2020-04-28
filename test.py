# "# " is used for making comment in Python
# print command is used to print something on console
print("Hello This is Just for Testing")

# Taking input from user
name = input("Please Enter your name ---- ")
print("your name is " + name)

#  When we take input from user, it is always a String, if you want number then we have to typecast
age = input("Please enter your age ------")

# Want to add 10 in age number
final_age = int(age) + 10  # Type casted age to number and then added 10
print("Your Actual Age is : " + str(final_age))  # Again type cast back to String to concatnate with another string