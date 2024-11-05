ls=[2,19,3, "hello", 3, 9.2]
print("ls=", ls)
print("len(ls)=", len(ls)) # length of list
ls.append(20)  #Adds an item to the list
print("ls=",ls)
ls2=["hi", "welcome"]
ls.extend(ls2) # Adds sequence to the list
print("ls=",ls)
 
ls3=[2,8,2,11,1,7]
print("max(ls3)=", max(ls3)) # maximum value of the list
print("min(ls3)=", min(ls3)) # minimum value of the list
ls3.sort() # sort list in ascending order
print("ls3.sort():", ls3) 
ls3.insert(2,15) # insert value at a specific index
print("ls3.insert(15,2):",ls3)
print("ls3.index(15)=", ls3.index(15)) # get index