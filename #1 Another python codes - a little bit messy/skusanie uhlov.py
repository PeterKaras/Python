import math
a = 1/2
b = math.pi/6
#radiany!
print(b)
print("Sin",math.degrees(math.sin(a)))
print("Cos",math.cos(a))
print("Tan",math.tan(a))
print("Cotg",math.atan(a))



radians = 0.5
degrees = math.degrees(radians)
#print(((degrees)*180)/math.pi)
b = 3
c = 4
#print(((math.sin(degrees))*180)/math.pi)
print ("The value of hypotenuse of 3 and 4 is : ", end="") 
print (math.hypot(b,c))
tu = math.degrees(math.atan2(2,2))#funguje to 
print(tu)

x = 2
y = 2
tangens = math.degrees(math.atan2(y, x))
if tangens < 0:
    tangens = 360 + tangens
else:
    pass
print("Funguje to!",tangens)
