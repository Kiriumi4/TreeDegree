from array import typecodes
from cgitb import enable
from multiprocessing import Value
from pydoc import visiblename
import PySimpleGUI as sg
import functions as func
import linecache
import numpy as np

title="GUI"
fsize=10
font_text=("Helvetica", 12)
font_menu=("Helvetica", 13)
font_title=("Helvetica", 12)
font_btn=("Helvetica", 12)
btn_size=(15,0)
btn_size_menu=(15,0)
print(int(linecache.getline('variables.txt',1).replace('\n','')))
print(int(linecache.getline('variables.txt',2).replace('\n','')))
num_buttons_i=100

num_buttons_j=100


theme_tree = {'BACKGROUND': '#1d2e30',
                'TEXT': '#6ce2a9',
                'INPUT': '#213b38',
                'TEXT_INPUT': '#6ce2a9',
                'SCROLL': '#2e4c48',
                'BUTTON': ('#6ce2a9', '#2e4c48'),
                'PROGRESS': ('#1d2e30', '#D0D0D0'),
                'BORDER': 0,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

sg.theme_add_new('ThemeTree', theme_tree)
sg.theme('ThemeTree')

obrazek= [[sg.Image(filename='backim.png')]]

options=[
    
    [sg.Text("Chosen Size",font = font_title,pad=(20,20))],
    [sg.Text("test",font = font_title,key='-INSIZE-')]
    
    ]
layout2 = [ 
    [sg.Column(options,element_justification='c'),sg.VSeperator(),sg.Column([[sg.Image('square.png',key='-SQUARE-')]])]
             
]
buttonsLayout=[[sg.Button("    ", key=(j, i),pad=(1,1),visible=False,size=(2,1)) for i in range(num_buttons_i)] for j in range(num_buttons_j)]
columnBtn=sg.Column(buttonsLayout,key='-COLIN1-',scrollable=True,size=(1980,800),justification='c')
layout3=[
    [sg.Column([[
        sg.Column([
            [sg.Text("Editing window",font = font_title)],
            [sg.Button('Road',pad=(1,1),key='-EDITBTN1-',font=font_btn,size=btn_size)],
            [sg.InputText(key='-EDITTEXT1-',visible=False,font=font_text,size=(15,10))],
            [sg.Button('Grass',pad=(1,1),key='-EDITBTN2-',font=font_btn,size=btn_size)],
            [sg.InputText(key='-EDITTEXT2-',visible=False,font=font_text,size=(15,10))],
            [sg.Button('Walkway',pad=(1,1),key='-EDITBTN3-',font=font_btn,size=btn_size)],
            [sg.InputText(key='-EDITTEXT3-',visible=False,font=font_text,size=(15,10))],
            [sg.Button('Tram tracks',pad=(1,1),key='-EDITBTN4-',font=font_btn,size=btn_size)],
            [sg.InputText(key='-EDITTEXT4-',visible=False,font=font_text,size=(15,10))],
            [sg.Button('Sign',pad=(1,1),key='-EDITBTN5-',font=font_btn,size=btn_size)],
            [sg.InputText(key='-EDITTEXT5-',visible=False,font=font_text,size=(15,10))],
            [sg.Button('Lamp post',pad=(1,1),key='-EDITBTN6-',font=font_btn,size=btn_size)],
            [sg.InputText(key='-EDITTEXT6-',visible=False,font=font_text,size=(15,10))]
       
        ], element_justification='c',justification='l'),
        sg.Column([
            [sg.Text("Editing window",font = font_title,pad=(1,3))],
            
           
            [sg.Button('Telecommunications network',pad=(1,1),key='-EDITBTN7-',font=font_btn,size=(17,2))],
            [sg.InputText(key='-EDITTEXT7-',visible=False,font=font_text,size=(16,10))],
            [sg.Button('Electrical grid',pad=(1,1),key='-EDITBTN8-',font=font_btn,size=(17,1))],
            [sg.InputText(key='-EDITTEXT8-',visible=False,font=font_text,size=(16,10))],
            [sg.Button('Pipeline transport',pad=(1,1),key='-EDITBTN9-',font=font_btn,size=(17,1))],
            [sg.InputText(key='-EDITTEXT9-',visible=False,font=font_text,size=(16,10))],
            [sg.Button('District heating',pad=(1,1),key='-EDITBTN10-',font=font_btn,size=(17,1))],
            [sg.InputText(key='-EDITTEXT10-',visible=False,font=font_text,size=(16,10))],
            [sg.Button('Water supply network',pad=(1,1),key='-EDITBTN11-',font=font_btn,size=(17,1))],
            [sg.InputText(key='-EDITTEXT11-',visible=False,font=font_text,size=(16,10))]

        ],element_justification='c',justification='l')],[
        sg.Button('Add',font=font_btn,pad=(1,1)),sg.Button('Delete',font=font_btn,pad=(1,1))]],element_justification='c'),
       
        
        sg.VSeperator(pad=(20,10)),
        #sg.Image('square.png',key='-EDITSQUARE-'),
        columnBtn
    ]
]

choices=('Max Trees','Small Gap 1-3m','Big Gap 4-10m','Random (Gaps 0-10m)')
choices2=( 'Small Trees','Medium Trees','Big Trees','Random (All tree sizes)')

layout4=[
        [sg.Column(
            [
                [sg.Column(
                    [[sg.Text("Options - Tree Density",font = font_title,pad=(20,0))],
                    [sg.Listbox(choices, key='-OPTIONSDENSE-',size=(25, len(choices)),enable_events=True)]],pad=(5,0))
                ],
                [sg.Column(
                    [[sg.Text("Options - Tree Variation",font = font_title,pad=(20,0))],
                    [sg.Listbox(choices2, key='-OPTIONSVARIETY-', size=(25, len(choices2)),enable_events=True)]],pad=(5,0))
                 ], 
                 [sg.Button('Start building',font=font_btn)]
            ],element_justification='c'),
        sg.VSeperator(),
        sg.Image('square.png',key='-BUILDSQUARE-'),
          sg.Column(
            [
               [sg.Text("Przykladowe drzewa",font = font_title,pad=(20,0))],
               [sg.Image('2.png',size=(70,50),key='-4-'),sg.Text("Klon pospolity (Acer platanoides), osiaga srednice i wysokosc okolo 4-5 m",font = font_title,key='-4t-')],
               [sg.Image('2.png',size=(70,50),key='-2-'),sg.Text("Jesion wyniosly (Fraxinus excelsior)- srednica ok. 2m",font = font_title,key='-2t-')],
               [sg.Image('3.png',size=(70,50),key='-3-'),sg.Text("Wisnia osobliwa (Prunus x eminens) - srednica ok. 3m",font = font_title,key='-3t-')],
               [sg.Image('5.png',size=(70,50),key='-5-'),sg.Text("Magnolia Galaxy - srednica ok 5-6m",font = font_title,key='-5t-')],
               [sg.Image('7.png',size=(70,50),key='-7-'),sg.Text("Wisnia pilkowana (Prunus serrulata) -srednica ok 7m",font = font_title,key='-7t-')],
               [sg.Image('8.png',size=(70,50),key='-8-'),sg.Text("Klon polny (Acer campestre) RedShine -srednica ok 8m",font = font_title,key='-8t-')],
               [sg.Image('11.png',size=(70,50),key='-11-'),sg.Text("Klon davida (Acer davidii ) -srednica ok 11m",font = font_title,key='-11t-')],
               [sg.Image('10.png',size=(70,50),key='-10-'),sg.Text("Klon jesionolistny 'Tadeusz Szymanowski' -srednica ok 10m",font = font_title,key='-10t-')],
               [sg.Image('9.png',size=(70,50),key='-9-'),sg.Text("Buk pospolity'Luteovariegata -srednica ok 9m",font = font_title,key='-9t-')],
               [sg.Image('6.png',size=(70,50),key='-6-'),sg.Text("Kasztanowiec 'Autumn Splendor' -srednica ok 6m",font = font_title,key='-6t-')],
               [sg.Text("Przykladowe krzewy",font = font_title,pad=(20,0))],
               [sg.Image('zyw.png',size=(70,50)),sg.Text("Zywotnik",font = font_title,pad=(20,0))],
               [sg.Image('cis.png',size=(70,50)),sg.Text("Cis posredni",font = font_title,pad=(20,0))],
            ],element_justification='l',key="-TREELIST-",visible=False),

    ]
   
]


layout5=[
        [sg.Column(
            [
                [sg.Column(
                    [[sg.Text("Options - Tree Density",font = font_title,pad=(20,0))],
                    [sg.Listbox(choices, key='-OPTIONSDENSE-',size=(25, len(choices)),enable_events=True)]],pad=(5,0))
                ],
                [sg.Column(
                    [[sg.Text("Options - Tree Variation",font = font_title,pad=(20,0))],
                    [sg.Listbox(choices2, key='-OPTIONSVARIETY-', size=(25, len(choices2)),enable_events=True)]],pad=(5,0))
                 ], 
                 [sg.Button('Start building',font=font_btn)]
            ],element_justification='c'),
        sg.VSeperator(),
        sg.Image('square.png',key='-BUILDSQUARE-'),
        sg.VSeperator(),
      
       

    ]
   
]

layout=[
    [sg.Column([[sg.Button('New',font=font_menu,pad=(1,0),size=btn_size_menu),
                 sg.Button('Open',font=font_menu,pad=(0,0),size=btn_size_menu),
                 sg.Button('Edit',font=font_menu,pad=(1,0),size=btn_size_menu),
                 sg.Button('Compute',font=font_menu,pad=(0,0),size=btn_size_menu),
                 sg.Button('Save',font=font_menu,pad=(1,0),size=btn_size_menu),
                  sg.Button('',font=font_menu,pad=(0,0),size=btn_size_menu,disabled=True),
                 sg.Button('Exit',font=font_menu,pad=((1,0),0),size=btn_size_menu)]],justification='l',pad=(0,0))],
    [sg.Column(obrazek,key='-OBR-',element_justification='c',vertical_alignment='c',justification='c'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-'), sg.Column(layout4, visible=False, key='-COL4-')]
]

window=sg.Window(title, layout,no_titlebar=False,grab_anywhere=True,size=(900,600),resizable=True,finalize=True)

columnBtn.expand(True,True)


def open_new_window(typeWin,buildArr):

    layout = [[sg.Text('Choose file name:', key='-SAVEOPEN-')], [sg.InputText(key='-SAVETEXT-',font=font_text,size=(40,10))],
              [sg.Button('Ok',key='-SAVEBTN-',font=font_menu,pad=(0,0),size=btn_size_menu)]]
    if typeWin=="New":
               layout = [[sg.Text('Input size [meter x meter]:', key='-SAVEOPEN-')], [sg.InputText(key='-SAVETEXT-',font=font_text,size=(40,10))],
              [sg.Button('Ok',key='-SAVEBTN-',font=font_menu,pad=(0,0),size=btn_size_menu)]]
    window = sg.Window(typeWin+" File", layout,size=(400,100), element_justification='c')
    
    while True:
        event, values = window.read()
        print(typeWin,event)
        if typeWin=="Save" and event == '-SAVEBTN-':
                 if values['-SAVETEXT-']=='':
                     sg.Popup('Cannot save file without name')
                 else:
                    f=open(values['-SAVETEXT-'],'w')
                    strArr=str(buildArr).replace('\n','')
                    strArr=strArr.replace('[','')
                    strArr=strArr.replace(']','\n')
                    strArr=strArr.replace('  ',' ')
                    f.write(strArr)
                    f.close()
                    break
        if typeWin=="Open" and event == '-SAVEBTN-':
                 if values['-SAVETEXT-']=='':
                     sg.Popup('Cannot open file')
                 else:
                    f=open(values['-SAVETEXT-'],'r')
                    arr=np.loadtxt(values['-SAVETEXT-'],dtype=float)
                    f.close()
                    window.close()
                    return arr
        if typeWin=="New" and event == '-SAVEBTN-':
                 
                 if values['-SAVETEXT-']=='':
                     sg.Popup('No size given')
                 else:
                    c=[int(i) for i in values['-SAVETEXT-'].split() if i.isdigit()]
                    arr=np.zeros((c[0],c[1]))
                    f=open('variables.txt','w')
                    f.write(str(c[0])+"\n"+str(c[0]))
                    f.close()
                    window.close()
                    return arr,c
        if  event == sg.WIN_CLOSED:
            return 0,0
        
    window.close()


