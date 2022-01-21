myList = ['Hello', 10, 90.8,'World']

print(myList)
myList[3] = 6
print(myList)


myTuple = ('Hello', 10, 90.8,'World')
print(myTuple)
#myTuple[3] = 6  #Error: object does not support item assignment
print(myTuple)
print(myTuple[1:4])

print(len(myTuple))

del myTuple #delete whole tuple
#print(myTuple) #Error: as myTuple is deleted