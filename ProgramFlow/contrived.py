numbers=[1,45,31,60]
for number in numbers:
    if number%8==0:
        print("These numbers are'nt acceptable")
        break
else: # else can be used after the loop and will only execute if the loop terminates normally
    print("Numbers are acceptable")