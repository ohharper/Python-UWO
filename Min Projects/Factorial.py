## n!= n * (n-1) * (n-2) *...* 1

ft= int(input("Find the factortial of the number:"))
x= 1
sum= 1

if ft < 0:
    print ("Enter positive integer")
elif ft == 0:
    print ("The factorial of 0 is 1")
else:
    print("The factorial is:")
    for item in range (1, ft+1):
        x *= item
        sum += x
print (x)

       
        
