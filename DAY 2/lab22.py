#convert seconds
S = int (input("enter the value for second:"))
Day = (((S/60) /60) /24)
print(f"total day for given seconds: {Day}")
Hour = ((S/60)/60)
print (f"total hous for given seconds:{Hour}")
Minute = (S /60)
print (f"total minutes for given second:s{Minute}")