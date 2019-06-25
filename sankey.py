import matplotlib.pyplot as plt

from matplotlib.sankey import Sankey

Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['','', '', 'first', 'second', 'third', 'fourth', 'fifth'],
       orientations=[-1, 1 , 0 , 1,1,1,0,-1]).finish()
plt.title("The default settings produce a diagram like this.")

plt.show()
