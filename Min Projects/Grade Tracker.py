Math= float(input("Enter Math grade here:"))
English= float(input("Enter English grade here:"))
ls= [Math, English]

def Average(ls):
    if len(ls) == 0:
        return "list empty"
    total= sum(ls)
    length= len(ls)
    print ("Average grade:", total/length)
Average(ls)