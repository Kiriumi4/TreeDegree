from optparse import Values
import PySimpleGUI as sg
import window as wnd
import functions as func
from window import num_buttons_i
from window import num_buttons_j
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors

cmap = colors.ListedColormap(['0.5','0.1','lightgreen','0.8','brown','green'])
bounds=[0,1,2,3,4,5,6]
norm = colors.BoundaryNorm(bounds, cmap.N)
c=(0,0)
rembTerr=0
colorButn=['grey35','grey25','lightgreen','grey70','brown','green']

while True:  # Event Loop
    event, values = wnd.window.read()
    print(event)
    print(values)
    butt=['Road','Grass','Walkway','Tram tracks']
    buttKey=['-EDITBTN1-','-EDITBTN2-','-EDITBTN3-','-EDITBTN4-']
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
       buildArr=np.zeros((c[0],c[1])) #Array to hold all building data
       f=open('variables.txt','w')
       f.write(str(c[0])+"\n"+str(c[0]))
       f.close()
       wnd.window[f'-COL1-'].update(visible=False)
       wnd.window[f'-COL2-'].update(visible=True)
       wnd.window[f'-INSIZE-'].update(values['-OUTSIZE-'])
       plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
       plt.savefig('square.png',transparent=True)
       wnd.window[f'-SQUARE-'].update('square.png')
       for i in range(0,c[0]):
           for j in range(0,c[1]):
               if event==(i,j):
                    wnd.window[(i,j)].update(text='  ')
       wnd.window.refresh()
       
    if event == 'Edit':
       wnd.window[f'-COL1-'].update(visible=False)
       wnd.window[f'-COL2-'].update(visible=False)
       wnd.window[f'-COL3-'].update(visible=True)
       wnd.window[f'-COL4-'].update(visible=False)
       plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
       plt.savefig('square.png',transparent=True)

       for i in range(0,c[0]):
            for j in range(0,c[1]):
                wnd.window[(i,j)].update(visible=True)
       wnd.window.refresh()

    for i in buttKey:
        if event==i:
              wnd.window[f'-EDITBUTTS{buttNum}-'].update(visible=True)
              for j in range(1,5):
                  if j!=buttNum:
                      wnd.window[f'-EDITBUTTS{j}-'].update(visible=False)    
              wnd.window.refresh()
              rembTerr=buttNum

        buttNum+=1

    for i in range(0,c[0]):
            for j in range(0,c[1]):
                if event==(i,j):
                    #wnd.window[(i,j)].update(text=' '+str(rembTerr)+' ')
                    wnd.window[(i,j)].update(button_color=colorButn[rembTerr])
                    buildArr[i][j]=rembTerr

    if event== 'Add':
        for i in range(1,5):
            if values[f'-EDITBUTTS{i}-']!='':
                if '-' in values[f'-EDITBUTTS{i}-']:
                    temp=values[f'-EDITBUTTS{i}-'].find('-')
                    left=values[f'-EDITBUTTS{i}-'][:temp]
                    right=values[f'-EDITBUTTS{i}-'][temp+1:]
                    print(left)
                    print(right)
                    if func.selectQuad(left,c[0],c[1])==False or func.selectQuad(right,c[0],c[1])==False:
                        sg.Popup("Picked quadrant out of range")
                    else:
                        xl,yl=func.selectQuad(left,c[0],c[1])
                        xr,yr=func.selectQuad(right,c[0],c[1])
                        while True:
                            buildArr[xl][yl]=i
                            if xl==xr and yl==yr:
                                break
                            elif yl==c[1]-1:
                                yl=0
                                xl+=1
                            else:
                                yl+=1 
                elif func.selectQuad(values[f'-EDITBUTTS{i}-'],c[0],c[1])==False:
                    sg.Popup("Picked quadrant out of range")
                else:
                    print(values[f'-EDITBUTTS{i}-'])
                    x,y=func.selectQuad(values[f'-EDITBUTTS{i}-'],c[0],c[1])
                    buildArr[x][y]=i
            wnd.window[f'-EDITBUTTS{i}-'].update('')

        plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
        plt.savefig('square.png',transparent=True)
        #wnd.window[f'-EDITSQUARE-'].update('square.png')
        #wnd.window[f'-EDITSQUARE-'].update(str(buildArr))
        wnd.window.refresh()
        
    if event== 'Delete':
        for i in range(1,5):
            if values[f'-EDITBUTTS{i}-']!='':
                if '-' in values[f'-EDITBUTTS{i}-']:
                    temp=values[f'-EDITBUTTS{i}-'].find('-')
                    left=values[f'-EDITBUTTS{i}-'][:temp]
                    right=values[f'-EDITBUTTS{i}-'][temp+1:]
                    print(left)
                    print(right)
                    if func.selectQuad(left,c[0],c[1])==False or func.selectQuad(right,c[0],c[1])==False:
                        sg.Popup("Picked quadrant out of range")
                    else:
                        xl,yl=func.selectQuad(left,c[0],c[1])
                        xr,yr=func.selectQuad(right,c[0],c[1])
                        while True:
                            buildArr[xl][yl]=0
                            if xl==xr and yl==yr:
                                break
                            elif yl==c[0]-1:
                                yl=0
                                xl+=1
                            else:
                                yl+=1          
                elif func.selectQuad(values[f'-EDITBUTTS{i}-'],c[0],c[1])==False:
                    sg.Popup("Picked quadrant out of range")
                else:
                    print(values[f'-EDITBUTTS{i}-'])
                    x,y=func.selectQuad(values[f'-EDITBUTTS{i}-'],c[0],c[1])
                    buildArr[x][y]=0
            wnd.window[f'-EDITBUTTS{i}-'].update('')
        plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
        plt.savefig('square.png',transparent=True)
        #wnd.window[f'-EDITSQUARE-'].update('square.png')
        #wnd.window[f'-EDITSQUARE-'].update(str(buildArr))
        wnd.window.refresh()
        rembTerr=0
    if event=='Compute':
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


     
wnd.window.close()




