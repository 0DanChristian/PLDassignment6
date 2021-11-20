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

first = 0
second = 0
third = 0
fourth = 0

# If 
# first statement
if first_no < fourth_no and first_no < third_no and first_no < second_no:
    first = first_no
    if second_no < fourth_no and second_no < third_no and second_no < first_no:
        first = second_no
    if third_no < first_no and fourth_no < second_no and fourth_no < third_no:
        first = third_no
    else:
        first = fourth_no

# second statement
elif first_no < second_no and first_no < third_no and first_no < fourth_no:
    second = first_no
    if second_no < first_no and second_no < third_no and second_no < fourth_no: 
        second = second_no
    if third_no < first_no and third_no < second_no and third_no < fourth_no:
        second = third_no
    else: 
        second = fourth_no

# third statement
elif first_no < second_no and first_no < third_no and first_no < fourth_no:
    third = first_no
    if second_no < first_no and second_no < third_no and second_no < fourth_no:
        second = second_no
    if third_no < first_no and third_no < second_no and third_no < third_no:
        second = third_no
    else:
        second = fourth_no

# fourth statement
elif first_no < second_no and first_no < third_no and first_no < fourth_no:
    fourth = first_no
    if second_no < first_no and second_no < third_no and second_no < fourth_no:
        fourth_no = second_no
    if third_no < first_no and third_no < second_no and third_no < fourth_no:
        fourth_no = third_no
    else:
        fourth = fourth_no


# display
print("The numbers from highest to lowest are: ", first, second, third, fourth)