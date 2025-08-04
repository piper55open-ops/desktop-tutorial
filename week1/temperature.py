import numpy as np
list1=[18.5 ,19,20,25.0,2,30,13.9]
num=20
v=np.array(list1)
m=np.average(list1)
print("The average temperature for the week: ",m)
n=np.max(list1)
print("The highest recorded  temperature for the week: ",n)
b=np.array(list1)*9/5 + 32
print("Converted all temperature to Fahrenheit and printed the converted values",b)
c=np.where(np.array(list1)>20)[0]
print("Printed the indices of days where the temperature exceeded 20°C",c)
