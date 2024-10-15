a = 14            # 14 = 0000 1110
b = 69            # 69 = 0100 0101
 
# Binary AND
c = a & b        # 4 = 0000 0100
print ("a & b : ", c)
 
# Binary OR
c = a | b        # 79 = 0100 1111
print ("a | b : ", c)
 
# Binary XOR
c = a ^ b        # 75 = 0100 1011
print ("a ^ b : ", c)
 
# Binary Ones Complement
c = ~a           # -15 = 1111 0001
print ("~a : ", c)
 
# Binary Left Shift
c = a << 2       # 56 = 0011 1000
print ("a << 2 : ", c)
 
# Binary Right Shift
c = a >> 2       # 3 = 0000 0011
print ("a >> 2 : ", c)