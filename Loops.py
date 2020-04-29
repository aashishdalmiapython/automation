# for loop with final range
for i in range(10):
    print(i)

number = input("Enter a number")
number = int(number)
for f in range(int(number)):
    print(f)

# for loop with starting & final range
z=5
for g in range(1,11):
    print(str(number) + " * " + str(g) + " = " + str(number*g))

# for loop with increment
z=5
for g in range(1,11,2):
    print(str(number) + " * " + str(g) + " = " + str(number*g))


# for loop with Decrement

z=5
for g in range(10,0,-1):
    print(str(number) + " * " + str(g) + " = " + str(number*g))


# for loop with list:

list1 = ['abc','def','ghi','jkl']
for h in list1:
    print(h)

list2 = [1,3,5,6,7,88]
sum = 0
for h in list2:
    sum = sum + h

print(str(sum))


# while loop with increment operator

j=1
while (j<=10):
    print(j)
    j+=1 # j=j+1

# while loop with decrement operator

d=10
while (d>=1):
    print(d)
    d -= 1 # d=d-1

# break statement (use to break out of the loop on a perticular condition)
d=10
while (d>=1):
    if (d==5):
        print(d)
        break
    d -= 1


# continue statement (use to skip the execution for a perticular condition in the loop)
n = 5
for l in range(1,11):
    if(n*l%10==0):
        continue
    print(n*l)

# else with loop

for k in range(2,12):
    print(k)
else:
    print("loop ended")


