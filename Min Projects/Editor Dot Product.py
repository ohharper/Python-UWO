def main():
    list_1 = [2, 7, 4, 6, 2]
    list_2 = [1, 6, 3, 5, 1]
    
    i=-1
    dot_product =0
   
    while i < 4:     
        i += 1
        a = list_1[i] * list_2[i]
        #dot_product= dot_product + list_1[i+1] * list_2[i+1]
        dot_product += a
    
    print (dot_product)
    return dot_product
    
main()