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

# first statement
if first_no < second_no and first_no < third_no and first_no < fourth_no:
    if second_no < third_no and second_no < fourth_no:
        min, first_mid, second_mid, max = first_no, second_no, third_no, fourth_no
    else: 
        min, first_mid, second_mid, max = first_no, second_no, third_no, fourth_no

# second statement
elif second_no < first_no and second_no < third_no and second_no < fourth_no:
    if first_no < third_no and first_no < fourth_no:
        min, first_mid, second_mid, max = first_no, second_no, third_no, fourth_no
    else:
        min, first_mid, second_mid, max = first_no, second_no, third_no, fourth_no

# third statement
elif third_no < first_no and third_no < second_no and third_no < fourth_no:
    if fourth_no < first_no and fourth_no < second_no:
        min, first_mid, second_mid, max = first_no, second_no, third_no, fourth_no
    else:
        min, first_mid, second_mid, max = first_no, second_no, third_no, fourth_no

# fourth statement
else:
    if first_no < second_no :
        min, first_mid, second_mid, max = first_no, second_no, third_no, fourth_no
    else:
        min, first_mid, second_mid, max = first_no, second_no, third_no, fourth_no

print("min : ", min)
print("mid : ", first_mid)
print("smid : ", second_mid)
print("max : ", max)