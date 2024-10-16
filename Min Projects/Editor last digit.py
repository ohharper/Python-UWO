def main ():
    num=27
    LastDigit= num%10
    if LastDigit%3 == 0:
        print ("True")
    else:
        print ("Fasle")

    divisible = (LastDigit%3)
    return divisible

main()