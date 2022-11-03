import random # "random" is a module that contains built in functions
# for i in range(0,4): # using for Loop
#     answer=12
#     print("enter any number between 1 and 15:")
#     guess=int(input())
#     if guess==answer:
#         print("wow, you've got it in first time!")
#         break
#     elif i<=3:
#         print("please guess again")
#     elif i==4:
#         print("you've lost")
#     else:
#         break

# using else if
hieghst_val=10
answer=random.randint(1,hieghst_val) # 'randint' is a function of random module that will select any random value from given range
print("answer is ",answer) # for testing the code
guess=int(input("enter any value between 1 and {}:".format(hieghst_val)))
if guess<answer:
    print("enter higher number:")
    guess=int(input())
    if guess==answer:
        print("you guessed it")
    else:
        print("sorry, you have not guessed corectly")
elif guess>answer:
    print("enter lower number:")
    guess=int(input())
    if guess==answer:
        print("you guessed it")
    else:
        print("sorry, you have not guessed correctly")
else:
    print("well done, you're guess is correct")

#or
# answer=12
# guess=int(input("please enter any number between 1 and 15:"))
# if guess!=answer:
#     if guess>answer:
#         print("please enter lower number:")
#     else:
#         print("please enter higher number:")
#     guess=int(input())
#     if guess==answer:
#         print("well done, you guessed it")
#     else:
#         print("sorry, you're guess was wrong")
# else:
#     print("you've guess it in first time")

