# Strings and Numeric values can operate togather with *
a , b = 2,3
txt = "@"
print(2*txt*3)

# Strings and strings can operate with +
a , b = "2",3
txt = "@"
print((a+txt)*b)

# Numeric values can operate with all arithmetic operations
a , b = 2,3
txt = 4
print(2+4*3)

# Arithmetic operations with integers and floats will result in float
a , b = 2,3.0
txt = a*b
print(txt)

# Result of division operator with two integer will be in float
a , b = 10,2
txt = a/b
print(txt)

# Integer divison with float and int will give int but displayed as a float
a , b = 1.5,3
txt = a//b
print(txt)




