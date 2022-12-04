from distutils.command.check import check
from lib2to3.pgen2.token import CIRCUMFLEX
import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from PIL import Image


####### Modul zawiera testy innych funkcji nie jest uzywany w programie wlasciwym!!!



owo= np.array([[3,2],[1,3],[2,2],[2,3],[2,4],[3,8],[3,3],[3,4],[3,5]])
#owo1= [[3,2],[1,3],[2,2],[2,3],[2,4],[3,8],[3,3],[3,4],[3,5]]





#grass= np.array([[4,5],[5,5],[5,9],[3,6],[5,6],[5,7],[4,6],[5,8],[3,7],[4,7],[3,8],[3,9],[4,8],[4,9]])

#print(grass)
#grass=grass[grass[:,1].argsort()]
#grass=grass[grass[:,0].argsort()]   
#print(grass)
#size=9
data=np.zeros((20 ,20))

##print(data)
#width, height = size, size
#coords=np.array([[]])
#a, b = int(size/2),int(size/2)
#r = int(size/2)
#data[a][b]=1
#for angle in range(0, 360, 5):
#    x = r * math.sin(math.radians(angle)) + a
#    y = r * math.cos(math.radians(angle)) + b
#    xr=int(round(x))
#    yr=int(round(y))
#    if xr<a and yr<b:
#        for i in range(yr,b):
#            for j in range(xr,a):
#                data[i][j] = 1
#    elif xr<a and yr>b:
#        for i in range(b,yr+1):
#            for j in range(xr,a):
#                data[i][j] = 1
#    elif xr>a and yr>b:
#        for i in range(b,yr+1):
#            for j in range(a,xr+1):
#                data[i][j] = 1
#    elif xr>a and yr<b:
#        for i in range(yr,b):
#            for j in range(a,xr+1):
#                data[i][j] = 1


# #nie dziala v
##def fill_circle(grid,a,b,r):
##    return 0;
##fill_circle(data)
##fill_circle(data,a,b,r)
#print(data)



def checkFound(coord,coordTab):

    for i in range (0,len(coordTab)):
        if coord[0]==coordTab[i][0] and coord[1]==coordTab[i][1]:
            return True
    return False

def circle( center, radius):
    circlecoords=np.array([])
    a=center[0]
    b=center[1]
    for angle in range(0, 360, 5):
        x = radius * math.sin(math.radians(angle)) + a
        y = radius * math.cos(math.radians(angle)) + b
        xr=int(round(x))
        yr=int(round(y))
        
        
            
        if xr<a:
                for j in range(xr,a):
                    if not checkFound((yr,j),circlecoords):
                        circlecoords=np.resize(circlecoords,(len(circlecoords)+1,2))
                        circlecoords[len(circlecoords)-1][len(circlecoords[0])-2]=yr
                        circlecoords[len(circlecoords)-1][len(circlecoords[0])-1]=j
        elif xr>a :
            
                for j in range(a,xr+1):
                    if not checkFound((yr,j),circlecoords):
                        circlecoords=np.resize(circlecoords,(len(circlecoords)+1,2))
                        circlecoords[len(circlecoords)-1][len(circlecoords[0])-2]=yr
                        circlecoords[len(circlecoords)-1][len(circlecoords[0])-1]=j
      
    
    return circlecoords
size=10
a=circle((10,10),int(size/2))
print(a)
for i,j in a:
    #print(i,j)
    data[int(i)][int(j)]=1

print(data)

