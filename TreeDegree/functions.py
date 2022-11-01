from tempfile import tempdir
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

def algorithm(tab):
        a=tab.shape # size of array
        grass=np.array([0,0])
        road=np.array([0,0])
        tram=np.array([0,0])
        walk=np.array([0,0])
        for i in range(0,a[0]):
             for j in range(0,a[1]):
                 if tab[i][j]==1:
                     print("road")
                 elif tab[i][j]==4:
                     print("tram")
                 elif tab[i][j]==3:
                     print("walk")
                 elif tab[i][j]==2:
                     print("grass")
                 elif tab[i][j]==0:
                     print("0")
              
                 #print(tab[i][j])
        return 0


    # ZMIENIC DLA KRAWEDZI DANYCH DZIALA DLA POLA W SRODKU
def doGrass(tab,i,j):      
    grass=np.array([[i,j]])
    temp=i
    temp2=j
    while(True):
        if tab[temp+1][temp2]==2 and checkFound((temp+1,temp2),grass)==False:
            grass=np.resize(grass,(grass.shape[0]+1,2))
            grass[grass.shape[0]-1][0]=temp+1
            grass[grass.shape[0]-1][1]=temp2
            temp+=1
        elif tab[temp][temp2+1]==2 and checkFound((temp,temp2+1),grass)==False:
            grass=np.resize(grass,(grass.shape[0]+1,2))
            grass[grass.shape[0]-1][0]=temp
            grass[grass.shape[0]-1][1]=temp2+1
            temp2+=1
        elif tab[temp-1][temp2]==2 and checkFound((temp-1,temp2),grass)==False:
            grass=np.resize(grass,(grass.shape[0]+1,2))
            grass[grass.shape[0]-1][0]=temp-1
            grass[grass.shape[0]-1][1]=temp2
            temp-=1
        elif tab[temp][temp2-1]==2 and checkFound((temp,temp2-1),grass)==False:
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

# funcja canTree
# sprawdzanie mo¿liwoœci w³o¿enia drzewa w dane miejsce
# (area-tabela koordynatów mo¿liwego miejsca, size- wielkosc korony [m], offset - odleg³osc wzglêdem krawêdzi (koordynaty))
#offset ustalany w samym algorytmie w zale¿nosci od krawedzi s¹siaduj¹cych, braku mozliwosci postawienia drzewa badz liczby losowej ustalajacej ksztalt

def canTree(area,size,offset): 
    x=offset[0]
    y=offset[1]
    areaStart1=10000000
    areaStart2=10000000
    placeable=0
    tempi=0
    for i in range (0,area.shape[0]):
        if area[i][0]< areaStart1 and area[i][1]< areaStart2:
            areaStart1=area[i][0]
            areaStart2=area[i][1]

    print(areaStart1, areaStart2)
    for i in range(0,size*size):
        for j in area:
            if j[0]==areaStart1+x+tempi and j[1]==areaStart2+y+i%size:    
                #print(areaStart1+x+i%size,",", areaStart2+y+tempi)
                placeable+=1
                
        if i%size==0 and i>=size:
            tempi+=1


            
    if placeable==size*size:
        print("The tree is put")
        return True
    else:
        return False

tab1=np.array([[0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,2,2,2,2,2,0,0,0,0,0],[0,2,2,2,2,2,0,0,0,0,0],[0,2,2,2,2,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]])
#tab1=np.resize(tab1,(4,2))
print(tab1)  #tab[wiersz][kolumna]
print(doGrass(tab1,2,1))
a=doGrass(tab1,2,1)
print(canTree(a,3,(0,1)))
#coordTab=np.array([[2,3]])
#print(checkFound((2,3),coordTab))
#print(algorithm(tab))
#algorithm(tab)

