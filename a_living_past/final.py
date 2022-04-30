import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import matplotlib
from matplotlib.markers import MarkerStyle

# 1
for i in range(1,5):
    plt.figure(figsize = (10,10))

    for j in range(0,100):
        plt.scatter(random.uniform(0,1),random.uniform(0,1),s = 100000 * random.uniform(0,1), color = 'none', edgecolors='#FE627E', linewidth = 10, alpha = 0.2)

    plt.axis('equal')
    plt.axis('off')
    plt.ylim((-1,2))
    plt.xlim((-1,2))
    plt.savefig('4+1.' + str(i) + '.png', facecolor='#297CF8', dpi = 1000, bbox_inches='tight')

# 2
plt.figure(figsize = (10,10))

for i in range(0,100):
    plt.scatter(random.uniform(0,1),random.uniform(0,1),s = 100000 * random.uniform(0,1), color = '#EEF3F7', edgecolors='', linewidth = 10, alpha = 0.1)

plt.axis('equal')
plt.axis('off')
plt.ylim((-1,2))
plt.xlim((-1,2))
plt.savefig('4+1.5.png', facecolor='#222222', dpi = 1000, bbox_inches='tight')
