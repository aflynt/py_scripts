#!/opt/rh/rh-python36/root/usr/bin/python
import sys
import csv
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

## define csv type
csv.register_dialect(\
    'mydialect', delimiter = ',',quotechar = '"', doublequote = True, \
    skipinitialspace = True, lineterminator = '\n' )

## define reading a csv file with header
def read_file(filename):
  with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')

    # get the header
    headers = next(reader)

    # get all the rows as a list
    data = list(reader)

    # transform data into numpy array
    data = np.array(data).astype(float)

    return headers, data

## read a file
twoFiles = False
filename1 = 'data.csv'

if len(sys.argv) == 2:
  filename1 = sys.argv[1]
  headers, data = read_file(filename1)
if len(sys.argv) == 3:
  twoFiles = True
  filename1 = sys.argv[1]
  filename2 = sys.argv[2]
  headers, data = read_file(filename1)
  h2, d2 = read_file(filename2)
else:
  headers, data = read_file(filename1)

## Assuming csv had x , y , z data
x = data[:,0]
y = data[:,1]
z = data[:,2]

## set plotting limits
xlimL = min(x) - 0.1
xlimH = max(x) + 0.1 
ylimL = min(y) - 0.1
ylimH = max(y) + 0.1

#fig, (ax1, ax2) = plt.subplots(nrows=2)
fig, ax2  = plt.subplots(nrows=1)

# -----------------------
# Interpolation on a grid
# -----------------------
# A contour plot of irregularly spaced data coordinates
# via interpolation on a grid.

# Create grid values first.
#xi = np.linspace(xlimL-0.1, xlimH+0.1, ngridx)
#yi = np.linspace(ylimL-0.1, ylimH+0.1, ngridy)
#
## Perform linear interpolation of the data (x,y)
## on a grid defined by (xi,yi)
#triang = tri.Triangulation(x, y)
#interpolator = tri.LinearTriInterpolator(triang, z)
#Xi, Yi = np.meshgrid(xi, yi)
#zi = interpolator(Xi, Yi)

# Note that scipy.interpolate provides means to interpolate data on a grid
# as well. The following would be an alternative to the four lines above:
#from scipy.interpolate import griddata
#zi = griddata(x, y), z, (xi[None,:], yi[:,None]), method='linear')


#ax1.contour(xi, yi, zi, levels=14, linewidths=0.5, colors='k')
#cntr1 = ax1.contourf(xi, yi, zi, levels=14, cmap="RdBu_r")
#
#fig.colorbar(cntr1, ax=ax1)
#ax1.plot(x, y, 'ko', ms=3)
##ax1.set(xlim=(-2, 2), ylim=(-2, 2))
#ax1.set(xlim=(xlimL, xlimH), ylim=(ylimL, ylimH))
#ax1.set_title('grid and contour (%d points, %d grid points)' %
#                  (npts, ngridx * ngridy))


# ----------
# Tricontour
# ----------
# Directly supply the unordered, irregularly spaced coordinates
# to tricontour.

ax2.tricontour(x, y, z, levels=14, linewidths=0.5, colors='k')
cntr2 = ax2.tricontourf(x, y, z, levels=14, cmap="RdBu_r")

fig.colorbar(cntr2, ax=ax2)
ax2.plot(x, y, 'ko', ms=3)
ax2.set(xlim=(xlimL, xlimH), ylim=(ylimL, ylimH))
ax2.set_title('tricontour ')

#plt.subplots_adjust(hspace=0.5)
plt.show()
