from asyncio.windows_events import NULL
import numpy as np
import random



def selectQuad(pick, sizeX, sizeY):
    temp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']
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
        if i>=25:
            i=0
            tempStr=temp[j]
            j=j+1
        count+=1;
        pass
    #print(count,int(numStr)-1)
    if count>sizeX-1 or int(numStr)>sizeY or count<0 or int(numStr)<0:
        return False
    else:
        
        return count,int(numStr)-1

def algorithm(tab,optionDens,optionVar):
        a=tab.shape # size of array
        G=np.array([[0,0]])
        TreePut=np.array([])
        b=0
        Dens=[[0],[1,2,3],[4,5,6]]
        Var=[[3,5,7],[9,11,13],[15,17,19]]


        sizeRan=Var[optionVar]
        
        for i in range(0,a[0]):
             for j in range(0,a[1]):
                 if tab[i][j]==1:
                     #print("road")
                     b=1
                 elif tab[i][j]==4:
                     #print("tram")
                     b=1
                 elif tab[i][j]==3:
                     #print("walk")
                     b=1    
                 elif tab[i][j]==2 and not checkFound((i,j),G):
                     
                     G=findPlaneOfType(tab,i,j,2) #szukanie trawy typ-2 
                     #wybranie rozmiaru drzewa w obrebie jednej trawy 
                     print(sizeRan)
                     size=sizeRan[random.randint(0,2)]
                     
                     offset=([0,0]) #ustalone wedlug najblizszej krawedzi
                     x0,y0=findStart(G,0)
                     blacklist=checkAround(tab,G)
                     temp=0
                     #print(temp2)
                     while(temp<len(G)):


                        hedge(tab,blacklist)
                        maxi=0
                        maxG=0
                        tempG=0
                        
                        print(x0+offset[0],y0+offset[1])

                        if canWholeTree(G,tab,size,(x0+offset[0],y0+offset[1])) and not checkFound2((x0+offset[0],y0+offset[1]),size,blacklist):
                            if checkFound2((x0+offset[0],y0+offset[1]),size,TreePut) ==False:
                                    x,y=canWholeTree(G,tab,size,(x0+offset[0],y0+offset[1]))
                                    tab,G,TreePut=putTree(tab,size,(x,y),G,TreePut) 
                                    offset[1]=offset[1]+size

                        offset[1]+=1

                        while maxi<len(G):
   
                            if G[maxi][0]==x0+offset[0]:
                                maxG+=1
                            maxi+=1
                            
                        
                        
                        temp+=1
                        if  offset[1]>=maxG:
                            offset[0]+=1
                            offset[1]=0
                            xnon,y0=findStart(G,offset[0])
                      
                 elif tab[i][j]==0:
                     b=1    
                 #print(tab[i][j])
        return tab


   
#wyszukanie ksztaltu (wszytkich dotykajacych sie punktow o danym typie np. trawa)
def findPlaneOfType(tab,i,j,typ):      
    grass=np.array([[i,j]])
    temp=i
    temp2=j
    bufferG=0
    #print(len(tab))
    #print(len(tab[0]))
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

    for i in range (0,coordTab.shape[0]):
        if coord[0]==coordTab[i][0] and coord[1]==coordTab[i][1]:
            return True
    return False

def checkFound2(coord,size,coordTab):

    for i in range(0,size):
           for j in range(0,size):
                for x in range (0,coordTab.shape[0]):
                    if coord[0]+i==coordTab[x][0] and coord[1]+j==coordTab[x][1]:
                       
                        return True
 
    return False

#Sprawdzenie wszystkich koordynatow na nesw dla pola droga i dodanie do listy zabronionych pozycji trawy na 3m od drogi
#make blacklist zmienic na rozpoznawanie od drogi
def checkAround(tab,grass):
    blacklist=np.array([])

    for g in grass:
        if g[0]-1>0 and tab[g[0]-1][g[1]]==1: #road
            for i in range(3):
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]+i
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]
        if g[1]-1>0 and tab[g[0]][g[1]-1]==1: #road
            for i in range(3):
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]+i
        if g[0]+1<len(tab) and tab[g[0]+1][g[1]]==1: #road
            for i in range(3):
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]-i
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]
        if g[1]+1<len(tab[0]) and tab[g[0]][g[1]+1]==1: #road
            for i in range(3):
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]-i
    return blacklist


#okreslamy odleglosc od znaku drogowego (zalozymy ze drzewo nie moze stac 1 m kolo znaku znakiem)
#zmienic warunek przy krawedzi (dla trawy o <3 m kolo krawedzi program sie wywala)
def isSign(treeCoord, tab, size):
    for i in range(1,size+3):
        if treeCoord[1]+i<len(tab[0]) and tab[treeCoord[0]][treeCoord[1]+i]==5:
        
            return False
    if (treeCoord[0]+1<len(tab) and tab[treeCoord[0]+1][treeCoord[1]]==5) or (treeCoord[0]-1<0 and tab[treeCoord[0]-1][treeCoord[1]]==5 ) or (treeCoord[1]-1<0 and tab[treeCoord[0]][treeCoord[1]-1]==5):
        return False
    else:
        return True


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
def canWholeTree(area,tab,size,areaCoords): 
  
    placeable=0
    tempi=0

    #print(area)
    areaStart1=areaCoords[0]
    areaStart2=areaCoords[1]

    #print("a1,a2",areaStart1, areaStart2)
    for i in range(0,size*size):
        for j in area:
            if j[0]==areaStart1+tempi and j[1]==areaStart2+i%size:    
                placeable+=1
                
                
        if i%size==0 and i>=size:
            tempi+=1
       
    if placeable==size*size and isSign((areaStart1, areaStart2),tab,size):
        print("Can put Tree")
        return areaStart1,areaStart2
    else:
        return False

#znalezienie koordynatow dla wyrysowania drzewa (zmienic na kolo i wg pnia a nie lisci)

def putTree(tab,size,start,G,TreePut):
    
    for i in range(0,size):
           for j in range(0,size):
                tab[start[0]+i][start[1]+j]=6
                TreePut=np.resize(TreePut,(len(TreePut)+1,2))
                TreePut[len(TreePut)-1][0]=start[0]+i
                TreePut[len(TreePut)-1][1]=start[1]+j

                            
    return tab,G,TreePut

def circle(data, center, radius, size):
    for i in range(size):
        for j in range(size):
            if (i - center[0]) ** 2 + (j - center[1]) ** 2 <= radius ** 2:
                data[i * size + j] = 6
    return data

def hedge(tab, blacklist):
    
    for i in range(len(blacklist)):
        x=int(blacklist[i][0])
        
        y=int(blacklist[i][1])
        print(x,y)
        if tab[x][y]==2:
            if tab[x-1][y]==1:
                checkHowMuchGrass(tab,(x,y),'north')
            elif tab[x][y-1]==1:
                checkHowMuchGrass(tab,(x,y),'west')
            elif tab[x+1][y]==1:
                checkHowMuchGrass(tab,(x,y),'south')
            elif tab[x][y+1]==1:
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

       if tab[x+a][y+b]==2:
            count+=1
       elif tab[x+a][y+b]==3:
           walkway=[x+a,y+b]
           break
    print(walkway)
    if count==3 and walkway!=[[]]:
        if orient=="north":
           tab[walkway[0]-2][walkway[1]]=7
        elif orient=="east":
           tab[walkway[0]][walkway[1]+2]=7
        elif orient=="south":
           tab[walkway[0]+2][walkway[1]]=7
        elif orient=="south":
           tab[walkway[0]][walkway[1]-2]=7
    if (count==2 or count==1 ) and walkway!=[[]]:
           tab[x][y]=7
        
        
    return count


#tab1=np.array([[0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,2,2,2,2,2,0,0,0,0,0],[0,2,2,2,2,2,0,0,0,0,0],[0,2,2,2,2,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]])
##tab1=np.resize(tab1,(4,2))
#print(tab1)  #tab[wiersz][kolumna]
#print(doGrass(tab1,2,1))
#a=doGrass(tab1,2,1)
#print(canTree(a,3,(0,1)))
#print(algorithm(tab1,0))
#coordTab=np.array([[2,3]])
#print(checkFound((2,3),coordTab))
#print(algorithm(tab))
#algorithm(tab)

