#using the "\n" an escape ch for new line jump
splitstring="this line\n has been splitted\n  into many\n   parts"
print(splitstring)

#or
splitstring="""the line
 has been 
 divided into several 
 lines"""
print(splitstring)

#or
print("""the line has
 been divided into
 several lines""")

#if don't want to jump to new line, then use "\" after end of line
print("""the line has\
 not been divided\
 into several line""")

#using the "\t" an escape ch for tab space
tabbedstring="this line\tis used with\ttabe escape ch"
print(tabbedstring)

#using the single quote (\') escape ch
print('the shop owner said: "no, no,... e\'s\',.... he\'s sleeping."')

#using the double quote (\") escape ch
print("the shop owner said: \"no, no,..... e's',.... he's sleeping.\"")

#if you want to use double and single quotes without any escape ch in a single statement then statement need to be enclosed in three time double quotes
print("""the shop owner said: "no, no,..... e's',..... he's sleeping." """)

#if you want to use back slash "\" in the print message then use double back slashes
print("c:\\users\\raw material")

