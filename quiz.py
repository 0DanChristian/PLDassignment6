# import
from random import randrange
import math
import sys
from time import sleep
# var
maxinf = 1
cor_ans = 0
wro_ans = 0
items = 10
# introduction
print("\033[95mIn this program, we will give two numbers for you to add and we'll see if your good at math!\033[0m")
# userinput
user = input("Please enter your name: ")
be_ready = input(f"\033[1m{user}\033[0m, are you ready to take this quiz? ")
ready = False

while not ready : 
    if be_ready.replace(".","",10).title() == "Yes":
        be_ready = "Yes"
        ready = True
    while be_ready.replace(".","",10).title() != "Yes":
        if be_ready.replace(".","",10).title() == "No":
            be_ready = input(f"No worries \033[1m{user}\033[0m! \nNow, are you ready \033[1m{user}\033[0m? ")
            if be_ready.replace(".","",10).title() == "No":
                be_ready = "No"
                break
            elif be_ready.replace(".","",10).title() == "Yes":
                be_ready = "Yes"
                break
            else:
                be_ready = ""
string = (f"\n\033[91mEmrace yourself\033[0m \033[1m{user}\033[0m\033[91m, we are about to begin.\033[0m \n")
for letter in string:
    sleep(0.10)
    sys.stdout.write(letter)
    sys.stdout.flush()

while maxinf <= items:

        no_one = randrange(0, 499)
        no_two = randrange(499, 999)
        system_answer = no_one + no_two
        if maxinf < items:
            print(f"Item no. {maxinf} out of {items}. \n\033[1m{no_one} + {no_two}.\033[0m\n")
        elif maxinf == items:
            print(f"Item no. {maxinf} out of {items}. \n\033[1m{no_one} + {no_two}.\033[0m\n")
        user_ans = input("What is your answer?\n")
        if user_ans.isalpha() == True:
            print("You are good!")
        elif user_ans.isdigit() == True:
            # correct answers
            if int(user_ans) == system_answer:
                cor_ans += 1
                maxinf += 1
                if cor_ans == 10:
                    None
                elif cor_ans >= 8 or cor_ans == 9:
                    print("That was great!")
                elif cor_ans >= 5 or cor_ans == 7:
                    print("Hooray")
                elif cor_ans >= 1 or cor_ans == 4:
                    print("That was nice!")
            # wrong answers
            elif int(user_ans) != system_answer:
                if wro_ans == 9:
                    print(f"The correct answer for no.{maxinf} is \033[91m{system_answer}.\033[0m")
                elif wro_ans >=7 or wro_ans == 8:
                    print(f"The correct answer for no.{maxinf} is \033[91m{system_answer}.\033[0m")
                elif wro_ans >=4 or wro_ans == 6:
                    print(f"The correct answer for no.{maxinf} is \033[91m{system_answer}.\033[0m")
                elif wro_ans >=0 or wro_ans == 3:
                    print(f"The answer for no.{maxinf} is \033[91m{system_answer}.\033[0m")

                wro_ans += 1
                maxinf += 1
        elif user_ans.isalnum() == True:
            print("\033[91mPlease take this seriously, if not, this quiz will never end.\033[0m")
        else:
            print("\033[93mThis program only accepts number as an input.\033[0m")


# grading
if cor_ans >= 10 and wro_ans == 0:
    print(f"\nYou are so good at this \033[1m{user}\033[0m you did a very great job! your grade is \033[92m{cor_ans}/{items}.\033[0m")
elif cor_ans >= 5 or cor_ans == 9 and wro_ans >= 1:
    print(f"\nYou are so good at this \033[1m{user}\033[0m you did a very great job! your grade is \033[92m{cor_ans}/{items}.\033[0m")
elif cor_ans >= 1 or cor_ans ==4 and wro_ans >= 1:
    print(f"\nThat was great! \033[1m{user}\033[0m you did a very great job! your grade is \033[92m{cor_ans}/{items}.\033[0m")
elif cor_ans == 0 and wro_ans >= 0:
    print(f"\nNot everyone is good at the beginning \033[1m{user}\033[0m :> your grade is \033[92m{cor_ans}/{items}.\033[0m")


