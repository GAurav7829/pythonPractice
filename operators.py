# arithmatic operators  ------------------------------------
print(5 + 6)
print(5 - 6)
print(5 * 6)
print(5 / 6)
print(5 % 6)
print(5**2)  # square of 5
print(17//3)  # quotient ans 5

# comparasion operators ------------------------------------
print(5 == 5)
print(5 != 5)
print(5 > 6)
print(5 < 6)
print(5 >= 6)
print(5 <= 6)

# assignment operators  ------------------------------------
var1 = 5 + 6
print(var1)
var2 = var1 + 3
print(var2)

var1 += 5
print(var1)

# bitwise operators  ------------------------------------
var1 = 13  # 1101
var2 = 5  # 0101

# AND         0101
print(var1 & var2)  # 5

# OR          1101
print(var1 | var2)  # 13

# XOR         1000
print(var1 ^ var2)  # 8

# Once Compliment
print(~var1)  # -14

# Binary shift left
print(var1 << 1)
# Binary shift right
print(var1 >> 1)

#logical operator   ------------------------------------
var1 = True
var2 = True
var3 = False
var4 = False
print("AND operator*****")
print(var1 and var2)
print(var1 and var3)
print(var3 and var4)
print("OR Operator*****")
print(var1 or var2)
print(var1 or var3)
print(var3 or var4)
print("NOT Operator*****")
print(not(var1))
print(not(var3))

#membership operator    ------------------------------------
string1 = 'Hello World!'
print('Membership operator*****')
print('H' in string1)
print('Z' in string1)

print('H' not in string1)
print('Z' not in string1)

#identity operator  ---------------------------------------
var1 = 10
var2 = 10
var3 = 5
print("Identity Operator*****")
print(var1 is var2)
print(var1 is var3)

print(var1 is not var2)
print(var1 is not var3)

