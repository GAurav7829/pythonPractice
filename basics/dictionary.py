#dictionary[key] = value
dictionary = {}
dictionary[1] = "Item1"
dictionary[2] = "Item2"
dictionary["Hello"] = "Item3"

print(dictionary)
print(dictionary.values())  # print values
print(dictionary.keys())  # print keys

print(dictionary['Hello'])  # print value of key 'Hello'

newDictionary = {1: 'Item1', 2: 'Item2', 'Hello': 'Item3'}
print(newDictionary)

del newDictionary[1]    #delete with key 1
print(newDictionary)

newDictionary.clear()   #clear dictionary
print(newDictionary)

del newDictionary   #delete entire dictionary