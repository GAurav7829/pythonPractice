myList = ['Hello', 45, 10.9]
print(myList*8) #print list 8 times
print(myList[0])
print(myList[1:3])

myList[0] = 'Bob'   #replace Hello to Bob
print(myList)

#concat list
myList2 = ['World']
myList3 = myList + myList2
print(myList3)

del myList[0]   #delete from list at index 0
print(myList)

print(len(myList))