import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from PIL import Image


####### Modul zawiera testy innych funkcji nie jest uzywany w programie wlasciwym!!!



#buildArr=np.zeros((10,10)) #Array to hold all building data

#cmap = colors.ListedColormap(['0.5','0.1','lightgreen','0.8','brown'])
#bounds=[0,1,2,3,4,5]
#norm = colors.BoundaryNorm(bounds, cmap.N)
#buildArr[1]=1
#buildArr[2]=2
#buildArr[3]=3
#buildArr[4]=4
#print(buildArr)
#plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
#plt.savefig('square.png',transparent=True)
#plt.show()

owo= np.array([[3,2],[1,3],[2,2],[2,3],[2,4],[3,8],[3,3],[3,4],[3,5]])
owo1= [[3,2],[1,3],[2,2],[2,3],[2,4],[3,8],[3,3],[3,4],[3,5]]
#owo=['-EDITBTN1-','-EDITBTN2-','-EDITBTN3-','-EDITBTN4-','-EDITBTN5-']
#print(owo)
#for opt in enumerate(owo):
#    print(opt[0])
#print(owo)
#print(len(owo))
#print(len(owo[0]))
#print(len(owo[1]))

#owo1.sort(key=lambda row:(row[0],row[1]),reverse=False)
#print(owo1)
##owo=owo[owo[:,0].argsort()]
#owo=owo[owo[:,1].argsort()]
#owo=owo[owo[:,0].argsort()]
#ind=np.lexsort((owo[:,0],owo[:,1]))
#owo[ind]
#ind = owo[:,1].argsort(kind='stable')
#owo[ind]
print(owo)
print(owo[:,0])
print(np.count_nonzero(owo[:len(owo)-1][0] == 3))




#for i,value in enumerate(owo):
#    print(i,value)

#for i in owo:
#    print(i) 
#    if value[0]==1 and value[1]==3:
#         #print('a')
#         owo=np.delete(owo, i,axis=0)

#print(owo)

#hemlo=np.array([[1,3]])
#print(hemlo)
#print(len(hemlo))
#hemlo=np.resize(hemlo,(len(hemlo)+1,2))
#hemlo[len(hemlo)-1][len(hemlo[0])-2]=1
#hemlo[len(hemlo)-1][len(hemlo[0])-1]=2
#print(hemlo)
#g=[1,1]
#blacklist=np.array([])
#print(blacklist)
#for i in range(3):
#                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
#                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]+i
#                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]
#                print(i,blacklist)
#print(blacklist)
#print(max(map(max, owo[0:2])))
#print(max(map(max, owo[3:5])))
#print(max(map(max, owo[6:9])))
#data="";
size=11
data=np.zeros((size,size))
##data=""
#print(data)
#def circle(data, center,  size):
#    radius=size/2+0.5
#    offset=(center[0]-radius,center[1]-radius)
#    for i in range(size):
#        for j in range(size):
#            x=i+offset[0]
#            y=j+offset[1]

#            print(x,y,radius)
#            if x ** 2 + y ** 2 <= radius** 2:
#                data=data+" x "
#                print("yo")
#            else:
#                data=data+"   "
#        data=data+"\n"

        
#    return data

#data=circle(data,(int(size/2)+1,int(size/2)+1),size)

#print(data)
width, height = size, size
coords=np.array([[]])
a, b = int(size/2),int(size/2)
r = int(size/2)
data[a][b]=1
for angle in range(0, 360, 5):
    x = r * math.sin(math.radians(angle)) + a
    y = r * math.cos(math.radians(angle)) + b
    
    data[int(round(y))][int(round(x))] = 1
 #nie dziala v
def fill_circle(grid,a,b,r):
    return 0;

fill_circle(data,a,b,r)
print(data)

#0
#G=np.array([[1,2],[1,5],[2,3],[2,8],[14,1]])
#print(G)
#i=0
#maxG=0
#while G[i][0]==1:
#    maxG=max(maxG, G[i][1])
#    i+=1
#print(maxG)
