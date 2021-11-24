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
