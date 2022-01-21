string1 = 'Python is awesome'

print(string1)
print(string1[1])
print(string1[1:4])
print(string1[:4] + ' Bob')

print('Hello\nWorld')   #new line \n

string2 = 'Python is the best'
string3 = string1 + ' ' + string2
print(string3)

var1 = 'Hello'
var2 = 'World'
print('%s is the best %s' %(var1, var2))

lorem = """Lorem Ipsum is simply dummy text of the printing and 
typesetting industry. Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, when an unknown 
printer took a galley of type and scrambled it to make a 
type specimen book. It has survived not only five centuries, 
but also the leap into electronic typesetting, 
remaining essentially unchanged.""" #print text as it is use """
print(lorem)

var4 = 'Hello World'
print(var4.capitalize())
print(var4.upper())
print(var4.lower())