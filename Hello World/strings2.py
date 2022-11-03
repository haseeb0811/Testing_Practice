parrot="naerign blue"
print(parrot)
#if you want to print any letter from string, then just write letter number in square brackets in print function
#the counting starts from "0" not "1"
print(parrot[3])

#now using the splitting in index by using colon ":"
print(parrot[0:6])
#or
print(parrot[:6])
#in this statement the last digit is not included that means this will show from 0 upto but not including 6
print(parrot[8:12])
#or
print(parrot[8:])

print(parrot[:6]+parrot[6:])
print(parrot[:])

letters="abcdefghijklmnopqrstuvwxyz"
print("my name is:",letters[7]+letters[0]+letters[-8]+letters[4]+letters[4]+letters[1])
print(letters[:])
print(letters[:27])

#using slides in split indexing
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6:2])    # gonna print Nre by selecting the second index in each turn
print(parrot[0:6:3])    # gonna print Nw by selecting the third index in each turn

number = "9,223;372:036 854,775;807"
seperators = number[1::4] #gonna print the seperators by selecting the fourth index in each turn
print(seperators)

#condition
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])