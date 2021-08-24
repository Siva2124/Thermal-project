from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from osgeo import gdal

#Get the thermal Sampling figure
ds = gdal.Open('FLIR0981.tif')

myarray = np.array(ds.GetRasterBand(2).ReadAsArray())


dem=myarray
ny, nx = dem.shape

x = np.linspace(-3, 3, nx)
y = np.linspace(-3, 3, ny)


X,Y = np.meshgrid(x,y)

#Z value is used for seperate Thermal heat and cool in the given Sample
Z = x*np.exp(-X**2 - Y**2)

fig = plt.figure(figsize=(8,6))

#set to 3D projection
ax = fig.add_subplot(111, projection='3d')
dem3d=ax.plot_surface(X,Y,Z,cmap='jet') #X=xv Y=yv

ax.set_title('THERMAL GRAPH')
ax.set_zlabel('Elevation of Temperature ')

# Display the Thermal Graph
plt.show()
























