# arithmetic operator
a = 5
b = 2 

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b) #exponent/power

# relational operator 
a = 50
b = 20

print(a == b) #false
print(a != b) #true
print(a > b) #true
print(a >= b) #true
print(a < b) #false
print(a <= b) #false

#Assignment operator
num = 10
num /= 5 #    /= , -= , += , %= **=
print("num :",num)

# Logical operator 
"""NOT Operator"""
a = 40
b = 39
print(not False)
print(not (a > b))

"""AND Operator"""
val1 = True
val2 = False
print("and operator:", val1 and val2) #And operator will always be true in case of TT otherwise false in TF, FT, FF

"""OR operator"""
print("or operator:", val1 or val2) # OR operator will be false in FF otherwise true in TT, TF, FT
print("or operator:", (a == b) or (a > b))
