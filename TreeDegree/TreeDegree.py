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

cmap = colors.ListedColormap(['0.5','0.1','lightgreen','0.8','brown','pink','green'])
bounds=[0,1,2,3,4,5,6,7]
norm = colors.BoundaryNorm(bounds, cmap.N)
c=(0,0)
rembTerr=0
colorButn=['grey35','grey25','lightgreen','grey70','brown','pink','green']
opened=0
while True:  # Event Loop
    event, values = wnd.window.read()
    print(event)
    print(values)
    butt=['Road','Grass','Walkway','Tram tracks','Sign']
    buttKey=['-EDITBTN1-','-EDITBTN2-','-EDITBTN3-','-EDITBTN4-','-EDITBTN5-']
    textboxKey=['-EDITTEXT1-','-EDITTEXT2-','-EDITTEXT3-','-EDITTEXT4-','-EDITTEXT5-']
    buttNum=1
    

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event=='New':

       wnd.window[f'-COL1-'].update(visible=True)
       wnd.window[f'-COL2-'].update(visible=False)
       wnd.window[f'-COL3-'].update(visible=False)
       wnd.window[f'-COL4-'].update(visible=False)
       wnd.window.refresh()

    if event == 'Ok':
       c=[int(i) for i in values['-OUTSIZE-'].split() if i.isdigit()]
       buildArr=np.zeros((c[0],c[1])) #Maciez trzymajaca informacje o aktualnie budowanym terenie
       f=open('variables.txt','w')
       f.write(str(c[0])+"\n"+str(c[0]))
       f.close()
       wnd.window[f'-COL1-'].update(visible=False)
       wnd.window[f'-COL2-'].update(visible=True)
       wnd.window[f'-INSIZE-'].update(values['-OUTSIZE-'])
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
            wnd.window[f'-COL1-'].update(visible=False)
            wnd.window[f'-COL2-'].update(visible=True)
            wnd.window[f'-INSIZE-'].update(values['-OUTSIZE-'])
            plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
            plt.savefig('square.png',transparent=True)
            wnd.window[f'-SQUARE-'].update('square.png')
            wnd.window.refresh()
  


    if event == 'Edit':
        if values['-OUTSIZE-']=='' and opened==0:
            sg.Popup('No new file. Click New to create file')
        else:
            wnd.window[f'-COL1-'].update(visible=False)
            wnd.window[f'-COL2-'].update(visible=False)
            wnd.window[f'-COL3-'].update(visible=True)
            wnd.window[f'-COL4-'].update(visible=False)
            
            plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
            plt.savefig('square.png',transparent=True)
            print(buildArr)
            for i in range(0,c[0]):
                for j in range(0,c[1]):
                    wnd.window[(i,j)].update(visible=True)
                    wnd.window[(i,j)].update(button_color=colorButn[int(buildArr[i][j])])
                    
            wnd.window.refresh()
        
    for count,value in enumerate(buttKey):
       
        if event==value:
            wnd.window[f'-EDITTEXT{count+1}-'].update(visible=True)
            for j in range(1,6):
                if j!=count+1:
                    wnd.window[f'-EDITTEXT{j}-'].update(visible=False)    
                wnd.window.refresh()
                rembTerr=count+1

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
                            buildArr[xl][yl]=count+1
                            wnd.window[(xl,yl)].update(button_color=colorButn[count+1])
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
                    buildArr[x][y]=count+1
                    wnd.window[(x,y)].update(button_color=colorButn[count+1])
            wnd.window[value].update('')

        plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
        plt.savefig('square.png',transparent=True)
        wnd.window.refresh()
        
    if event== 'Delete':
        for i in range(1,6):
            if values[f'-EDITTEXT{i}-']!='':
                if '-' in values[f'-EDITTEXT{i}-']:
                    temp=values[f'-EDITTEXT{i}-'].find('-')
                    left=values[f'-EDITTEXT{i}-'][:temp]
                    right=values[f'-EDITTEXT{i}-'][temp+1:]
                    #print(left)
                    #print(right)
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
        if values['-OUTSIZE-']=='' and opened==0:
            sg.Popup('No new file. Click New to create file')
        else: 
            wnd.window[f'-COL1-'].update(visible=False)
            wnd.window[f'-COL2-'].update(visible=False)
            wnd.window[f'-COL3-'].update(visible=False)
            wnd.window[f'-COL4-'].update(visible=True)
            plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
            plt.savefig('square.png',transparent=True)
            wnd.window[f'-BUILDSQUARE-'].update('square.png')
            wnd.window.refresh()

    if event=='Start building':
        func.algorithm(buildArr,0)
        plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
        plt.savefig('square.png',transparent=True)
        wnd.window[f'-BUILDSQUARE-'].update('square.png')
        wnd.window.refresh()
    if event=='Save':
      wnd.open_new_window('Save',buildArr);


     
wnd.window.close()




