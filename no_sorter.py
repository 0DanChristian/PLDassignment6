#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

# ask for the first number
first_no = int(input("Enter your first desired number: "))
# ask for the second number 
second_no = int(input("Enter your second desired number: "))
# ask for the third number
third_no = int(input("Enter your third desired number: "))
# ask for the fourth number
fourth_no = int(input("Enter your fourth desired number: "))
# what number is the smallest

smallest = 0
small = 0
middle = 0
large = 0

# If 
# first situation
if first_no < third_no and first_no < second_no:
    smallest = first_no
    if second_no < third_no and second_no < first_no:
        smallest = second_no
    else:
        smallest = third_no

# second situation
elif first_no < second_no and first_no < third_no:
    small = first_no
    if second_no > first_no and second_no < third_no: 
        small = second_no
    else: 
        small = third_no

# third situation
elif first_no > second_no and first_no > third_no:
    middle = first_no
    if second_no > first_no and second_no > third_no:
        middle = second_no
    else:
        middle = third_no


# display
print("The numbers from highest to lowest are: ", smallest, small, middle)