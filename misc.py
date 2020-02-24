#Recursive Functions Test
#Author: Eveshogweyore Alle

#Decrease any give value down to 1
def num_decrease(n):
    print(n)
    if n > 1:
        return num_decrease(n-1)

#Increase any given value by 1
#provided the the start and
#end point is explicitly given
def num_increase(start, end):
    print(start)
    if start < end:
        return num_increase(start+1, end)

num_decrease(10)  
num_increase(0, 10)
