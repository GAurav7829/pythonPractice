var1 = 'Hello World'

for var in var1:
    if(var==' '):
        print('there was a space')
        break
    print(var)

for var in var1:
    if(var==' '):
        print('there was a space')
        continue
    print(var)

var2 = 100
while(var2 < 110):
    print('less than 110: '+str(var2))
    var2 += 1
else:
    print('not less than 110')
