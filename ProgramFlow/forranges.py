# "range" is a built in function and can be used with any other built in functions, loops or conditions
# range works just like slicing strings, the end digit is not included
for i in range(0,20): # this should count upto but not including 20
    print("i is now {}".format(i))

# if you want to count from zero, then you don't have to give starting value
for j in range(20):
    print("the value of j is now {0}".format(j))

# using steps need a start value too
for k in range(10,20,2): # using steps of 2 digits
    print("value of k is {}".format(k))

# prinitng in reverse order requires decrement of negative indexing
for l in range(10,0,-1):
    print("value of l:{}".format(l))