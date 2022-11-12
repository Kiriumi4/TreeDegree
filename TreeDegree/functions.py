from re import X
from turtle import xcor
import numpy as np

temp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']

def selectQuad(pick, sizeX, sizeY):
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

def algorithm(tab,option):
        a=tab.shape # size of array
        G=np.array([[0,0]])
        b=0
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
                     #print("aaaa",i,j)
                     G=findPlaneOfType(tab,i,j,2) #szukanie trawy typ-2 
                     size=3
                     offset=([0,0]) #ustalone wedlug najblizszej krawedzi
                     x0,y0=findStart(G)
                     blacklist=checkAround(tab,G)
                     temp=0
                     while(temp<=len(G)):
                        if canTree(G,tab,size,(x0+offset[0],y0+offset[1])) and not checkFound((x0+offset[0],y0+offset[1]),blacklist) :
                             x,y=canTree(G,tab,size,(x0+offset[0],y0+offset[1]))
                             tab,G=putTree(tab,size,(x,y),G)  
                             offset[1]+=3
                        offset[1]+=1
                        offset[0]+=0
                        temp+=1

                 elif tab[i][j]==0:
                     b=1
              
                 #print(tab[i][j])
        return tab


   
    #wyszukanie ksztaltu (wszytkich dotykajacych sie punktow o danym typie np. trawa)
def findPlaneOfType(tab,i,j,typ):      
    grass=np.array([[i,j]])
    temp=i
    temp2=j
    #print(len(tab))
    #print(len(tab[0]))
    while(True):
        if temp+1<len(tab) and tab[temp+1][temp2]==typ and checkFound((temp+1,temp2),grass)==False:
            grass=np.resize(grass,(grass.shape[0]+1,2))
            grass[grass.shape[0]-1][0]=temp+1
            grass[grass.shape[0]-1][1]=temp2
            temp+=1
        elif temp2+1<len(tab[0]) and tab[temp][temp2+1]==typ and checkFound((temp,temp2+1),grass)==False:
            grass=np.resize(grass,(grass.shape[0]+1,2))
            grass[grass.shape[0]-1][0]=temp
            grass[grass.shape[0]-1][1]=temp2+1
            temp2+=1
        elif temp>1 and tab[temp-1][temp2]==typ and checkFound((temp-1,temp2),grass)==False:
            grass=np.resize(grass,(grass.shape[0]+1,2))
            grass[grass.shape[0]-1][0]=temp-1
            grass[grass.shape[0]-1][1]=temp2
            temp-=1
        elif temp2>1 and tab[temp][temp2-1]==typ and checkFound((temp,temp2-1),grass)==False:
            grass=np.resize(grass,(grass.shape[0]+1,2))
            grass[grass.shape[0]-1][0]=temp
            grass[grass.shape[0]-1][1]=temp2-1
            temp2-=1
        else:
            break
        
    return grass

def checkFound(coord,coordTab):

    for i in range (0,coordTab.shape[0]):
        if coord[0]==coordTab[i][0] and coord[1]==coordTab[i][1]:
            return True
    return False

#def checkFoundWhole(coordTab1,coordTab2):

#    for i in range (0,coordTab2.shape[0]):
#        for i in range (0,coordTab1.shape[0]):
#            if coordTab2[0]==coordTab1[i][0] and coordTab1[1]==coordTab2[i][1]:
#                return True
#    return False
#nu nu nu inaczej sprawdzamy szyskie coordynaty
def checkAround(tab,grass):
    blacklist=np.array([])

    for g in grass:
        if tab[g[0]-1][g[1]]==1: #road
            for i in range(3):
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]+i
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]
        if tab[g[0]][g[1]-1]==1: #road
            for i in range(3):
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]+i
        if tab[g[0]+1][g[1]]==1: #road
            for i in range(3):
                blacklist=np.resize(blacklist,(len(blacklist)+1,2))
                blacklist[len(blacklist)-1][len(blacklist[0])-2]=g[0]-i
                blacklist[len(blacklist)-1][len(blacklist[0])-1]=g[1]
        if tab[g[0]][g[1]+1]==1: #road
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

# funcja canTree
# sprawdzanie mozliwosci wlozenia drzewa w dane miejsce
# (area-tabela koordynatow mozliwego miejsca, size- wielkosc korony [m], offset - odleglosc wzgledem krawedzi (koordynaty))
#offset ustalany w samym algorytmie w zaleznosci od krawedzi sasiadujacych, braku mozliwosci postawienia drzewa badz liczby losowej ustalajacej ksztalt
#zalozmy areastart1/areastar2 jako pien drzewa //na pozniej - jeszcze nie zaimplementowane

def findStart(area):
    areaStart1=10000000
    areaStart2=10000000
    for i in range (0,area.shape[0]):
        areaStart1=min(areaStart1,area[i][0])

    for i in range (0,area.shape[0]):
        if area[i][0]==areaStart1:
           areaStart2 = min(areaStart2,area[i][1])

    return areaStart1,areaStart2



def canTree(area,tab,size,areaCoords): 
  
    placeable=0
    tempi=0

    print(area)
    areaStart1=areaCoords[0]
    areaStart2=areaCoords[1]

    print("a1,a2",areaStart1, areaStart2)
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

def putTree(tab,size,start,G):
    
    for i in range(0,size):
           for j in range(0,size):
                tab[start[0]+i][start[1]+j]=6
                for count,value in enumerate(G):

                        if value[0]==start[0]+i and value[1]==start[1]+j:
                             print(G[count])
                             G=np.delete(G, count,axis=0)
                            
 

    return tab,G


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

