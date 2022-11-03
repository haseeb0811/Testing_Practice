# for printing separators 
data=input("Enter a series of number with any separators you like: ")
separator=" "
for char in data:
    if not char.isnumeric():
        separator=separator+char
print(separator)

# for printing number
digit=" "
for num in data:
    if num.isnumeric():
       digit=digit+num
    if not num.isnumeric():
        digit=digit+" "
print(digit)




