from optparse import Values
import PySimpleGUI as sg
import window as wnd
import functions as func
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors

cmap = colors.ListedColormap(['0.5','0.1','lightgreen','0.8','brown'])
bounds=[0,1,2,3,4,5]
norm = colors.BoundaryNorm(bounds, cmap.N)




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
       #a=c[0]
       #b=c[1]
       #text=""
       #for x in range(a):
       #    text+=b*"o "
       #    text+="\n" 
       wnd.window[f'-COL1-'].update(visible=False)
       wnd.window[f'-COL2-'].update(visible=True)
       wnd.window[f'-INSIZE-'].update(values['-OUTSIZE-'])
       #wnd.window[f'-SQUARE-'].update(text)
       plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
       plt.savefig('square.png',transparent=True)
       wnd.window[f'-SQUARE-'].update('square.png')
       wnd.window.refresh()
       
    if event == 'Edit':
       wnd.window[f'-COL1-'].update(visible=False)
       wnd.window[f'-COL2-'].update(visible=False)
       wnd.window[f'-COL3-'].update(visible=True)
       wnd.window[f'-COL4-'].update(visible=False)
       #wnd.window[f'-EDITSQUARE-'].update(text)
       plt.imshow(buildArr, interpolation='nearest', cmap=cmap, norm=norm)
       plt.savefig('square.png',transparent=True)
       wnd.window[f'-EDITSQUARE-'].update('square.png')
       wnd.window.refresh()
    for i in buttKey:
        if event==i:
              wnd.window[f'-EDITBUTTS{buttNum}-'].update(visible=True)
              for j in range(1,5):
                  if j!=buttNum:
                      wnd.window[f'-EDITBUTTS{j}-'].update(visible=False)
                     
              wnd.window.refresh()
        buttNum+=1
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
        wnd.window[f'-EDITSQUARE-'].update('square.png')
        #wnd.window[f'-EDITSQUARE-'].update(str(buildArr))
        wnd.window.refresh()
        func.algorithm(buildArr)
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
        wnd.window[f'-EDITSQUARE-'].update('square.png')
        #wnd.window[f'-EDITSQUARE-'].update(str(buildArr))
        wnd.window.refresh()
    if event=='Compute':
        wnd.window[f'-COL1-'].update(visible=False)
        wnd.window[f'-COL2-'].update(visible=False)
        wnd.window[f'-COL3-'].update(visible=False)
        wnd.window[f'-COL4-'].update(visible=True)
        wnd.window[f'-BUILDSQUARE-'].update('square.png')
        wnd.window.refresh()

     
wnd.window.close()




