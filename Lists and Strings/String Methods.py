string="robo,garden,John,Ali" 

print("string=", string) 

print("length of the string=",len(string)) #return the length of the string  

ls=string.split(",") # divide string into multiple substrings based on the ',' delimiter  

print("ls=",ls) 

st=ls[1].capitalize() # capitalize the first letter of the string  

print("st=",st)