#inserting/removing/changing  a value in touple didnt work

tuple1 = (23,25,27,29,"aashish",27)
print(tuple1)
print(tuple1[4])

for i in range(len(tuple1)):
    print(tuple1[i])

# join two tuple
tuple2 = (23,98)
tuple3 =tuple1+tuple2
print(tuple3)

# find index of any value
print(tuple3.index("aashish"))

# find the count of a particular value in tuple
print(tuple3.count(27))