parrot="Norwegian Blue"
letter=input("Enter a letter: ")
# "in" used for checking the letters and it's letter sensitive
if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("i don't need that letter.")
