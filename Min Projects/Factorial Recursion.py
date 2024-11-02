def factorial_recursion(n):
    if n < 0:
        return ("Enter positive integer")
    elif n == 0 or n == 1:
        return 1
    else:
        return n*factorial_recursion(n-1)


