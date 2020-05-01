## read file by creating object of the file class method(open), here "r" means,readingthe file
objfile = open("C:\FileRead\pytest.txt","r")
## read complete file
#x=objfile.read()
#print(x)
##
## read file line by line
y = objfile.readline()
# print(y)

# to read character by character
for i in y:
    print(y)
    objfile.seek(7)  # move to the cursor to the mention position...
    print(objfile.tell()) # tell the current position on curson
    y = objfile.readline()

# to read line by line
while (y):
    print(y)
    y=objfile.readline()


# writing to file
objwrite = open("C:\FileRead\pytest1.txt", "w")
objwrite.write("This is test 456575")
#appending the file.
objappend = open("C:\FileRead\pytest1.txt","a")
objappend.write("this is next line")


