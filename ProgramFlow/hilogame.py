low=int(input("Enter the starting number:"))
high=int(input("Enter the ending number:"))
print("Think of any number between {} and {}".format(low,high))
input("Press Enter to start when you're ready...")
guesses=1
while True:
    mid=low+(high-low)//2
    user_val=input("My guess is {}. Press 'h' for higher, 'l' for lower, and 'c' for correct guessing:".format(mid).casefold())
    if user_val=="h":
        low=mid+1
    if user_val=="l":
        high=mid-1
    guesses+=1
    if user_val=="c":
        break
print("I guessed it in {} times".format(guesses))
    