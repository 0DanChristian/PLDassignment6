first_ = int(input("enter first: "))
second_ = int(input("enter second: "))
third_ = int(input("enter third: "))

if first_ < second_ :
    if second_ < third_ :
        min, mid, max = first_, second_, third_
    else: 
        min, mid, max = first_, second_, third_
    
elif second_ < first_ and second_ < third_:
    if first_ < third_:
        min, mid, max = first_, second_, third_
    else:
        min, mid, max = first_, second_, third_
    
else:
    if first_ < second_:
        min, mid, max = first_, second_, third_
    else:
        min, mid, max = first_, second_, third_

print("From highest to lowest based from the given numbers, the first one is", min, end='')
print(", second is ", mid, end='')
print(", and lastly, ", max, end='')
print(".")