possible_directions=["east","west","north","south"]
entered_direction=""
while entered_direction not in possible_directions:
    entered_direction=input("Enter a direction: ")
    if entered_direction.casefold()=="quit":
        print("Game over")
        break
if entered_direction in possible_directions:
    print("Aren't you glad, you got out of there")
