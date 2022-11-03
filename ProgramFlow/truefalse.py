day="monday"
temprature=30
raining=True
if (day=="saturday" and temprature==30) or not raining: # parenthesis changes the result by priority order
    print("go swimming")
else:
    print("learn python")

# using boolean expressions
name=input("Please enter your name: ")
if name:
    print("hello {0}".format(name))
else:
    print("are you the man with no name?")

