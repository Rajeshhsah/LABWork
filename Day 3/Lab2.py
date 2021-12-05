#WAP which accepts marks of four subjects and display total marks, percentage and grade. 
# Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 

a=int(input("Enter the first Subject Marks : "))
b=int(input("Enter the second Subject Marks : "))
c=int(input("Enter the Third Subject Marks : "))
d=int(input("Enter the Fouth Subject Marks : "))
e=(a+b+c+d)
TotalPercentage =(e/400)*100
print(f"The Total Marks is {e}")
print(f"Total Percentage is {TotalPercentage}%")
if (TotalPercentage>=70):
    print("You have got Distinction")
elif(TotalPercentage>=60):
    print("You have got First Division")
elif(TotalPercentage>=40):
    print("You have got second Division")
else:
    print("You have Failed")
    
      