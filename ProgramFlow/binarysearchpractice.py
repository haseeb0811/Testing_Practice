size=int(input("Enter length of list:"))
user_list=[]
i=0
for val in range(size):
    val=int(input("Enter value to be stored in list:"))
    user_list.append(val)
val_to_find=int(input("Enter a number to find:"))
j=0
k=size-1
flag=0
mid=0
pos=0
while j<k and flag==0:
    mid=(j+k)//2
    if user_list[mid]==val_to_find:
        flag=1
        pos=mid+1
    if user_list[mid]>val_to_find:
        k=mid-1
    else:
        j=mid+1
if flag==1:
        print("{} found at {}".format(val_to_find,pos))
else:
        print("Number not found!")