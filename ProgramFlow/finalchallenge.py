message="Please choose your option from the list below:"
msg1="\n1. Learn Python"
msg2="\n2. Learn Java"
msg3="\n3. Go swimming"
msg4="\n4. Have dinner"
msg5="\n5. Go to bed"
msg0="\n0. Exit"
while True:
    print(message,msg1,msg2,msg3,msg4,msg5,msg0)
    user_val=int(input())
    if user_val in range(1,6):
        print("Your choose {}".format(user_val))
    elif user_val not in range(0,6):
        print("Invalid Input!")
        continue
    else:
        print("You Quit")
        break