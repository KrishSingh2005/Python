# Arithemtic Opeartors

a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # % = call it modulo and use for find remainder
print(a ** b) # ** use for power means a ratio the power b 


# Relational operators = used for comparison betwwn two values
# it gives us output  only in true or false

a = 50 
b = 20

print ( a == b) # it means a is equal to b it is not so it gives in output is false

print (a != b) # it means a is not equal to b it is yes  so it gives in output is true
print (a >= b)
print (a > b)
print (a <= b)
print (a < b)

# Assingnment operators

num = 10 # ye += ussi variable k andr ki valu ko add kr deta h 
num += 10 # jaise isne yha num variable k andr hi 10 ko add kr diya 
print ("num :", num) # output : 20

num = 10
num -= 10
print ("num :", num) # output : 0
num = 10
num *= 10
print ("num :", num) # output : 100
num = 10
num /= 10
print ("num :", num) # output : 1.0
num = 10
num %= 10
print ("num :", num) # output : 0
num = 10
num **= 10
print ("num :", num) # output : 10000000000

# Logical operator

 #NOT operator
print(not True) # not operator gives us opposite value
print(not False) 
 #using in condition
a = 50
b = 20
print(not (a > b))

#AND operator
val1 = True # When both are true then then the output is true 
val2 = True
print (val1 and val2)

val3 = True  
val4 = False
print ( "AND operator of val3 and val4 is " , val3 and  val4)

val5 = False  
val6 = False
print ( "AND operator of val5 and val6 is " , val5 and  val6)

a = 50
b = 30
print( (a==b) and (a>b))

#OR operator
val7 = True # If one is true then output is true
val8 = False
print ("Or opearator of val7 and val8 is", val7 or val8)

val9 = True 
val10 = True
print ("Or opearator of val9 and val10 is", val9 or val10)

val11 = False 
val12 = False
print ("Or opearator of val11 and val12 is", val11 or val12)

a = 70
b = 40
print((a==b) or (b<a))







