def Average(ls):
    if len(ls) == 0:
        return "list empty"
    total= sum(ls)
    length= len(ls)
    return total/length

ls =[1,4]
print (Average(ls))