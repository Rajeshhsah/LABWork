#Given a positive real number, print its fractional part. 

a=4.5
b= a- int(a)
c=(a-b)
print (f"The Fraction Nominator {c}")
print (f"The Fraction Dominator {b}")

#another method 
#Given a positive real number, print its fractional part. 

import math
a=float(input("Enter the number:"))
x,y = math.modf(a)
print(x)
print(y)