#Given three integers, print the smallest one. (Three integers should be user input) 

a=int(input("Enter The first Number"))
b=int(input("Enter The 2nd Number"))
c=int(input("Enter The 3rd Number"))
if (b>a) and (c>a):
 print(f"The Smallest Number is {a}")
elif (a>b) and (c>b):
    print(f"The smallest Number is {b}")
else:
    print(f"The smallest Number is {c}")
    
    
    
