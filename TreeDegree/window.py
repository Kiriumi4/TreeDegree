from pydoc import visiblename
import PySimpleGUI as sg
import functions as func
import linecache

title="GUI"
fsize=10
font_text=("Helvetica", 12)
font_title=("Helvetica", 12)
font_btn=("Helvetica", 12)
print(int(linecache.getline('variables.txt',1).replace('\n','')))
print(int(linecache.getline('variables.txt',2).replace('\n','')))
num_buttons_i=100

num_buttons_j=100


theme_tree = {'BACKGROUND': '#4f6553',
                'TEXT': '#fbf2af',
                'INPUT': '#627c66',
                'TEXT_INPUT': '#fef6c0',
                'SCROLL': '#627c66',
                'BUTTON': ('#fef6c0', '#627c66'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

sg.theme_add_new('ThemeTree', theme_tree)
sg.theme('ThemeTree')


layout1 = [ 
       
    [sg.Text("Give size [meters x meters]",font = font_title)],  [sg.InputText(key='-OUTSIZE-',font=font_text)],      
    [sg.Button('Ok',font=font_btn)]
          
]
options=[
    
    [sg.Text("Inputed size",font = font_title,pad=(20,20))],
    [sg.Text("test",font = font_title,key='-INSIZE-')]
    
    ]
layout2 = [ 
        [sg.Column(options),sg.VSeperator(),sg.Column([[sg.Image('square.png',key='-SQUARE-')]])]
             
]

layout3=[
    [sg.Column(
        [[sg.Text("Editing window",font = font_title,justification='c')],
        [sg.Button('Road',pad=(0,0),key='-EDITBTN1-',font=font_btn)],
        [sg.InputText(key='-EDITBUTTS1-',visible=False,font=font_text,size=(20,10))],
        [sg.Button('Grass',pad=(0,0),key='-EDITBTN2-',font=font_btn)],
        [sg.InputText(key='-EDITBUTTS2-',visible=False,font=font_text,size=(20,10))],
        [sg.Button('Walkway',pad=(0,0),key='-EDITBTN3-',font=font_btn)],
        [sg.InputText(key='-EDITBUTTS3-',visible=False,font=font_text,size=(20,10))],
        [sg.Button('Tram tracks',pad=(0,0),key='-EDITBTN4-',font=font_btn)],
        [sg.InputText(key='-EDITBUTTS4-',visible=False,font=font_text,size=(20,10))],
        [sg.Button('Add',font=font_btn),sg.Button('Delete',font=font_btn)]]
        ),
        
        sg.VSeperator(),
        #sg.Image('square.png',key='-EDITSQUARE-'),
        sg.Column(
        [[sg.Button("   ", key=(j, i),pad=(0,0),visible=False) for i in range(num_buttons_i)] for j in range(num_buttons_j)])
    ]
]

choices=('Normal','Wild','Pretty')
choices2=('Tree1','Flowers3','Bush1','Bush2')

layout4=[
        [sg.Column(
        [[sg.Text("Options",font = font_title,pad=(20,20))],
        [sg.Listbox(choices, size=(15, len(choices)))],
        [sg.Button('Start building',font=font_btn)]]
        ),
        sg.VSeperator(),
        sg.Image('square.png',key='-BUILDSQUARE-')

    ]
   
]

layout=[
    [sg.Column([[sg.Button('New',font=font_text),sg.Button('Edit',font=font_text),sg.Button('Compute',font=font_text),sg.Button('Exit',font=font_text)]],justification='l')],
    [sg.Column(layout1, visible=False,key='-COL1-',justification='c'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-'), sg.Column(layout4, visible=False, key='-COL4-')]
]

window=sg.Window(title, layout,no_titlebar=False,grab_anywhere=True, size=(900,600))
