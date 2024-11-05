

def main(): 

        dictionary={"a": "apple", "b":"banana"} 

        key="c" 

        try:
                print (dictionary['key'])
                return True
        
        except KeyError:
                print ("False")
                return False

  

main() 