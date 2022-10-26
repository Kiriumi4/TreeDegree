import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from PIL import Image
buildArr=np.zeros((10,10)) #Array to hold all building data

cmap = colors.ListedColormap(['0.5','0.1','lightgreen','0.8','brown'])
bounds=[0,1,2,3,4,5]
norm = colors.BoundaryNorm(bounds, cmap.N)
buildArr[1]=1
buildArr[2]=2
buildArr[3]=3
buildArr[4]=4
print(buildArr)
plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
plt.savefig('square.png',transparent=True)
plt.show()