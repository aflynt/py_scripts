import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

csv.register_dialect(\
    'mydialect', delimiter = ',',quotechar = '"', doublequote = True, \
    skipinitialspace = True, lineterminator = '\n' )

filename = 'names.csv'
r0 = []
r1 = []
r2 = []
r3 = []

#with open(filename, newline='\n') as csvfile:
with open(filename, 'r') as f:
  reader = csv.reader(f, delimiter=',')

  # get the header
  headers = next(reader)

  # get all the rows as a list
  data = list(reader)

  # transform data into numpy array
  data = np.array(data).astype(float)

print(headers)
print(data.shape)
print(data[:3])

#plot the data
#for i in range(1,28):
for i in range(1,10):
  plt.plot(data[:,0], data[:,i], label=headers[i])

#plt.plot(data[:,0], data[:,1], label=headers[1])
#plt.plot(data[:,0], data[:,2], label=headers[2])
plt.xlabel(headers[0])
plt.ylabel(headers[1])
plt.legend()
plt.show()

"""

#f1 = savgol_filter(r1, 51, 3) # window size 51, polynomial order 3
#f3 = savgol_filter(r3, 51, 3) # window size 51, polynomial order 3

# save data to file
#with open('output.dat', 'w') as f:
#  f.write('\n'.join('{} {} {}'.format(t[0], t[1], t[2]) for t in zip(r0, r1, f1)))
#  f.close()


plt.xlim(1.1,2.1)
plt.xticks([1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1])

#plt.ylim(-4,4)
plt.xlabel('Time (s)')
plt.ylabel(r'$Forces$ $(N)$')
plt.title('Global Forces')
plt.grid(True)
plt.plot(r0,r1  ,'-', label=r'$F_x (N)$')
plt.plot(r0,r2  ,'-', label=r'$F_y (N)$')
plt.plot(r0,r3  ,'-', label=r'$F_z (N)$')
#plt.plot(r0,r4  ,'-', label='Fy-cf (N)')
#plt.plot(r0,r5  ,'-', label='Fy-d  (N)')
#plt.plot(r0,r6  ,'-', label='Fy-g  (N)')
#plt.plot(r0,r7  ,'-', label='Fz-cf (N)')
#plt.plot(r0,r8  ,'-', label='Fz-d  (N)')
#plt.plot(r0,r9  ,'-', label='Fz-g  (N)')

plt.legend()
plt.savefig('Fx-lab.png')
plt.show()
"""
