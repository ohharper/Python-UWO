dict1= {"h": "hello","w": "welcome","r":"RoboGarden"}
print("dict1=", dict1)
	
dict1["j"]="John" # adding a new entry to the dictionary
print("dict1=", dict1)
 
dict1['h']="hi" # modify an existing entry 
print("dict1=", dict1)
 
del dict1['w']  # delete an existing entry
print("dict1=", dict1)
 
dict1.clear()  # remove all entries in the dictionary
print("dict1=", dict1)
 
del dict1  # delete the dictionary itself
print("dict1=", dict1)