from asyncio.windows_events import NULL
from optparse import Values
import PySimpleGUI as sg
import window as wnd
import functions as func
from window import num_buttons_i
from window import num_buttons_j
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
#                                      0,                   road            , grass     ,      walkway,           tram  ,            sign ,        tree ,                  hedge   ,      lamp             ,Telecom  Net,           Elec,      pipe  ,       heating  ,        water
cmap = colors.ListedColormap([(0.35, 0.35, 0.35,1),(0.23, 0.23, 0.23,1),(0.79, 1, 0.44,1),(0.7, 0.7, 0.7,1),(0.63, 0.32, 0.18,1),(1, 0.27, 0,1),(0.42, 0.56, 0.14,1),(0.60, 0.80, 0.2,1),(1, 0.93, 0.55,1),(0.94, 0.5, 0.5,1),(1, 0.84, 0,1),(1, 1, 1,1),(1, 0.39, 0.28,1),(0, 0.96, 1,1)])
bounds=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
norm = colors.BoundaryNorm(bounds, cmap.N)
c=(0,0)
rembTerr=0
#             0,     1. road   ,2. grass     ,3. walkway, 4.tram  ,    5.  sign ,      6.  tree ,  7.  hedge   ,   8.   lamp       ,9.Telecom  Net,  10.Elec,    11.pipe  ,12.heating  ,13. water
colorButn=['grey35','grey23','DarkOliveGreen1','grey70','sienna','OrangeRed','OliveDrab', 'OliveDrab3','LightGoldenrod1','LightCoral','gold','thistle1','tomato','turquoise1']
butt=['Road','Grass','Walkway','Tram tracks','Sign','Lamp post','Telecommunications network','Electrical grid','Pipeline transport','District heating','Water supply network']
buttKey=['-EDITBTN1-','-EDITBTN2-','-EDITBTN3-','-EDITBTN4-','-EDITBTN5-','-EDITBTN6-','-EDITBTN7-','-EDITBTN8-','-EDITBTN9-','-EDITBTN10-','-EDITBTN11-']
textboxKey=['-EDITTEXT1-','-EDITTEXT2-','-EDITTEXT3-','-EDITTEXT4-','-EDITTEXT5-','-EDITTEXT6-','-EDITTEXT7-','-EDITTEXT8-','-EDITTEXT9-','-EDITTEXT10-','-EDITTEXT11-']
pickedTree=[]
opened=0
buildArr=0
while True:  # Event Loop
    event, values = wnd.window.read()
    print(event)
    print(values)
   
    buttNum=1
    

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event=='New':
     
       buildArr,c=wnd.open_new_window('New',[])
       if type(buildArr)==type(np.array([])):
            wnd.window[f'-OBR-'].update(visible=False) 
            
            wnd.window[f'-COL2-'].update(visible=True)
            
            plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
            plt.savefig('square.png',transparent=True)
            wnd.window[f'-SQUARE-'].update('square.png')
            wnd.window.refresh()


    
    if event=='Open':

        buildArr=wnd.open_new_window('Open',0);
        
        if type(buildArr)!=type(np.array([])):
             sg.Popup('No file selected')
        else:
            c=len(buildArr),len(buildArr[0])
            opened=1
            wnd.window[f'-OBR-'].update(visible=False)
            
            wnd.window[f'-COL2-'].update(visible=True)
            wnd.window[f'-INSIZE-'].update(values['-OUTSIZE-'])
            plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
            plt.savefig('square.png',transparent=True)
            wnd.window[f'-SQUARE-'].update('square.png')
            wnd.window.refresh()
  


    if event == 'Edit':
        if type(buildArr)!=type(np.array([])) and opened==0:
            sg.Popup('No file. Click New/Open to create/open file')
        else:
            
            wnd.window[f'-COL2-'].update(visible=False)
            wnd.window[f'-COL3-'].update(visible=True)
            wnd.window[f'-COL4-'].update(visible=False)
            
            print(buildArr)
            for i in range(0,c[0]):
                for j in range(0,c[1]):
                    wnd.window[(i,j)].update(visible=True)
                    wnd.window[(i,j)].update(button_color=colorButn[int(buildArr[i][j])])
                    
            wnd.window.refresh()
        
    for count,value in enumerate(buttKey):
       
        if event==value:
            wnd.window[f'-EDITTEXT{count+1}-'].update(visible=True)
            for j in range(1,12):
                if j!=count+1:
                    wnd.window[f'-EDITTEXT{j}-'].update(visible=False)    
                wnd.window.refresh()
                if count+1<6:
                     rembTerr=count+1
                else:
                    rembTerr=count+1+2
                
    if type(buildArr)==type(np.array([])):
        for i in range(0,c[0]):
            for j in range(0,c[1]):
                if event==(i,j):
                    #wnd.window[(i,j)].update(text=' '+str(rembTerr)+' ')
                    wnd.window[(i,j)].update(button_color=colorButn[rembTerr])
                    buildArr[i][j]=rembTerr
            

    if event== 'Add':
        for count,value in enumerate(textboxKey):
            if values[value]!='':
                if '-' in values[value]:
                    temp=values[value].find('-')
                    left=values[value][:temp]
                    right=values[value][temp+1:]
                    print(left)
                    print(right)
                    if func.selectQuad(left,c[0],c[1])==False or func.selectQuad(right,c[0],c[1])==False:
                        sg.Popup("Picked quadrant out of range")
                    else:
                        xl,yl=func.selectQuad(left,c[0],c[1])
                        yp=yl
                        xr,yr=func.selectQuad(right,c[0],c[1])
                        while True:

                            if count+1<6:
                                buildArr[xl][yl]=count+1
                                wnd.window[(xl,yl)].update(button_color=colorButn[count+1])
                            else:
                                buildArr[xl][yl]=count+1+2 
                                wnd.window[(xl,yl)].update(button_color=colorButn[count+1+2])

                           
                            if xl==xr and yl==yr:
                                break
                            elif yl==yr:
                                yl=yp
                                xl+=1
                            else:
                                yl+=1 
                elif func.selectQuad(values[value],c[0],c[1])==False:
                    sg.Popup("Picked quadrant out of range")
                else:
                    
                    x,y=func.selectQuad(values[value],c[0],c[1])

                    if count+1<6:
                        buildArr[xl][yl]=count+1
                        wnd.window[(x,y)].update(button_color=colorButn[count+1])
                    else:
                        buildArr[xl][yl]=count+1+2
                        wnd.window[(x,y)].update(button_color=colorButn[count+1+2])
                   
                    
            wnd.window[value].update('')

        print(plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm))
        plt.savefig('square.png',transparent=True)
        wnd.window.refresh()
        
    if event== 'Delete':
        for i in range(1,6):
            if values[f'-EDITTEXT{i}-']!='':
                if '-' in values[f'-EDITTEXT{i}-']:
                    temp=values[f'-EDITTEXT{i}-'].find('-')
                    left=values[f'-EDITTEXT{i}-'][:temp]
                    right=values[f'-EDITTEXT{i}-'][temp+1:]
                 
                    if func.selectQuad(left,c[0],c[1])==False or func.selectQuad(right,c[0],c[1])==False:
                        sg.Popup("Picked quadrant out of range")
                    else:
                        xl,yl=func.selectQuad(left,c[0],c[1])
                        yp=yl
                        xr,yr=func.selectQuad(right,c[0],c[1])
                        while True:
                            buildArr[xl][yl]=0
                            if xl==xr and yl==yr:
                                break
                            elif yl==yr:
                                yl=yp
                                xl+=1
                            else:
                                yl+=1          
                elif func.selectQuad(values[f'-EDITTEXT{i}-'],c[0],c[1])==False:
                    sg.Popup("Picked quadrant out of range")
                else:
                    x,y=func.selectQuad(values[f'-EDITTEXT{i}-'],c[0],c[1])
                    buildArr[x][y]=0
            wnd.window[f'-EDITTEXT{i}-'].update('')
        plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
        plt.savefig('square.png',transparent=True)

        wnd.window.refresh()
        rembTerr=0

    if event=='Compute':
        if type(buildArr)!=type(np.array([])) and opened==0:
            sg.Popup('No new file. Click New to create file')
        else: 
           
            wnd.window[f'-COL2-'].update(visible=False)
            wnd.window[f'-COL3-'].update(visible=False)
            wnd.window[f'-COL4-'].update(visible=True)
            plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
            plt.savefig('square.png',transparent=True)
            wnd.window[f'-BUILDSQUARE-'].update('square.png')
            wnd.window.refresh()

    if event=='Start building':
        if values['-OPTIONSDENSE-']==[] or values['-OPTIONSVARIETY-']==[]:
            sg.Popup('Pick options for tree density and variety')
        else:
            option1=0
            option2=0
            for count,val in enumerate(wnd.choices):
                
                if val in values['-OPTIONSDENSE-']:
                    option1=count
            for count,val in enumerate(wnd.choices2):
                if val in values['-OPTIONSVARIETY-']:
                    option2=count


            print(option1,option2)
            buildArr,pickedTree=func.algorithm(buildArr,option1,option2)
            plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
            plt.savefig('square.png',transparent=True)
            wnd.window[f'-BUILDSQUARE-'].update('square.png')
            wnd.window[f'-TREELIST-'].update(visible=True)
            print(pickedTree)
            for i in range(2,12):
                if i not in pickedTree:
                    wnd.window[f'-{i}t-'].update('')
                    wnd.window[f'-{i}-'].update(visible=False)
            wnd.window.refresh()
    if event=='Save':
      wnd.open_new_window('Save',buildArr);


     
wnd.window.close()




