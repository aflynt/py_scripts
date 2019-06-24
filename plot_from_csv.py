import csv
import matplotlib.pyplot as plt
#import numpy as np

csv.register_dialect(\
    'mydialect', delimiter = ',',quotechar = '"', doublequote = True, \
    skipinitialspace = True, lineterminator = '\n' )

filename = 'names.csv'
r0 = []
r1 = []
r2 = []

#with open(filename, newline='\n') as csvfile:
with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile)

#trying to skip the header
  next(csvreader)

  for row in csvreader:
    r0tmp = row[0]
    r1tmp = row[1]
    r2tmp = row[2]
    #print(', '.join(row))
    r0.append(float(r0tmp))
    r1.append(float(r1tmp))
    r2.append(float(r2tmp))

  print("Total no. of rows: %d"%(csvreader.line_num))

# had to pop the headers
#r0.pop(0)
#r1.pop(0)
#r2.pop(0)

# printing the field names
#print("Now r0")
#print(r0)
#print("Now r1")
#print(r1)
#print("Now r2")
#print(r2)
#print('Field names are:' + ', '.join(field for field in fields))


#x = np.linspace(-10,10,100)
#y = np.sin(x)
#plt.plot(r0,r1,marker="x")
plt.xlabel('Time (s)')
plt.ylabel('alpha')
plt.title('Angular Acceleration')
plt.grid(True)
plt.plot(r0,r1,'r-')
plt.show()
