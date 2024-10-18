ls= [7,"Hello", 2.5] 

st="RoboGarden" 

  

for item in ls: #iterate over a list 

    print("item:", item) 

     

for letter in st: 

    print("letter:", letter)


#Iterating by index
ls= [7,"Hello", 2.5] 

for ind in range(len(ls)): #iterate over a list 

    print("index:",ind,"item:", ls[ind])