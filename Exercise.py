# Exercise 1
# Interchange variable values with using 3rd Variable
#  Take input number from User

input_num_a = int(input("Please enter your first number --- > "))
input_num_b = int(input("Please enter your second number --- > "))

# We are using 3rd variable
c = input_num_a
input_num_a = input_num_b
input_num_b = c

# After change first value is
print("After changing value, first value is =  " + str(input_num_a))

# After change second value is
print("After changing value, second value is =  " + str(input_num_b))


# Interchange variable values without using 3rd Variable

#  Take input number from User

input_num_a = int(input("Please enter your first number --- > "))
input_num_b = int(input("Please enter your second number --- > "))

# We are not using 3rd variable

input_num_a = input_num_a + input_num_b
input_num_b = input_num_a - input_num_b
input_num_a = input_num_a - input_num_b

# After change first value is
print("After changing value, first value is =  " + str(input_num_a))

# After change second value is
print("After changing value, second value is =  " + str(input_num_b))

# Exercise 2

for i in range(1,5):
    print("*****")

for j in range(1,5):
    if(j==2 or j==3):
        print("*   *")
        continue
    print("*****")


# Exercise 3

inputnumber = input("enter a number,like 11 -- ")
for i in range(1,11):
    if(int(inputnumber)*i%3==0 or int(inputnumber)*i%5==0 or int(inputnumber)*i%7==0):
        continue
    print(str(i) + " * " + inputnumber + " = " + str(int(inputnumber)*i))


# Exercise 4 (Factorial)
inputnumber1 = input("enter a number,like 2 -- ")
inputnumber1 = int(inputnumber1)
fac=1
while(inputnumber1>=1):
    fac = fac*inputnumber1
    inputnumber1 -=1
print(fac)


# Exercise (Fibanacci 0, 1,1,2,3,5,8,13,21,34)
inputnumber2 = input("enter a number,like 2 -- ")
inputnumber2 = int(inputnumber2)
s=0
g=1
print(s)
print(g)
while((g+s)<=inputnumber2):
    g = g+s
    s = g-s
    print(g)

# Practical Programming - 6: Write program to check Number is Prime or Not

#  Take input from User and Check number is Prime number or not

x = int(input("Please enter your number :  - "))

z = 0
for i in range(2, x):
    if (x % i == 0):
        print("Its not a Prime number")
        z = 1
        break
    i = i + 1
if (z == 0):
    print("This is Prime number")
