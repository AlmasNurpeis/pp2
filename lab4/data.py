from datetime import datetime , timedelta , date , time
import datetime as dt
#1 Write a Python program to subtract five days from current date.
for i in range(5): 
    tomorrow = datetime.now() + timedelta(days=i)
    print(tomorrow) 
#2 Write a Python program to print yesterday, today, tomorrow.
for i in range(-1, 2): 
    days = datetime.now() + timedelta(days=i)
    print(days)
#3 Write a Python program to drop microseconds from datetime.
tim = str(datetime.now())
tim1 = tim.split(".")
print(tim1[0])
#4 Write a Python program to calculate two date difference in seconds
a = datetime.now()
b = tomorrow = datetime.now() + timedelta(days=1)
print((b-a).total_seconds())