# data strore in the form for key and value pair
# We can add and update any value in dict...

odisc = {"k1":"test",2:"test2","K3":3}
print(odisc)
# printing value by its key
print((odisc["K3"]))

odisc["K4"]="abc2"
print(odisc)

# print all keys
print(odisc.keys())
# print all values
print(odisc.values())
# print all keys: Values
print(odisc.items())
# print length of disc..
print(len(odisc))
