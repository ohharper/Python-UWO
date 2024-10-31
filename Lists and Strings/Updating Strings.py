st1="hello everyone" 

st2="RoboGarden" 

st3="hi" 

  

## assign one string to another string 

st3=st2 

print("st2=", st2) 

print("st3=", st3) 

  

##change string with its previous content 

print("The original value of st1=",st1) 

st1=st1[0:3]+" Python" 

print("After modification: st1=",st1) 

  

## Try to change the entire content of the string 

st1[0]="f" 

print("st1=",st1)