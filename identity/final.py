import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd

plt.figure(figsize = (10,10))
im = Image.open("gmap1.png").convert('L')
size = 400,400
im_resized = im.resize(size, Image.ANTIALIAS)
pix = im_resized.load()

for y in range(0,400):

    row = []
    for x in range(0,400):
        row.append(int(pix[x,y]))

    row_mean = np.mean(row)

    data_x = [i for i in range(0,400)]
    data_y = (-(row - row_mean) / 20) + (400 - y)

    plt.plot(data_x,data_y,'-', c='#1C7FE8',alpha=1, linewidth = 0.5)

plt.axis('off')
plt.savefig('GMAP1_processed.png', facecolor='#F0EED4', dpi = 1000, bbox_inches='tight')

plt.figure(figsize = (10,10))
im = Image.open("gmap2.png").convert('L')
size = 400,400
im_resized = im.resize(size, Image.ANTIALIAS)
pix = im_resized.load()

for y in range(0,400):

    row = []
    for x in range(0,400):
        row.append(int(pix[x,y]))

    row_mean = np.mean(row)

    data_x = [i for i in range(0,400)]
    data_y = (-(row - row_mean) / 20) + (400 - y)

    plt.plot(data_x,data_y,'-', c='#E85458',alpha=1, linewidth = 0.5)

plt.axis('off')
plt.savefig('GMAP2_processed.png', facecolor='#F0EED4', dpi = 1000, bbox_inches='tight')

plt.figure(figsize = (10,10))
im = Image.open("gmap3.png").convert('L')
size = 400,400
im_resized = im.resize(size, Image.ANTIALIAS)
pix = im_resized.load()

for y in range(0,400):

    row = []
    for x in range(0,400):
        row.append(int(pix[x,y]))

    row_mean = np.mean(row)

    data_x = [i for i in range(0,400)]
    data_y = (-(row - row_mean) / 20) + (400 - y)

    plt.plot(data_x,data_y,'-', c='#F0EED4',alpha=1, linewidth = 0.5)

plt.axis('off')
plt.savefig('GMAP3_processed.png', facecolor='#703050', dpi = 1000, bbox_inches='tight')
