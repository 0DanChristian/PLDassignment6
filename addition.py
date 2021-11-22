# addition quiz
# program that automatically generate two numbers to add
# let the user answer and evaluate if the user has the correct answer

# import random
from random import randint 

# intro
print("\n\033[95mWe'll give two random numbers, please find the sum.\033[0m \n ")


# generate 2 random integer
print("The first number will be ", end='')
print(randint(1, 1000,))
print("The second number will be ", end='')
print(randint(1, 1000))

