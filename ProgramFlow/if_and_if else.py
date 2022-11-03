name=input("please enter your name: ")
age=int(input("please enter your age {}: ".format(name)))
# used "int" to make sure entered value is integer
if age<18:
    print("please come back in {} years".format(18-age))
elif age==900:
    print("sorry, yoda, you die in return of jedi")
else:
    print("{}, you're eligible for voting".format(name))
    print("please put X in the box")
    

