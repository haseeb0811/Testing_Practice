activity=input("what would you like to do? ")
# "not in" used to convert the boolen value
if "cinema" not in activity.casefold(): # "str.casefold() is used to convert upper into lower case where "str" is name of variable string
    print("but i want to go cinema")
else:
    print("ok!")