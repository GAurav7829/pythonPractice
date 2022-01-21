def awesomeFunction():
    print('Hello World!!')
    print('From function')

awesomeFunction()

def add(num1, num2):
    res = num1 + num2
    return res

print('Result: ',add(2,9))

var1 = 2
def changeVal(num1):
    num1 = 4    #change locally, not change var1 val
    return

changeVal(var1)
print(var1)

def defaultVal(num1 = 5):
    return num1 * 2

print(defaultVal())
print(defaultVal(6))