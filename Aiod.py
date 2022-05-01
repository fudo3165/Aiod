import tkinter as tk
from tkinter import *
import os
import os.path
from unittest.util import _count_diff_all_purpose

def Main():

    global color1
    global color2
    global color3
    global color4
    global color5
    global color6
    global color7
    global color8
    global color9
    global color10
    global color11
    global color12
    global color13
    global color14
    global color15
    global color16
    global color17
    global color18
    global color19
    global color20
    global color21
    global color22
    global color23
    global color24
    global color25

    color1 = ('#CD6155')
    color2 = ('#EC7063')
    color3 = ('#AF7AC5')
    color4 = ('#A569BD')
    color5 = ('#5499C7')
    color6 = ('#5DADE2')
    color7 = ('#48C9B0')
    color8 = ('#52BE80')
    color9 = ('#58D68D')
    color10 = ('#F4D03F')
    color11 = ('#F5B041')
    color12 = ('#EB984E')
    color13 = ('#DC7633')
    color14 = ('#F0F3F4')
    color15 = ('#CACFD2')
    color16 = ('#AAB7B8')
    color17 = ('#AAB7B8')
    color18 = ('#5D6D7E')
    color19 = ('#566573')
    color20 = ('#DFFF00')
    color21 = ('#FFBF00')
    color22 = ('#FF7F50')
    color23 = ('#DE3163')
    color24 = ('#9FE2BF')
    color25 = ('#CCCCFF')

    global setingFolder
    global backgroundColorFile
    global foregroundColorFile
    global setingFile

    user = os.getlogin()

    folderSave = ('/inode/directory')

    setingFolder = (f'/home/{user}/Aiod')
    setingFile = (f'/home/{user}/Aiod/folder.aid')
    backgroundColorFile = (f'/home/{user}/Aiod/backgroundColor.aid')
    foregroundColorFile = (f'/home/{user}/Aiod/foregroundColor.aid')

    check_folder = os.path.exists(f'{setingFolder}')
    check_file = os.path.exists(f'{setingFile}')
    checkBackgroundColor = os.path.exists(f'{backgroundColorFile}')
    checkForegroundColor = os.path.exists(f'{foregroundColorFile}')

    if(check_folder == True):
        check1 = True
    if(check_folder == False):
        os.system(f'mkdir {setingFolder}')
        check1 = True

    if(check_file == True):
        check2 = True

    if(checkBackgroundColor == True):
        check3 = True

    if(checkForegroundColor == True):
        check4 = True

    if(check_file == False):
        createSeting = open(f'{setingFile}', 'w')
        createSeting.write(f'{folderSave}')
        createSeting.close()
        check2 = True

    if(checkBackgroundColor == False):
        create1 = open(f'{backgroundColorFile}', 'w')
        create1.write(f'white')
        create1.close()
        check3 = True

    if(checkForegroundColor == False):
        create2 = open(f'{foregroundColorFile}', 'w')
        create2.write(f'black')
        create2.close()
        check4 = True


    if(check1 and check2 == True):
        Start()
    else:
        Error()


    Start()

def Error():
    print('Error!')
    input()
    quit()

def Start():
    #Start program!

    #folder
    user = os.getlogin()
    setingFile = (f'/home/{user}/Aiod/folder.aid')
    #folder


    #function main
    def savingFolder():

        #Seting window

        global setingFolder
        global backgroundColorFile
        global foregroundColorFile
        global setingFile

        readBackground = open(backgroundColorFile)
        readForeground = open(foregroundColorFile)

        background = readBackground.read()
        foreground = readForeground.read()

        Seting = tk.Tk()
        Seting['bg']=background
        Seting.title('Save folder')
        Seting.resizable(width=FALSE, height=FALSE)
        Seting.geometry('300x155')

        #Seting function

        def Save_Folder():
            global message
            S_F = message.get()
            SF = open(f'{setingFile}', 'w')
            SF.write(f'{S_F}')
            SF.close()
            ok = tk.Label(Seting, text='Ok', fg='green', bg=background).place(x=0, y=70, width=300, height= 30)
            message.delete("0", END)

        #Seting function

        #Seting label
        text = tk.Label(Seting, text='Save folder', bg=background, fg=foreground).place(x=0, y=0, width=300, height=30)
        #Seting label

        #Seting Entry
        global message
        ins = open(setingFile, 'r')
        ins2 = ins.read()
        message = Entry(Seting, bg=background, fg=foreground)
        message.place(x=0, y=30, width=300, height=30)
        message.insert(0, f"{ins2}")

        #Seting Entry

        #Seting button
        b4 = tk.Button(Seting, text='Ok', bg=background, fg=foreground, command=Save_Folder).place(x=0, y=100, width=300, height=55)
        #Seting button

        Seting.mainloop()
        #Seting window

    def colorFg():
        global color1
        global color2
        global color3
        global color4
        global color5
        global color6
        global color7
        global color8
        global color9
        global color10
        global color11
        global color12
        global color13
        global color14
        global color15
        global color16
        global color17
        global color18
        global color19
        global color20
        global color21
        global color22
        global color23
        global color24
        global color25

        global backgroundColorFile
        global foregroundColorFile
        global setingFile

        readBackground = open(backgroundColorFile)
        readForeground = open(foregroundColorFile)

        background = readBackground.read()
        foreground = readForeground.read()

        fg = tk.Tk()
        fg.title('Foreground color')
        fg.resizable(width=FALSE, height=FALSE)
        fg.geometry('216x82')
        fg['bg']=background

        #fg function

        def Color1():
            colorFg = (f'{color1}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color2():
            colorFg = (f'{color2}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color3():
            colorFg = (f'{color3}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color4():
            colorFg = (f'{color4}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color5():
            colorFg = (f'{color5}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color6():
            colorFg = (f'{color6}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color7():
            colorFg = (f'{color7}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color8():
            colorFg = (f'{color8}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color9():
            colorFg = (f'{color9}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color10():
            colorFg = (f'{color10}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color11():
            colorFg = (f'{color11}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color12():
            colorFg = (f'{color12}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color13():
            colorFg = (f'{color13}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color14():
            colorFg = (f'{color14}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color15():
            colorFg = (f'{color15}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color16():
            colorFg = (f'{color16}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color17():
            colorFg = (f'{color17}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color18():
            colorFg = (f'{color18}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()
        
        def Color19():
            colorFg = (f'{color19}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color20():
            colorFg = (f'{color20}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color21():
            colorFg = (f'{color21}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color22():
            colorFg = (f'{color22}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color23():
            colorFg = (f'{color23}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color24():
            colorFg = (f'{color24}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color25():
            colorFg = (f'{color25}')
            sFg = open(foregroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        #fg function

        #fg button
        c=tk.Button(fg, bg=color1, command=Color1).place(x=2, y=2, width=25, height=25)
        c=tk.Button(fg, bg=color2, command=Color2).place(x=28, y=2, width=25, height=25)
        c=tk.Button(fg, bg=color3, command=Color3).place(x=55, y=2, width=25, height=25)
        c=tk.Button(fg, bg=color4, command=Color4).place(x=82, y=2, width=25, height=25)
        c=tk.Button(fg, bg=color6, command=Color6).place(x=109, y=2, width=25, height=25)
        c=tk.Button(fg, bg=color7, command=Color7).place(x=136, y=2, width=25, height=25)
        c=tk.Button(fg, bg=color8, command=Color8).place(x=163, y=2, width=25, height=25)
        c=tk.Button(fg, bg=color9, command=Color9).place(x=190, y=2, width=25, height=25)
        c=tk.Button(fg, bg=color10, command=Color10).place(x=2, y=28, width=25, height=25)
        c=tk.Button(fg, bg=color11, command=Color11).place(x=28, y=28, width=25, height=25)
        c=tk.Button(fg, bg=color12, command=Color12).place(x=55, y=28, width=25, height=25)
        c=tk.Button(fg, bg=color13, command=Color13).place(x=82, y=28, width=25, height=25)
        c=tk.Button(fg, bg=color14, command=Color14).place(x=109, y=28, width=25, height=25)
        c=tk.Button(fg, bg=color15, command=Color15).place(x=136, y=28, width=25, height=25)
        c=tk.Button(fg, bg=color16, command=Color16).place(x=163, y=28, width=25, height=25)
        c=tk.Button(fg, bg=color17, command=Color17).place(x=190, y=28, width=25, height=25)
        c=tk.Button(fg, bg=color18, command=Color18).place(x=2, y=55, width=25, height=25)
        c=tk.Button(fg, bg=color19, command=Color19).place(x=28, y=55, width=25, height=25)
        c=tk.Button(fg, bg=color20, command=Color20).place(x=55, y=55, width=25, height=25)
        c=tk.Button(fg, bg=color21, command=Color21).place(x=82, y=55, width=25, height=25)
        c=tk.Button(fg, bg=color22, command=Color22).place(x=109, y=55, width=25, height=25)
        c=tk.Button(fg, bg=color23, command=Color23).place(x=136, y=55, width=25, height=25)
        c=tk.Button(fg, bg=color24, command=Color24).place(x=163, y=55, width=25, height=25)
        c=tk.Button(fg, bg=color25, command=Color25).place(x=190, y=55, width=25, height=25)
        #fg button

        fg.mainloop()

    def colorBg():

        global color1
        global color2
        global color3
        global color4
        global color5
        global color6
        global color7
        global color8
        global color9
        global color10
        global color11
        global color12
        global color13
        global color14
        global color15
        global color16
        global color17
        global color18
        global color19
        global color20
        global color21
        global color22
        global color23
        global color24
        global color25

        global backgroundColorFile
        global foregroundColorFile
        global setingFile

        readBackground = open(backgroundColorFile)
        readForeground = open(foregroundColorFile)

        background = readBackground.read()
        foreground = readForeground.read()

        #Bg
        bg = tk.Tk()
        bg.title('Background color')
        bg.resizable(width=FALSE, height=FALSE)
        bg.geometry('216x82')
        bg['bg']=background

        #bg

        def Color1():
            colorFg = (f'{color1}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color2():
            colorFg = (f'{color2}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color3():
            colorFg = (f'{color3}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color4():
            colorFg = (f'{color4}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color5():
            colorFg = (f'{color5}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color6():
            colorFg = (f'{color6}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color7():
            colorFg = (f'{color7}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color8():
            colorFg = (f'{color8}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color9():
            colorFg = (f'{color9}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color10():
            colorFg = (f'{color10}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color11():
            colorFg = (f'{color11}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color12():
            colorFg = (f'{color12}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color13():
            colorFg = (f'{color13}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color14():
            colorFg = (f'{color14}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color15():
            colorFg = (f'{color15}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color16():
            colorFg = (f'{color16}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color17():
            colorFg = (f'{color17}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color18():
            colorFg = (f'{color18}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()
        
        def Color19():
            colorFg = (f'{color19}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color20():
            colorFg = (f'{color20}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color21():
            colorFg = (f'{color21}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color22():
            colorFg = (f'{color22}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color23():
            colorFg = (f'{color23}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color24():
            colorFg = (f'{color24}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        def Color25():
            colorFg = (f'{color25}')
            sFg = open(backgroundColorFile, 'w')
            sFg.write(f'{colorFg}')
            sFg.close()

        #bg button
        c=tk.Button(bg, bg=color1, command=Color1).place(x=2, y=2, width=25, height=25)
        c=tk.Button(bg, bg=color2, command=Color2).place(x=28, y=2, width=25, height=25)
        c=tk.Button(bg, bg=color3, command=Color3).place(x=55, y=2, width=25, height=25)
        c=tk.Button(bg, bg=color4, command=Color4).place(x=82, y=2, width=25, height=25)
        c=tk.Button(bg, bg=color6, command=Color6).place(x=109, y=2, width=25, height=25)
        c=tk.Button(bg, bg=color7, command=Color7).place(x=136, y=2, width=25, height=25)
        c=tk.Button(bg, bg=color8, command=Color8).place(x=163, y=2, width=25, height=25)
        c=tk.Button(bg, bg=color9, command=Color9).place(x=190, y=2, width=25, height=25)
        c=tk.Button(bg, bg=color10, command=Color10).place(x=2, y=28, width=25, height=25)
        c=tk.Button(bg, bg=color11, command=Color11).place(x=28, y=28, width=25, height=25)
        c=tk.Button(bg, bg=color12, command=Color12).place(x=55, y=28, width=25, height=25)
        c=tk.Button(bg, bg=color13, command=Color13).place(x=82, y=28, width=25, height=25)
        c=tk.Button(bg, bg=color14, command=Color14).place(x=109, y=28, width=25, height=25)
        c=tk.Button(bg, bg=color15, command=Color15).place(x=136, y=28, width=25, height=25)
        c=tk.Button(bg, bg=color16, command=Color16).place(x=163, y=28, width=25, height=25)
        c=tk.Button(bg, bg=color17, command=Color17).place(x=190, y=28, width=25, height=25)
        c=tk.Button(bg, bg=color18, command=Color18).place(x=2, y=55, width=25, height=25)
        c=tk.Button(bg, bg=color19, command=Color19).place(x=28, y=55, width=25, height=25)
        c=tk.Button(bg, bg=color20, command=Color20).place(x=55, y=55, width=25, height=25)
        c=tk.Button(bg, bg=color21, command=Color21).place(x=82, y=55, width=25, height=25)
        c=tk.Button(bg, bg=color22, command=Color22).place(x=109, y=55, width=25, height=25)
        c=tk.Button(bg, bg=color23, command=Color23).place(x=136, y=55, width=25, height=25)
        c=tk.Button(bg, bg=color24, command=Color24).place(x=163, y=55, width=25, height=25)
        c=tk.Button(bg, bg=color25, command=Color25).place(x=190, y=55, width=25, height=25)
        #bg button

        bg.mainloop()
        

    def add():
        global setingFile
        global Name
        if var.get() == 0:
            otv = ('false')

        if var.get() == 1:
            otv = ('true')

        Oname = oName.get()
        Ocomment = oComment.get()
        Ocommand = oCommand.get()
        Oicon = oIcon.get()

        readSetingFile1 = open(setingFile, 'r')
        readSetingFile2 = readSetingFile1.read()

        desktop = open(f'{readSetingFile2}{Oname}.desktop', 'w')
        desktop.write('[Desktop Entry]\n')
        desktop.write('Version=1.0\n')
        desktop.write(f'Name={Oname}\n')
        desktop.write(f'Comment={Ocomment}\n')
        desktop.write(f'Exec={Ocommand}\n')
        desktop.write(f'Icon={Oicon}\n')
        desktop.write(f'Terminal={otv}\n')
        desktop.write(f'Type=Application\n')
        desktop.write(f'Categories=Aiod\n')
        desktop.close()

    #function main


    #Main window!
    global setingFolder
    global backgroundColorFile
    global foregroundColorFile

    global Name

    readBackground = open(backgroundColorFile)
    readForeground = open(foregroundColorFile)

    background = readBackground.read()
    foreground = readForeground.read()

    main = tk.Tk()
    main.title('Aiod')
    main['bg']=background
    main.resizable(width=False, height=FALSE)
    main.geometry('500x600')
    #Main window!

    #Button
    b1 = tk.Button(text='Save folder', bg=background, fg=foreground, command=savingFolder).place(x=0, y=0, width=166.66, height=30)
    b2 = tk.Button(text='Background color', bg=background, fg=foreground, command=colorBg).place(x=166.66, y=0, width=166.66, height=30)
    b3 = tk.Button(text='Foreground color', bg=background, fg=foreground, command=colorFg).place(x=334.32, y=0, width=166.66, height=30)

    #Entry
    oName = StringVar()
    Name = Entry(main, bg=background, fg=foreground, textvariable = oName).place(x=75, y=54, width=425, height=30)
    oComment = StringVar()
    Comment = Entry(main, bg=background, fg=foreground, textvariable = oComment).place(x=75, y=110, width=425, height=30)
    oCommand = StringVar()
    Command = Entry(main, bg=background, fg=foreground, textvariable = oCommand).place(x=75, y=166, width=425, height=30)
    oIcon = StringVar()
    Icon = Entry(main, bg=background, fg=foreground, textvariable = oIcon).place(x=75, y=222, width=425, height=30)
    #ENTRY

    #label
    text=tk.Label(text='Name', bg=background, fg=foreground).place(x=0, y=54, width=65, height=30 )
    text=tk.Label(text='Comment', bg=background, fg=foreground).place(x=0, y=110, width=65, height=30 )
    text=tk.Label(text='Command', bg=background, fg=foreground).place(x=0, y=166, width=65, height=30 )
    text=tk.Label(text='Icon', bg=background, fg=foreground).place(x=0, y=222, width=65, height=30 )
    text=tk.Label(text='Terminal', bg=background, fg=foreground).place(x=0, y=267, width=65, height=30 )

    var = IntVar()
    var.set(0)
    red = Radiobutton(text="True", bg=background, fg=foreground, variable=var, value=1).place(x=75, y=267)
    green = Radiobutton(text="False", bg=background, fg=foreground, variable=var, value=0).place(x=200, y=267)
    #label

    add = tk.Button(text='Add', bg=background, fg=foreground, command=add).place(x=0, y=540, width=500, height=60)
    
    main.mainloop()

Main()
