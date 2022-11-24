import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from PIL import Image


####### Modul zawiera testy innych funkcji nie jest uzywany w programie wlasciwym!!!



owo= np.array([[3,2],[1,3],[2,2],[2,3],[2,4],[3,8],[3,3],[3,4],[3,5]])
owo1= [[3,2],[1,3],[2,2],[2,3],[2,4],[3,8],[3,3],[3,4],[3,5]]





grass= np.array([[4,5],[5,5],[5,9],[3,6],[5,6],[5,7],[4,6],[5,8],[3,7],[4,7],[3,8],[3,9],[4,8],[4,9]])

print(grass)
grass=grass[grass[:,1].argsort()]
grass=grass[grass[:,0].argsort()]   
print(grass)
#size=11
#data=np.zeros((size,size))

##print(data)
#width, height = size, size
#coords=np.array([[]])
#a, b = int(size/2),int(size/2)
#r = int(size/2)
#data[a][b]=1
#for angle in range(0, 360, 5):
#    x = r * math.sin(math.radians(angle)) + a
#    y = r * math.cos(math.radians(angle)) + b
    
#    data[int(round(y))][int(round(x))] = 1
# #nie dziala v
#def fill_circle(grid,a,b,r):
#    return 0;

#fill_circle(data,a,b,r)
#print(data)
