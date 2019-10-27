import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


#delta = 0.025
#x = np.arange(-3.0, 3.0, delta)
#y = np.arange(-2.0, 2.0, delta)
#X, Y = np.meshgrid(x, y)
#Z1 = np.exp(-X**2 - Y**2)
#Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
#Z = (Z1 - Z2) * 2
#
#fig, ax = plt.subplots()
#CS = ax.contour(X, Y, Z)
#ax.clabel(CS, inline=1, fontsize=10)
#ax.set_title('Simplest default with labels')

grid_x, grid_y = np.mgrid[0:1:5j, 0:1:10j]

print(grid_x)
print(grid_y)

def func(x,y):
  return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2

points = np.random.rand(20,2)
values = func(points[:,0], points[:,1])

print(points)
print(values)

