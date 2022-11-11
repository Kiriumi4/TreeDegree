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

owo= np.array([[1,2],[1,3],[2,2],[2,3],[2,4],[3,2],[3,3],[3,4],[3,5]])
#owo=['-EDITBTN1-','-EDITBTN2-','-EDITBTN3-','-EDITBTN4-','-EDITBTN5-']
#print(owo)
#for opt in enumerate(owo):
#    print(opt[0])
print(owo)

for i,value in enumerate(owo):
    #print(i)
  
    if value[0]==1 and value[1]==3:
         #print('a')
         owo=np.delete(owo, i,axis=0)

print(owo)


#print(max(map(max, owo[0:2])))
#print(max(map(max, owo[3:5])))
#print(max(map(max, owo[6:9])))