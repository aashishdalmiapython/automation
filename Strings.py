

# fetch substring using starting and ending index
string = "  learnsoftwaretestingskills  "
print(len(string))
print(string[0:9])

# fetch substring using just the starting index
print(string[13:])

# fetch substring using just the ending index
print(string[:13])
# to print all string in upper case
print(string.upper())
# toprint all string in lower case
print(string.lower())
# to print first letter of string as capital

print(string.capitalize())
# remove the leading spaces
print(string.lstrip())
# remove the trailing spaces
print(string.rstrip())
# remove leading & trailing spaces both
print(string.strip())


#### replace part of a sting
print(string.replace("software","automation"))

#find how many l exists in string
#1 way
x=0
for i in string:
   if(i=='l'):
       x=x+1
print(x)
# 2 way
x= len(string)
y=len(string.replace("l", ""))
print(x-y)

### find a substring in a string
print(string.find("testing"))

##### split the string
email_add = "this is my email aashishdalmia10@gmail.com"
splitlist = (email_add.split(' '))
print(len(splitlist))
print(splitlist)


####Compair 2 strings

