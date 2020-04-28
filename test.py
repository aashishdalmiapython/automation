# "# " is used for making comment in Python
# print command is used to print something on console
print("Hello, This is Just for Testing")





# Exercise 1: -
# Taking input from user
name =\
    input("Please Enter your name ---- ")

#print("your name is " + name)

#  When we take input from user, it is always a String, if you want number then we have to typecast
age=\
    input("Please enter your age ------")
# Want to add 10 in age number
#final_age = int(age) + 0  # Type casted age to number and then added 10
#print("Your Actual Age is : " + str(final_age))  # Again type cast back to String to concatnate with another string



# Take Name, Age and Location from User
location = input\
    ("Please enter your location ---->")
#Print data in following format
print("User name is " + name + ", is " + age + " years old and lives in " + location)

# Exercise 2
Math_marks = input("Enter maths marks")
Science_marks =input("Enter science marks")
Eng_marks =input("Enter english marks")
#Take Marks of Maths, Science and English from User
Total = int(Math_marks) + int(Science_marks) + int(Eng_marks)
percentage = (Total/3)
print("User name is " +name+", Scored " + str(percentage) + " % in exams")


# Exercise 3
Enter_number = input("Enter a number")
if (int(Enter_number)>=100):
    print("Number is greater")
else:
    print("Number is smaller")


# Exercise 4
number = input("Enter the number")
if (int(number) < 0):
    print("Number is -ve")
elif (int(number) == 0):
    print("Number is 0")
elif (int(number) % 2 == 0):
    print("number is even")
else:
    print("number is odd")

# Condition handling using if else
# Condition handling using if ,elif, elif...else
# Condition handling using nested  if if else else
# Condition handling using logical or condition (or)
# Condition handling using logical and condition (and)
# Condition handling using with Not condition (!=)
