from distutils.command.check import check
from lib2to3.pgen2.token import CIRCUMFLEX
import math
import numpy as np
import random 
from matplotlib import pyplot as plt
from matplotlib import colors
from PIL import Image



####### Modul zawiera testy innych funkcji nie jest uzywany w programie wlasciwym!!!



#owo= np.array([[3,2],[1,3],[2,2],[2,3],[2,4],[3,8],[3,3],[3,4],[3,5]])
##owo1= [[3,2],[1,3],[2,2],[2,3],[2,4],[3,8],[3,3],[3,4],[3,5]]





#grass= np.array([[4,5],[5,5],[5,9],[3,6],[5,6],[5,7],[4,6],[5,8],[3,7],[4,7],[3,8],[3,9],[4,8],[4,9]])
#print(np.concatenate((grass,owo), axis=0))
##print(grass)
##grass=grass[grass[:,1].argsort()]
##grass=grass[grass[:,0].argsort()]   
##print(grass)
##size=9
#data=np.zeros((20 ,20))

folder2=['Wierzba','Wisnia','KlonPospolity','KlonFrancuski','KlonPolny','Jarzab','Deren','Glog','Bukszpan','Kalina']
#text1=['Wierzba ostrolistna','Wisnia osobliwa Umbraculifera','Klon Pospolity','Klon Francuski','Klon Polny','Jarzab pospolity','Deren wlasciwy','Glog jednoszyjkowy','Bukszpan Zwyczajny','Kalina hordowina']
#text2=['Wymiary: max 5m wysokosci, ok. 3m szerokosci. Strefa mrozoodpornosci: 4a. Rodzaj gleby: niewielkie wymagania. Okres sadzenia: III-IV','Wymiary: max 10m wysokosci, ok. 3-5m szerokosci. Strefa mrozoodpornosci: 5b. Rodzaj gleby: niewielkie wymagania.Wymaga podwiazywania pnia. Okres sadzenia: III-XI',
#       'Wymiary: max 5m wysokosci, ok. 4-5m szerokosci. Strefa mrozoodpornosci: 4a. Rodzaj gleby: wrazliwy na zasolenie. Okres sadzenia: X-XI',
#       'Wymiary: max 10m wysokosci, ok. 4-6m szerokosci. Strefa mrozoodpornosci: 6a. Rodzaj gleby: niewielkie wymagania. Okres sadzenia: III-IV,XI',
#       'Wymiary: max 4m wysokosci, ok. 5m szerokosci. Strefa mrozoodpornosci: 4a. Rodzaj gleby: wrazliwosc na zanieczyszczenia zwiazkami fluoru. Okres sadzenia: III-IV,X-XI',
#       'Wymiary: max 15m wysokosci, ok. 5-10m szerokosci. Strefa mrozoodpornosci: 3. Rodzaj gleby: brak wymagan. Okres sadzenia: II-III','Wymiary: max 10m wysokosci, ok. 5-10m szerokosci. Strefa mrozoodpornosci: 5b. Rodzaj gleby: niewielkie wymagania. Okres sadzenia: IV-VI,X-XI',
#       'Wymiary: max 10m wysokosci, ok. 8m szerokosci. Strefa mrozoodpornosci: 4a. Rodzaj gleby: unikac piaszczystych lub podmoklych. Okres sadzenia: X-XI',
#       'Wymiary: max 4m wysokosci, ok. 1m szerokosci. Strefa mrozoodpornosci: 6a. Rodzaj gleby: unikac piaszczystych. Okres sadzenia: XIII-IX',
#       'Wymiary: max 3m wysokosci, ok. 5m szerokosci. Strefa mrozoodpornosci: 4a. Rodzaj gleby: niewielkie wymagania. Okres sadzenia: IV-VI,X-XI']
for i,value in enumerate(folder2):
    print(value)
    direc=r'Trees\\'+value+r'\\im.png'
    image = Image.open(direc)
    new_image = image.resize((150, 150))
    new_image.save(direc)

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
##print(data)



#def checkFound(coord,coordTab):

#    for i in range (0,len(coordTab)):
#        if coord[0]==coordTab[i][0] and coord[1]==coordTab[i][1]:
#            return True
#    return False

#def circle( center, radius):
#    circlecoords=np.array([])
#    a=center[0]
#    b=center[1]
#    for angle in range(0, 360, 5):
#        x = radius * math.sin(math.radians(angle)) + a
#        y = radius * math.cos(math.radians(angle)) + b
#        xr=int(round(x))
#        yr=int(round(y))
        
        
            
#        if xr<a:
#                for j in range(xr,a):
#                    if not checkFound((yr,j),circlecoords):
#                        circlecoords=np.resize(circlecoords,(len(circlecoords)+1,2))
#                        circlecoords[len(circlecoords)-1][len(circlecoords[0])-2]=yr
#                        circlecoords[len(circlecoords)-1][len(circlecoords[0])-1]=j
#        elif xr>a :
            
#                for j in range(a,xr+1):
#                    if not checkFound((yr,j),circlecoords):
#                        circlecoords=np.resize(circlecoords,(len(circlecoords)+1,2))
#                        circlecoords[len(circlecoords)-1][len(circlecoords[0])-2]=yr
#                        circlecoords[len(circlecoords)-1][len(circlecoords[0])-1]=j
      
    
#    return circlecoords
#size=10
#a=circle((10,10),int(size/2))
#print(a)
#for i,j in a:
#    #print(i,j)
#    data[int(i)][int(j)]=1

#print(data)

