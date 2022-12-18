from asyncio.windows_events import NULL
from ctypes.wintypes import SIZE
import numpy as np
import random
import math

def selectQuad(pick, sizeY, sizeX):
    temp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    x=0
    y=0
    numStr=""
    tempStr=""
    for x in pick:
        if x.isdigit():
            numStr=numStr+x
    #print("num:"+numStr)
    #print("cal:"+pick)
    lettStr=pick.replace(numStr,'')
    #print("repl:"+lettStr)
    i=0;
    j=0;
    count=0;
    while True:
        if lettStr==tempStr+temp[i]:
            break
        i=i+1
        if i>=26:
            i=0
            tempStr=temp[j]
            j=j+1
        count+=1;
        pass
    #print(count,int(numStr)-1)
    if count>sizeY-1 or int(numStr)>sizeX or count<0 or int(numStr)<0:
        return False
    else:
        
        return count,int(numStr)-1

def algorithm(tab,optionDens,optionVar):
        a=tab.shape # size of array
        G=np.array([[0,0]])
        TreePut=np.array([])
        print(tab) 
        print(tab[0][0])      
        
        
        Dens=[[0],[1,2],[3,4,5]]
        DensFlat=[0,1,2,3,4,5]
        Var=[[3,4,5],[6,7,8],[9,10]]
        VarFlat=[3,4,5,6,7,8,9,10]
        Sizes=[0,0,0,0,0,0,0,0]
        sIdx=0
        if optionVar==3:
             sizeRan=VarFlat
        else:
            sizeRan=Var[optionVar]
        if optionDens==3:
             sizeDens=DensFlat
        else:
            sizeDens=Dens[optionDens]
        
        for i in range(0,a[0]):
             for j in range(0,a[1]):
                 
   
                 if tab[i][j]==2 and not checkFound((i,j),G):
                     
                     G=findPlaneOfType(tab,i,j,2) #szukanie trawy typ-2 
                     #wybranie rozmiaru drzewa w obrebie jednej trawy 
                     size=sizeRan[random.randint(0,len(sizeRan)-1)]
                     gap=sizeDens[random.randint(0,len(sizeDens)-1)]
                     
                     offset=([0,0]) #ustalone wedlug najblizszej krawedzi
                     x0,y0=findStart(G,0)
                     #blacklist dla drogi typ 1 3 metry
                     blacklistRoad=checkAround(tab,G,3,1)
                     print("G",G)
                     print("blacklist",blacklistRoad)
                     #blacklist dla sieci gazowej typ 11 3 metry
                     blacklistGass=checkAround2(tab,G,3,11)
                     blacklistEnergy=checkAround2(tab,G,2,10)
                     blacklistTele=checkAround2(tab,G,2,9)
                     blacklistWater=checkAround2(tab,G,2,13)

                     blacklistOther=[]

                     for i in range(4):
                        if i==0:
                            blcktmp=blacklistGass
                        elif i==1:
                            blcktmp=blacklistEnergy
                        elif i==2:
                            blcktmp=blacklistTele
                        elif i==3:
                            blcktmp=blacklistWater
                       
                        if len(blcktmp)!=0:
                            
                            if len(blacklistOther)==0:
                                blacklistOther=blcktmp
                                
                            blacklistOther=np.concatenate((blacklistOther,blcktmp),axis=0)
                       
                     
                     
                     blacklistHeat=checkAround(tab,G,2,12)
                     temp=0
                     #print(temp2)
                     while(temp<len(G)):

                         #dodanie krzewow na podstawie black listy 
                        hedge(tab,blacklistRoad)
                        maxi=0
                        maxG=0
                        
                        
                        Tree=circle((x0+offset[0],y0+offset[1]),int(size/2))
                      
                        #sprawdzenie czy pien mozna postawic w miejscu na trawie
                        if  checkFound((x0+offset[0],y0+offset[1]),G):
                            #sprawdzenie czy pieñ nie stoi zbyt blisko drogi 
                            if not checkFound((x0+offset[0],y0+offset[1]),blacklistRoad):
                                #sprawdzenie czy pieñ nie stoi zbyt blisko innych sieci 
                                if not checkFound((x0+offset[0],y0+offset[1]),blacklistOther):
                                    #sprawdzenie czy korona nie narusza znakow, ulicy,lamp czy innych drzew
                                    if canWholeTreeCirk(tab,Tree) and not checkFoundCirk(Tree,TreePut): 
                                        #sprawdzenie czy korona znajduje sie 2 metry od sieci grzewczej
                                        if not checkFoundCirk(Tree,blacklistHeat):

                                                   
                                            tab,TreePut=putTreeCirk(tab,int(size/2),(x0+offset[0],y0+offset[1]),TreePut,gap) 
                                            if size not in Sizes:
                                                Sizes[sIdx]=size
                                                sIdx+=1

                                            if optionVar==3:
                                                size=sizeRan[random.randint(0,len(sizeRan)-1)]
                                
                                            if optionDens==3:
                                                gap=sizeDens[random.randint(0,len(sizeDens)-1)]                   

                        offset[1]+=1

                        while maxi<len(G):
   
                            if G[maxi][0]==x0+offset[0]:
                                maxG+=1
                            maxi+=1
                            
                        temp+=1
                        if  offset[1]>=maxG:
                            offset[0]+=1
                            offset[1]=0
                            _,y0=findStart(G,offset[0])
               
                
        return tab,Sizes


   
#wyszukanie ksztaltu (wszytkich dotykajacych sie punktow o danym typie np. trawa)
def findPlaneOfType(tab,i,j,typ):      
    grass=np.array([[i,j]])
    temp=i
    temp2=j
    bufferG=0
    while(True):
        bufferG=0
        for i in range(0,len(grass)):
            temp=grass[i][0]
            temp2=grass[i][1]
            if temp>1 and tab[temp-1][temp2]==typ and checkFound((temp-1,temp2),grass)==False:
                grass=np.resize(grass,(grass.shape[0]+1,2))
                grass[grass.shape[0]-1][0]=temp-1
                grass[grass.shape[0]-1][1]=temp2
                bufferG=1
                
            if temp2+1<len(tab[0]) and tab[temp][temp2+1]==typ and checkFound((temp,temp2+1),grass)==False:
                grass=np.resize(grass,(grass.shape[0]+1,2))
                grass[grass.shape[0]-1][0]=temp
                grass[grass.shape[0]-1][1]=temp2+1
                bufferG=1
                
            if temp+1<len(tab) and tab[temp+1][temp2]==typ and checkFound((temp+1,temp2),grass)==False:
                grass=np.resize(grass,(grass.shape[0]+1,2))
                grass[grass.shape[0]-1][0]=temp+1
                grass[grass.shape[0]-1][1]=temp2
                bufferG=1
                
            if temp2>1 and tab[temp][temp2-1]==typ and checkFound((temp,temp2-1),grass)==False:
                grass=np.resize(grass,(grass.shape[0]+1,2))
                grass[grass.shape[0]-1][0]=temp
                grass[grass.shape[0]-1][1]=temp2-1
                bufferG=1
        if bufferG==0:
            break
    grass=grass[grass[:,1].argsort()]
    grass=grass[grass[:,0].argsort()]   
    
    return grass

def checkFound(coord,coordTab):

    for i in range (0,len(coordTab)):
        
        if coord[0]==coordTab[i][0] and coord[1]==coordTab[i][1]:
            return True
    return False


def checkFoundCirk(circleTab,coordTab):
    temp=0
    for xc,yc in circleTab:
           for xt,yt in coordTab:
               if xc==xt and yc==yt:
                   return True

    return False
#Sprawdzenie wszystkich koordynatow na nesw dla pola droga i dodanie do listy zabronionych pozycji trawy na 3m od drogi
#make blacklist zmienic na rozpoznawanie od drogi

def checkAround2(tab,grass,meters,typ):
    blacklist=np.array([])

    for g in grass:
        
        if g[0]>0 and tab[g[0]-1][g[1]]==typ: 
            for i in range(meters):
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]+i
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]
        if g[1]>0 and tab[g[0]][g[1]-1]==typ: 
            for i in range(meters):
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]+i
        if g[0]+1<len(tab) and tab[g[0]+1][g[1]]==typ: 
            for i in range(meters):
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]-i
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]
        if g[1]+1<len(tab[0]) and tab[g[0]][g[1]+1]==typ: 
            for i in range(meters):
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]-i
    return blacklist

def checkAround(tab,grass,meters,typ):
    blacklist=np.array([])

    for g in grass:
        for i in range(meters+1):
            if g[0]-i>=0 and tab[g[0]-i][g[1]]==typ: 
               
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]
            if g[1]-i>=0 and tab[g[0]][g[1]-i]==typ: 
           
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]
            if g[0]+i<len(tab) and tab[g[0]+i][g[1]]==typ: 
            
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]
            if g[1]+i<len(tab[0]) and tab[g[0]][g[1]+i]==typ: 
            
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]
    return blacklist



def findStart(area,start):
    areaStart1=10000000
    areaStart2=10000000

    for i in range (0,area.shape[0]):
        areaStart1=min(areaStart1,area[i][0])

    for i in range (0,area.shape[0]):
        if area[i][0]==areaStart1+start:
           areaStart2 = min(areaStart2,area[i][1])

    return areaStart1,areaStart2


# funcja canTree
# sprawdzanie mozliwosci wlozenia drzewa w dane miejsce
# (area-tabela koordynatow mozliwego miejsca, size- wielkosc korony [m], offset - odleglosc wzgledem krawedzi (koordynaty))
#offset ustalany w samym algorytmie w zaleznosci od krawedzi sasiadujacych, braku mozliwosci postawienia drzewa badz liczby losowej ustalajacej ksztalt
#zalozmy areastart1/areastar2 jako pien drzewa //na pozniej - jeszcze nie zaimplementowane
# dla drzew niskich sprawdzanie czy cale drzewo zmiesci sie na trawie
#postarac sie zmienic na kolo i wg pnia 



def canWholeTreeCirk(tab,Circle): 
  
    
    tempi=0
    for i,j in Circle:
        i=int(i)
        j=int(j)
        if i<0 or j<0 or i>=len(tab) or j>=len(tab[0]):
            return False
        if tab[i][j]==1 :
            print(i,j," road")
            tempi=1
            return False
        if tab[i][j]==4:
            print(i,j," tram")
            tempi=1
            return False
        if tab[i][j]==5:
            print(i,j," sign")
            tempi=1
            return False
        if  tab[i][j]==6:
            print(i,j," other tree")
            tempi=1
            return False
        if  tab[i][j]==8:
            print(i,j," lamp")
            tempi=1
            return False
                
    if tempi==0:
       
        return True
    else:
        return False

def putTreeCirk(tab,size,start,TreePut,gap):

    Circle=circle(start,size)
    CircleGap=circle(start,size+gap)

    for i,j in Circle:

        tab[int(i)][int(j)]=6
        
    for i,j in CircleGap:

        TreePut=np.resize(TreePut,(len(TreePut)+1,2))
        TreePut[len(TreePut)-1][0]=int(i)
        TreePut[len(TreePut)-1][1]=int(j)

                          
    return tab,TreePut


def circle(center, radius):
    circlecoords=np.array([])
    a=center[1]
    b=center[0]
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

def hedge(tab, blacklist):
    
    for i in range(len(blacklist)):
        x=int(blacklist[i][0])
        y=int(blacklist[i][1])
        
        if tab[x][y]==2:
            if x>=1 and tab[x-1][y]==1:
                checkHowMuchGrass(tab,(x,y),'north')
            elif y>=1 and tab[x][y-1]==1:
                checkHowMuchGrass(tab,(x,y),'west')
            elif x<len(tab)-1 and tab[x+1][y]==1:
                checkHowMuchGrass(tab,(x,y),'south')
            elif y<len(tab[0])-1 and tab[x][y+1]==1:
                checkHowMuchGrass(tab,(x,y),'east')

    

def checkHowMuchGrass(tab,coords,orient):
    x=coords[0]
    y=coords[1]
    count=0
    a=0
    b=0
    walkway=[[]]

    for i in range (4):
       if orient=="north":
           a=i
       elif orient=="east":
           b=-i
       elif orient=="south":
           a=-i
       elif orient=="west":
           b=i

       if x+a>0 and x+a<len(tab) and y+b>0 and y+b<len(tab[0]):
            if  tab[x+a][y+b]==2:
                count+=1
            elif  tab[x+a][y+b]==3:
                walkway=[x+a,y+b]
                break
    
    if count==3 and walkway!=[[]]:
        if orient=="north" and not walkway[0]-2<0:
           tab[walkway[0]-2][walkway[1]]=7
        elif orient=="east" and not walkway[1]+2>=len(tab[1]):
           tab[walkway[0]][walkway[1]+2]=7
        elif orient=="south" and not walkway[0]+2>=len(tab[0]):
           tab[walkway[0]+2][walkway[1]]=7  
        elif orient=="south" and not walkway[0]-2<0:
           tab[walkway[0]][walkway[1]-2]=7
    elif count==2 and walkway!=[[]]:
        if orient=="north" and not walkway[0]-1<0:
           tab[walkway[0]-1][walkway[1]]=7
        elif orient=="east" and not walkway[1]+1>=len(tab[1]):
           tab[walkway[0]][walkway[1]+1]=7
        elif orient=="south" and not walkway[0]+1>=len(tab[0]):
           tab[walkway[0]+1][walkway[1]]=7
        elif orient=="south" and not walkway[1]-1<0:
           tab[walkway[0]][walkway[1]-1]=7
        
        
    return count

