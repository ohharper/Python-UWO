st="RoboGarden" 

for ind in range(len(st)): # break example 

    letter=st[ind] 

    if "g"==letter: 

        break 

    print("current letter is:", letter) 

     

print("The letter 'g' was found in the string at the index=", ind) 

  

  

x= 0 

while x<6: # continue example 

    x+=1 

    if x==3: 

        continue 

    print("Current x value is:", x) 

  

ls=[10,2.6,"hello", 8, 9.1]   

for item in ls: # pass example 

    if item==8: 

        pass 

        print("line after pass statement") 

         

    print("item is:",item) 

  

print("Bye bye")