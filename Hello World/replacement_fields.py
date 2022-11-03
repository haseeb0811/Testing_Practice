age=24 #an integar literal
# "str" function can be used to coherce the interger into string value
#print("my age is ",str(age)," years")

#or by using the ".formate(variable name)" and with a {0} where you want to print that value
print("my age is {0} years".format(age))

city="bahawalpur"
print("i live in {0}".format(city))

#or
print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(31,"jan","mar","may","jul",
                                                             "aug","oct","dec"))
#values are replaced by the liertal inside the parenthesis after ".format"
#or
print("there are {0} days in jan, mar, may, jul, aug, oct, dec".format(31))

#it's not the order that determines the value, it's the index that defines the value to be used
print("jan: {2}, feb: {0}, mar: {1}, april: {2}, may: {1}".format(28,30,31))