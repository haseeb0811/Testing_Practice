answer=5
guess=int(input("Enter any number between 1 and 10:"))
if guess==answer:
    print("well done, you've guessed it in first try")
elif guess!=answer:
    if guess>answer:
        print("enter lower number:")
    else:
        print("enter higher number:")
    guess=int(input())
if guess==answer:
        print("you've guessed it")
else:
    print("you're guess was wrong")
    
    