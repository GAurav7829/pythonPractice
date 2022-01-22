import re   #regular expression


#match
pattern = re.compile('ell')
print(pattern.match('Hello World'))
print(pattern.match('Hello World', 1))

result = pattern.match('Hello World', 1)
print(result.span())    #return (1, 4)

#search
print(pattern.search('Hello World'))

#Advance Search
string1 = 'Hello world is awesome'
result = re.search(r'(.*) world (.*?) .*', string1, re.M|re.I)    #pattern, string, flag(re.M = multiline, re.I = case insenstitive)
if(result):
    print(result.group())
else:
    print('No result')

#search and replace
string2 = '121212ef4322345435eftgfdgdftyret454'
result = re.sub(r'\D', " ", string2) #remove characters  #pattern, replaced string, string to search
print(result)   #only numbers will display