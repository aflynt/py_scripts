#!/opt/rh/rh-python36/root/usr/bin/python
from datetime import date
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, WEEKLY, WE

import csv
import matplotlib.pyplot as plt
import numpy as np

csv.register_dialect(\
    'mydialect', delimiter = ',',quotechar = '"', doublequote = True, \
    skipinitialspace = True, lineterminator = '\n' )

filename = 'time_series_19-covid-Confirmed.csv'
r0 = []
r1 = []
r2 = []
hdr = []
country = []

#keyCountry = 'US'
#keyCountry = 'China'
keyCountry = 'Italy'

#   0          1      2     3     4        N
# Province, Country, LAT, LONG, DATE0 ... DATE N


#with open(filename, newline='\n') as csvfile:
with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  dates = next(csvreader)[4:]
  print(dates)
#trying to skip the header
#  next(csvreader)

  # find the row of interest aka keyCountry
  for row in csvreader:
    if row[1].find(keyCountry) != -1:
      cname = row[1]
      country = row[4:]
      print(cname, ' with dates: ', country)

# try to parse the dates
today = date.today()
dlist = []
for d in dates:
  dvals = d.split('/')
  mo = int(dvals[0])
  dy = int(dvals[1])
  yr = int(2020)
  dobject = date(day=dy,month=mo,year=yr)
  delta = int((dobject - today).days)
  dlist.append(delta)








#x = np.linspace(-10,10,100)
#y = np.sin(x)
#plt.plot(dates,country,marker="x")
plt.plot(dlist,country,marker="x")
#plt.plot(x,y,marker="x")
plt.yscale("log")
plt.xlabel('Time (s)')
plt.ylabel('alpha')
plt.title('Angular Acceleration')
plt.grid(True)
plt.plot(r0,r1,'r-')
plt.savefig("test.pdf")
plt.show()
