

# Practice Exercise 1
print ("Practice Exercise 1")
number1 = input("Enter First number ")
number1 = int(number1)

number2 = input("Enter Second number ")
number2 = int(number2)

number3 = input("Enter Third number ")
number3 = int(number3)a

if (number1>number2 and number1>number3):
    print(str(number1) + " is largest number")
elif(number2>number1 and number2>number3):
    print(str(number2) + " is largest number")
elif(number3 > number1 and number3 > number2):
    print(str(number3) + " is largest number")

if (number1 < number2 and number1 < number3):
    print(str(number1) + " is smallest number")
elif (number2 < number1 and number2 < number3):
    print(str(number2) + " is smallest number")
elif (number3 < number1 and number3 < number2):
    print(str(number3) + " is smallest number")
print ("Practice Exercise 1 - Ends here")

# Practice Exercise 2
print ("Practice Exercise 2 - Start")
number = input("Enter a number ")
number = int(number)
if (number%5==0 and number%11==0):
    print(str(number)+ " is divisible by 5 & 11 both")
elif(number%5==0 and number%11!=0):
    print(str(number)+ " is divisible by 5 Only")
elif(number%5!=0 and number%11==0):
    print(str(number) + " is divisible by 11 Only")
else:
    print(str(number) + " is not divisible by 5 and 11")
print("Practice Exercise 2 - Ends here")


# Practice Exercise 3
print ("Practice Exercise 3 - Start")
if (number>0 and number<=12):
    if(number==2):
        print("no of days are 28")
    if(number==1 or number==3 or number==5 or number==7 or number==8 or number==10 or number==12):
        print("no of days are 31")
    else:
        print("no of days are 30")
else:
    print("Invalid month entered")

print("Practice Exercise 3 - Ends here")


# Practice Exercise 4
print("Practice Exercise 4 - Starts here")
side1 = input("Enter First side ")
side1 = int(side1)

side2 = input("Enter Second side ")
side2 = int(side2)

side3 = input("Enter Third side ")
side3 = int(side3)

if (side1==side2==side3):
    print("this is equilateral triangle")
elif(side1==side2 or side1==side3 or side1==side3):
    print("this is isosceles triangle")
else:
    print("this is Scalene triangle")
print("Practice Exercise 4 - Ends here")

# Practice Exercise 5
print("Practice Exercise 5 - Starts here")
Math_marks = input("Enter maths marks")
Science_marks =input("Enter science marks")
Eng_marks =input("Enter english marks")
#Take Marks of Maths, Science and English from User
Total = int(Math_marks) + int(Science_marks) + int(Eng_marks)
percentage = (Total/3)

if (percentage>90):
    print("Grade A Marks")
elif (percentage>80 and percentage<90):
    print("Grade B Marks")
elif(percentage>70 and percentage<80):
    print("Grade C Marks")
elif (percentage>60 and percentage<70):
    print("Grade D Marks")
elif (percentage>50 and percentage<60):
    print("Grade E Marks")
elif (percentage>40 and percentage<50):
    print("Grade F Marks")
else:
    print("Fail")
print("Practice Exercise 5 - Ends here")