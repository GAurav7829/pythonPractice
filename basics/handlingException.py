
#assert statement
def fun1(var1):
    assert(var1 != 0), "Zero is Invalid"    #if var1 = 0, show this
    return 10 / var1

#print(fun1(0))
print(fun1(5))

try:
    file = open('text.txt', 'w')
    file.write('Hello...')
except IOError:
    print('File not Found')
else:
    print('File Found.')
    file.close()