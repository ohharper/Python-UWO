num1 = 0
num2 = 1
count = 0

nterms = int(input("How many counts?"))

if nterms <= 0:
    print ("Enter a positive integer")
elif nterms == 1:
    print ("Fibonacci sequence:", num1)
else:
    print ("Fibonacci sequence:")
    while count < nterms:
        print (num1)
        nth = num1 + num2
        num1 = num2
        num2 = nth
        count += 1
