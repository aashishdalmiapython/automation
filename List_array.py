list1 = [12,20.34,"test",38, 55]
list2 = ["dalmia", 34, 2008, 34]
for i in list1:
    print(i)

# fetching by index
print(list1[2])
# fetching by just starting index
print(list1[2:])
# fetching by just last index
print(list1[:2])
# fetching by range of index
print(list1[1:2])

# change a value
list1[3] = 57
print(list1)

# insert a value
list1.insert(3, "aashish")
print(list1)
# remove a value
list1.remove(55)
print(list1)
# length of the list
print(len(list1))


# Concatinate list
list3 = list1+list2
print(list3)

# find the count of a particular value in tuple
print(list3.count(34))