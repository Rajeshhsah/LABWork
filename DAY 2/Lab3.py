#Given the integer N - the number of minutes that is passed since midnight - how many
#hours and minutes are displayed on the 24h digital clock?

N=int(input("Enter the Minutes"))
Hours = N//60
Minutes = N%60
print(f"The display on 24h Digital clock in hours and Minutes :- {Hours}{Minutes}") 


