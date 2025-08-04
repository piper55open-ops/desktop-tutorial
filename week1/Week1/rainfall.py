import numpy as np
import calendar
x = np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
print("Sample Data converted to Numpy array: ",x)
a=0
num=0
for i in range (0,7):
    a=a+x[i]
print("The total rainfall for the week is ""%.1f" % a)
b=a/7
print("The average rainfall for the week is: ""%.2f" % b)
for i in range (0,7):
    if x[i]==0:
        num=num+1
print("Number of days with no rain: ",num)

for i in range (0,7):
    if x[i]>=5:
        weekday_name = calendar.day_name[i - 1]
        print("Days with more than 5 mm of rain: ",weekday_name )
