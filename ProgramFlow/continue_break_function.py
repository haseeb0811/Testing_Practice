# continue function when called skips the remaining block of code and transfer the control to loop statement
shopping_list1=["milk","soda","spam","eggs"]
for item in shopping_list1:
    if item=="spam":
        continue
    print("buy "+item)

# break function terminates all remaining block of code in loop
shopping_list2=["milk","soda","spam","eggs","bread"]
item_at=None 
item_to_find=input("enter item to find: ")
for index in range(len(shopping_list2)):
    if shopping_list2[index]==item_to_find:
        item_at=index
        break
if item_at is not None:
    print("{} item found at index {}".format(item_to_find,item_at))
else:
    print("Item not found")


