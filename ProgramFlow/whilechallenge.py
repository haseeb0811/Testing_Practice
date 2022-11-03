import random
highest_val=int(input("Enter the highest number you want to go upto:"))
answer=random.randint(1,highest_val)
guess=int(input("Guess a number:"))
if guess==answer:
    print("Wow!, you've got it in first try")
while guess!=answer:
    if guess>answer:
        print("Please enter lower number:")
    else:
        print("Please enter higher number:")
    guess=int(input())
    if guess==0 or guess=="quit":
        print("Game Over!")
        break
    if guess==answer:
        print("Your answer '{}' is correct!".format(guess))