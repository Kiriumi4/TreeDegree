from pydoc import visiblename
import PySimpleGUI as sg
import functions as func
import linecache

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


layout1 = [ 
       
    [sg.Text("Give size [meters x meters]",font = font_title)],  [sg.InputText(key='-OUTSIZE-',font=font_text)],      
    [sg.Button('Ok',font=font_btn,size=btn_size)]
          
]
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
    [sg.Column(
        [[sg.Text("Editing window",font = font_title)],
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
        [sg.Button('Add',font=font_btn,pad=(1,1)),sg.Button('Delete',font=font_btn,pad=(1,1))]],
        element_justification='c',justification='l'),
        
        sg.VSeperator(pad=(20,10)),
        #sg.Image('square.png',key='-EDITSQUARE-'),
        columnBtn
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
    [sg.Column([[sg.Button('New',font=font_menu,pad=(0,0),size=btn_size_menu),
                 sg.Button('Edit',font=font_menu,pad=(0,0),size=btn_size_menu),
                 sg.Button('Compute',font=font_menu,pad=(0,0),size=btn_size_menu),
                 sg.Button('Exit',font=font_menu,pad=(0,0),size=btn_size_menu)]],justification='l',pad=(0,0))],
    [sg.Column(layout1, visible=False,key='-COL1-',element_justification='c',vertical_alignment='c',justification='c'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-'), sg.Column(layout4, visible=False, key='-COL4-')]
]

window=sg.Window(title, layout,no_titlebar=False,grab_anywhere=True,size=(900,600),resizable=True,finalize=True)

columnBtn.expand(True,True)
