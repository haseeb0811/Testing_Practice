name=input("Please enter your name: ")
age=int(input("Hello {}, what is your age: ".format(name)))
if not (age>18 and age<=31):
    if age<=18:
        print("you're underage")
    elif age>31:
        print("you're overage")
else:
    print("Welcome, enjoy youre holidys")

