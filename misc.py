def num_decrease(n):
    print(n)
    if n > 1:
        return num_decrease(n-1)

def num_increase(start, end):
    print(start)
    if start < end:
        return num_increase(start+1, end)
        
num_increase(5, 10)
