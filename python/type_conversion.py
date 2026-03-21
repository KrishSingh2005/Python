# Two types of types converion 
# 1. conversion = that is done automatically by python interpreter
# 2. casting = that is doing by ourself or manually

# Conversion = when we convert the one data type into another data type

a = 1 # it siomply convert or integer data type into float data type
b = 4.5
print (a + b)

# Casting = that is doing manually

    #c = "1" # now that time interreter gives the erroe coz we don't dd string into float 
   # d = 3.8 # so we wan t to chnage tha data type of c variable
   # print (c + d)

# so how to write it

c = int("2") # humne yha c ka data type hi change kr diya hume jis data type ka use banana h usko aage likh              
d = 4.5       # denge aur jisko krna chata h usko bracket m 
print(c+ d)

# Exceptional case in casting 

#e = "krish" # agr mai yha e k data type ko change kru aur mai chata hu jaise e ko float m change krna ya
#f = 3.7     # int m toh wo pssible nhi h add krna conversion bhi hamra fit baithna chaiye hum kisi ko bhi 
#print = (e + f) # kisi m bhi convert ni kr skte

e = float"krish"
f = 3.7
print(e + f)
