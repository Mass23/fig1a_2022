import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import matplotlib
from matplotlib.markers import MarkerStyle

# wu1
plt.figure(figsize = (10,10))

for i in range(0,100):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    plt.scatter(x ,y , marker = (2, 0, 90 * (x + y)), color = 'teal', linestyle='None', s = 20000)


plt.axis('equal')
plt.axis('off')
plt.ylim((-0.5,1.5))
plt.xlim((-0.5,1.5))
plt.savefig('TA1.png', facecolor='#83CFE1', dpi = 1000, bbox_inches='tight')
print(5)

# wu2
plt.figure(figsize = (10,10))

for i in range(0,100):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    plt.scatter(x ,y , marker = (2, 0, -180 * x * y), color = '#FDEF4F', linestyle='None', s = 20000)


plt.axis('equal')
plt.axis('off')
plt.ylim((-0.5,1.5))
plt.xlim((-0.5,1.5))
plt.savefig('TA2.png', facecolor='#E185A3', dpi = 1000, bbox_inches='tight')
print(6)
