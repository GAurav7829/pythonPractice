import os

#var1 = input('Enter value: ')
#print(var1)

var2 = open('file.txt','w')    #wb - create file if not exist, w - writable, r - read mode
print(var2)
print(var2.name)

var2.write('Hello Py')  #write content to file
var2.close()
#-----------------------------------------------------
var2 = open('file.txt','r')
string1 = var2.read(2)
print(string1)
string1 = var2.read()
print(string1)

var2.close()
#----------------------------------------------------
#os.rename('file.txt','newName.txt')
#os.remove('newName.txt')

#s.mkdir('folderName')
#os.rmdir('folderName')

