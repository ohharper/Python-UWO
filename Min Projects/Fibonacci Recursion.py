def fibonacci_rec(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_rec(n-1) + fibonacci_rec(n-2))
    

n = int(input("How many counts?:"))
if n <= 0:
    print ("Enter a positive integer")
else:
    for i in range(n):
        print (fibonacci_rec(i))
