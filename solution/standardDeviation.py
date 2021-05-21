import csv
import math
with open('Standard_deviation-master/solution/data.csv', newline='') as f:
         reader = csv.reader(f)
         file_data = list(reader)

data=file_data[0]

def mean (data):
    total=0
    n=len(data)
    for x in data:
        total=total+int(x)
    mean=total/n
    return mean



#squaring and getting the values
squared_list=[]
for number in data:
    a = int (number)-mean(data)
    a = a**2 
    squared_list.append(a)

#getting sum 
sum=0
for i in squared_list:
    sum=sum+i

#dividing the sum by total value
result = sum/(len(data)-1)

#standard deviation 
std_deviation=math.sqrt(result)
print("Standard Deviation :" +str(std_deviation))

