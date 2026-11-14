from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import time
hdul = fits.open("AndromedaGal261029055127 (1).FITS")
header = hdul[0].header
image = hdul[0].data
print(header['OBJECT'])
plt.figure(figsize = (8, 8))
plt.imshow(image, cmap = 'viridis', origin = 'lower', vmax = 500, vmin = 270)
plt.xlabel('X Axis (Columns)')
plt.ylabel('Y Axis (Rows)')
plt.show()
im = plt.imshow(image, cmap = 'viridis')
print(im.get_cmap().name + ": Algorithm Filter used: Processed")

time.sleep(1)
print(header['FILTER'])
plt.figure(figsize = (8, 8))
plt.imshow(image, cmap = 'gray', origin = 'lower', vmax = 580, vmin = 200)
plt.xlabel('X Axis (Columns)')
plt.ylabel('Y Axis (Rows)')
plt.show()
im = plt.imshow(image, cmap = 'gray')
print(im.get_cmap().name + ": Algorithm Filter used: Processed")
time.sleep(1.2)
print("Processed Images are there! Thank you")
hdul.close()
