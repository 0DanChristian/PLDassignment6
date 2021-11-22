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

# first statement if the first given is the highest
if first_no >= second_no >= third_no >= fourth_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {first_no}, {second_no}, {third_no}, and {fourth_no}. ")
elif first_no >= third_no >= fourth_no >= second_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {first_no}, {third_no}, {fourth_no}, and {second_no}. ")
elif first_no >= fourth_no >= second_no >= third_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {first_no}, {fourth_no}, {second_no}, and {third_no}. ")
elif first_no >= second_no >= fourth_no >= third_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {first_no}, {second_no}, {fourth_no}, and {third_no}. ")
elif first_no >= third_no >= second_no >= fourth_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {first_no}, {third_no}, {second_no}, and {fourth_no}. ")
elif first_no >= fourth_no >= third_no >= second_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {first_no}, {fourth_no}, {third_no}, and {second_no}. ")

# second statement if the second given is the highest
elif second_no >= first_no >= third_no >= fourth_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {second_no}, {first_no}, {third_no}, and {fourth_no}. ")
elif second_no >= third_no >= fourth_no >= first_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {second_no}, {third_no}, {fourth_no}, and {first_no}. ")
elif second_no >= fourth_no >= first_no >= third_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {second_no}, {fourth_no}, {first_no}, and {third_no}. ")
elif second_no >= third_no >= first_no >= fourth_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {second_no}, {third_no}, {first_no}, and {fourth_no}. ")
elif second_no >= first_no >= fourth_no >= third_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {second_no}, {first_no}, {fourth_no}, and {third_no}. ")
elif second_no >= fourth_no >= first_no >= third_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {second_no}, {fourth_no}, {first_no}, and {third_no}. ")

# third statement if the third given is the highest
elif third_no >= first_no >= second_no >= fourth_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {third_no}, {first_no}, {second_no}, and {fourth_no}. ")
elif third_no >= first_no >= fourth_no >= second_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {third_no}, {first_no}, {fourth_no}, and {second_no}. ")
elif third_no >= second_no >= first_no >= fourth_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {third_no}, {second_no}, {first_no}, and {fourth_no}. ")
elif third_no >= second_no >= fourth_no >= first_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {third_no}, {second_no}, {fourth_no}, and {first_no}. ")
elif third_no >= fourth_no >= first_no >= second_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {third_no}, {fourth_no}, {first_no}, and {second_no}. ")
elif third_no >= fourth_no >= second_no >= first_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {third_no}, {fourth_no}, {second_no}, and {first_no}. ")

# fourth statement if the fourth given is the highest
elif fourth_no >= first_no >= second_no >= third_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {fourth_no}, {first_no}, {second_no}, and {third_no}. ")
elif fourth_no >= first_no >= third_no >= second_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {fourth_no}, {first_no}, {third_no}, and {second_no}. ")
elif fourth_no >= second_no >= first_no >= third_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {fourth_no}, {second_no}, {first_no}, and {third_no}. ")
elif fourth_no >= second_no >= third_no >= first_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {fourth_no}, {second_no}, {third_no}, and {first_no}. ")
elif fourth_no >= third_no >= first_no >= second_no:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {fourth_no}, {third_no}, {first_no}, and {second_no}. ")
else:
    print(f"From highest to lowest, the arrangement of the numbers from the given is, {fourth_no}, {third_no}, {second_no}, and {first_no}. ")