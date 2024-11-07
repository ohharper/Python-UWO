file= open("Diary.txt", "r+")
file.write(input(str("Enter new diary entry here:")))  #create new diary entry

diary= file.read()
print (diary)

