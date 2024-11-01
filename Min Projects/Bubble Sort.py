ls= [3,5,73,31,748,4,9,90,8766,68,6587,4579,7865]
for n in range(len(ls) -1, 0, -1):
    for i in range(n):
        if ls[i] > ls[i+1]:
            ls[i], ls[i+1]= ls[i+1], ls[i]

print (ls)
