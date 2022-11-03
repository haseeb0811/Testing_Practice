# now to use "and" operator!
age=int(input("please enter your age:"))
if age>=16 and age<=65:
    print("have a good day at work")
else:
    print("you're not eligible")

# using "range" function
age=int(input("enter your age: "))
if age in range(16,66):
    print("have a good day at work!")
else:
    print("enjoy youre free time")

# now to use "or" operator!
age=int(input("what is your age? "))
if age<16 or age>65:
    print("you may rest")
else:
    print("have a good day at work")

