from Widget import *
from PIL import Image,ImageTk,ImageFilter
from configparser import ConfigParser

global Colors
Colors=['#3e1515','#32100f','white','#85f88d','#260606','#9d0000','#32100f','#5757ED','#9d0000','#260606']
root=Tk()
root.overrideredirect(True)
root.iconbitmap('images\\data_ico.ico')
root.title('Dataabase Control')
try:
    parser=ConfigParser()
    parser.read('Themes.txt')
    col=parser.get('Defualt','color2')
    root.config(bg=col)
except:pass
def Size_midel(x_s,y_s):
    x_size=str((root.winfo_screenwidth()/2)-(x_s/2))
    y_size=str((root.winfo_screenheight()/2)-(y_s/2)-10)
    lista=[]
    lista1=[]
    for i in x_size:
        lista.append(i)
    for i in y_size:
        lista1.append(i)
    lista.pop()
    lista.pop()
    lista1.pop()
    lista1.pop()
    vvvar=''.join(lista)
    vvvar1=''.join(lista1)
    return f"{x_s}x{y_s}+{vvvar}+{vvvar1}"
root.geometry(Size_midel(600,400))
frame_forb=Frame(root)
frame_forb.pack(fill=BOTH,expand=True)
canvas=Canvas(frame_forb,width=400,height=300,highlightthickness=0)
canvas.pack(fill=BOTH,expand=True)
f_im=Image.open('images\\run_image.jpg')
f_im=f_im.resize((600,400),Image.Resampling.LANCZOS)
f_im=ImageTk.PhotoImage(f_im.filter(ImageFilter.GaussianBlur(1.5)))
canvas.create_image(0,0,image=f_im,anchor='nw')
ima=Image.open('images\\acept_database.png')
ima=ImageTk.PhotoImage(ima.resize((150,150),Image.Resampling.LANCZOS))
canvas.create_image(150,315,image=ima)
canvas.create_text(295,35,text='Database_Server',fill='#ff3737',font=('tajwal',25,'bold'))

def switch():
    frame_forb.destroy()
    My_App()    
    
def show_text_in_image(show_text,place):
    create_list=[0,'']
    text=canvas.create_text(    (place),
                                fill='#b67749',
                                font=('Microsoft YaHei UI Light',14,'bold'),
                                anchor='sw')
    def r():
        try:
            create_list[1] += (show_text[create_list[0]])
            canvas.itemconfig(text,text=create_list[1])
            create_list[0]+=1
            root.after(30,r)
        except:
            pass
    r()
root.after(200,lambda: show_text_in_image('√ Connect to server...',(250,280)))
root.after(500,lambda: show_text_in_image('√ Control Database...' ,(250,310)))
root.after(800,lambda: show_text_in_image('√ Add information...'  ,(250,340)))
root.after(1100,lambda: show_text_in_image('√ Control DB ...'     ,(250,370)))
root.after(2000,switch)

def My_App():
    import mysql.connector
    from tkinter import messagebox 
    from tkinter import ttk 
    from tkinter import filedialog
    import os
    from ctypes import windll
    import win32gui , win32con

    root.minimized = False
    root.maximized = False

    def set_appwindow(mainWindow): 
        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080
        hwnd = windll.user32.GetParent(mainWindow.winfo_id())
        stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        stylew = stylew & ~WS_EX_TOOLWINDOW
        stylew = stylew | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
        mainWindow.wm_withdraw()
        mainWindow.after(10, lambda: mainWindow.wm_deiconify())
    root.after(10, lambda: set_appwindow(root))
    
    def minimize_me():
        minimize_app=win32gui.GetForegroundWindow()
        win32gui.ShowWindow(minimize_app,win32con.SW_MINIMIZE)
    
    def maximize_me():
        if root.maximized == False: 
            root.normal_size = root.geometry()
            expand_button.config(text="2")
            root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
            root.maximized = not root.maximized 
            root.after(50,move_widget)
        else:
            expand_button.config(text="1")
            root.geometry(root.normal_size)
            root.maximized = not root.maximized
            root.after(50,move_widget)
    Container_Configer_Color=['','','','','','']

    def Change_Colors(colors):
        for fonction in Container_Configer_Color:
            try:
                fonction(colors)
            except:pass

    def Theme(section):
        options=['color1','color2','color3','color4','color5',
                'color6','color7','color8','color9','color10']
        try:
            parser=ConfigParser()
            parser.read('files\\Themes.txt')  
            if parser.has_section(section):
                colors_list=[]
                for option in options:
                    try:
                        colors_list.append(parser.get(section,option))
                    except:
                        colors_list.append('white')
                global Colors
                Colors=colors_list.copy()
                for c in range(len(colors_list)):
                    parser.set('Defualt',options[c],colors_list[c])
                with open('files\\Themes.txt','w') as config:
                    parser.write(config)
                Change_Colors(Colors)
        except:pass     
    Theme('Defualt')
    root.config(bg=Colors[1])
    global my_top
    my_top=''
    def Meak_Theme():
        def top():
            global my_top
            from tkinter import colorchooser
            top=Toplevel()
            my_top=top
            top.title('Meak Theme')
            top.geometry(Size_midel(300,400))
            top.resizable(0,0)
            oreginal_colors=Colors.copy()
            list_colors11=Colors.copy()
            def cancel():
                global Colors
                Colors=oreginal_colors.copy()
                Change_Colors(Colors)
                top.destroy()
            def a(n,c):
                def color1():
                    var=colorchooser.askcolor()[1]
                    if var:
                        Butt111.config(bg=var)
                        list_colors11[n]=var
                    top.focus()
                f=Frame(top)
                f.pack(fill=X)
                if c=='':
                    c='black'
                Label(f,text='Defult',bg=c).pack(side=LEFT,padx=2,pady=1)
                Butt111=Button(f,text=f'color {n}',bd=1,relief=RIDGE,command=color1)
                Butt111.pack(fill=X,padx=1,pady=2)
            for n in range(len(list_colors11)):
                a(n,list_colors11[n])     
            def Save_Theme():
                def Save():
                    parser=ConfigParser()
                    parser.read('files\\Themes.txt')
                    check=parser.has_section(ent.get())
                    if not check:
                        parser.add_section(ent.get())
                        parser.set(ent.get(),'color1',list_colors11[0])
                        parser.set(ent.get(),'color2',list_colors11[1])
                        parser.set(ent.get(),'color3',list_colors11[2])
                        parser.set(ent.get(),'color4',list_colors11[3])
                        parser.set(ent.get(),'color5',list_colors11[4])
                        parser.set(ent.get(),'color6',list_colors11[5])
                        parser.set(ent.get(),'color7',list_colors11[6])
                        parser.set(ent.get(),'color8',list_colors11[7])
                        parser.set(ent.get(),'color9',list_colors11[8])
                        parser.set(ent.get(),'color10',list_colors11[9])
                        with open('files\\Themes.txt','w') as config:
                            parser.write(config)
                        frame_confirme.destroy()
                        Change_Colors(list_colors11)
                        pick_themes_on_menu()
                        top.destroy()

                    else:
                        global l3331
                        try:
                            l3331.destroy()
                        except:pass
                        ent.delete(0,'end')
                        l3331=Label(frame_confirme,
                                    text='Theme alredy exeste !',
                                    bg='white',
                                    fg='red')
                        l3331.place(x=20,y=100)              
                def Cancel():
                    frame_confirme.destroy()
                frame_confirme=Frame(top,
                                bg='white',
                                highlightthicknes=1,
                                highlightbackground='#5757ED',
                                highlightcolor='#5757ED')
                frame_confirme.place(x=25,y=100,width=250,height=200)
                l=Label(frame_confirme,text='Theme Name',bg='white',font=('tajwal',12,'bold'))
                l.place(x=5,y=18)
                ent=Entry(frame_confirme,bg='white',justify='center')
                ent.place(x=120,y=20)
                fx=Frame(frame_confirme,bg='white')
                fx.pack(side=BOTTOM,fill=X)
                b1=Button(fx,text='Save',bd=1,relief=RIDGE,command=Save,width=8)
                b1.pack(side=RIGHT,padx=4,pady=2)
                b2=Button(fx,text='Cancel',bd=1,relief=RIDGE,command=Cancel,width=8)
                b2.pack(side=RIGHT,padx=4,pady=2)
            def apply1():
                global Colors
                Colors=list_colors11.copy()
                Change_Colors(Colors)
            f2=Frame(top)
            f2.pack(side=BOTTOM,fill=X)
            b1=Button(f2,text='Apply',bd=1,relief=RIDGE,command=apply1,width=8)
            b1.pack(side=RIGHT,padx=4,pady=2)
            b2=Button(f2,text='Save',bd=1,relief=RIDGE,command=Save_Theme,width=8)
            b2.pack(side=RIGHT,padx=4,pady=2)
            b3=Button(f2,text='Cancel',bd=1,relief=RIDGE,command=cancel,width=8)
            b3.pack(side=RIGHT,padx=4,pady=2)

            top.mainloop()     
        global my_top
        if my_top != '':
            try:
                my_top.focus()
            except:
                top()
        else:
            top()

    class My_Widget:
        enter_image=PhotoImage(file='images\\123456.png')
        enter_image_fucos=PhotoImage(file='images\\112233.png')
        flash_down=PhotoImage(file='images\\flashdown.png')
        flash_up=PhotoImage(file='images\\flashup.png')
        flash_up_active=PhotoImage(file='images\\flashup_active.png')
        var_order=False
        buttons_=[]
        var=True

        def My_Button(place,Text,command,Database_name=None,right_command=None):
            Frame_name=Frame(place,
                            width=250,
                            height=30,
                            bg=Colors[6],
                            highlightbackground=Colors[5],
                            highlightcolor=Colors[5],
                            highlightthicknes=1)
            Frame_name.pack(pady=1)
            label1=Label(Frame_name,text=f'  {Text}',anchor=W,fg=Colors[2],bg=Colors[6],width=34)
            label1.place(x=1,y=4)
            VarList=[0,250,30,False,False]
            def De3():
                Frame_name.config(bg=Colors[6],
                                    highlightbackground=Colors[5],
                                    highlightcolor=Colors[5])
                label1.config(bg=Colors[6],fg=Colors[2])
                Frame_name.pack(pady=1)
                VarList[3]=False
                VarList[4]=False
                def aaaaa1():
                    if VarList[0] > 0 :
                        VarList[0] -= 1
                        VarList[1] -= 2
                        VarList[2] -= 1
                        Frame_name.config(width=VarList[1],height=VarList[2])
                        root.after(20,aaaaa1)
                aaaaa1()
            def De2():
                Frame_name.config(bg=Colors[0],
                                highlightbackground=Colors[7],
                                highlightcolor=Colors[7])
                label1.config(bg=Colors[0],fg=Colors[7])
                Frame_name.pack(pady=0)
                VarList[3]=True
                def aaaaa():
                    v=True
                    if VarList[0] < 4 and v:
                        if VarList[3]  :
                            VarList[0] += 1
                            VarList[1] += 2
                            VarList[2] += 1
                            Frame_name.config(width=VarList[1],height=VarList[2])
                            root.after(20, aaaaa)
                        else:
                            v=False 
                aaaaa()
            def return_click(event):
                Sheck_Var=VarList[3]
                if Sheck_Var:
                    Frame_name.config(bg=Colors[0],highlightthicknes=1)
                    label1.config(bg=Colors[0],fg=Colors[7])
                else:
                    Frame_name.config(bg=Colors[6],highlightthicknes=1)
                    label1.config(bg=Colors[6],fg=Colors[2])
            def Click(event):
                Frame_name.focus()
                if Database_name:
                    command(Text,Database_name)
                else:
                    command(Text)
                VarList[4]=True 
                Frame_name.config(bg=Colors[6],highlightthicknes=3)
                label1.config(bg=Colors[6],fg='red')
            if right_command:
                def my_minu(event):
                    if Database_name:
                        right_command(event,Database_name,Text)
                    else:right_command(event,Text)
                Frame_name.bind('<ButtonRelease-3>',my_minu)
                label1.bind('<ButtonRelease-3>',my_minu)
            Frame_name.bind('<Enter>',lambda e: De2() )
            Frame_name.bind('<Leave>',lambda e: De3() )
            Frame_name.bind('<Button-1>',Click )
            label1.bind('<Button-1>',Click )
            Frame_name.bind('<ButtonRelease-1>',return_click )
            label1.bind('<ButtonRelease-1>',return_click )

            class config:
                def config(bg=None,fg=None,highlightbackground=None):
                    if bg:
                        Frame_name.config(bg=bg)
                        label1.config(bg=bg)
                    if fg:
                        label1.config(fg=fg)
                    if highlightbackground:
                        Frame_name.config(highlightbackground=highlightbackground)
            return config

        def Minu_Button(Uframe,Text,my_command=None,setings=None,com_g_click=None,return_name=None):
            my_varible=Label(Uframe,
                        text=f'    {Text}',
                        anchor=W,
                        cursor='hand2',
                        width=30,
                        bg=Colors[6],
                        fg=Colors[2],
                        font=('Verdana',8))
            def Fook(event):
                my_varible.config(bg=Colors[0],fg=Colors[7])
            def Taht(event):
                my_varible.config(bg=Colors[6],fg=Colors[2])
            def click_mn_b(event):
                my_varible.config(bg=Colors[4])
                try:
                    Uframe.destroy()
                except:pass
                if com_g_click:
                    com_g_click()
                if my_command:
                    if setings:
                        my_command((Text , setings))
                    elif return_name:
                        my_command(Text)
                    else:
                        my_command()
                def return_mn_b():
                    try:
                        my_varible.config(bg=Colors[6])
                    except:pass
                root.after(100,return_mn_b)
            my_varible.bind('<Enter>',Fook)
            my_varible.bind('<Leave>',Taht)
            my_varible.bind('<ButtonRelease-1>',click_mn_b)
            my_varible.pack(padx=1,ipady=3)
        
        def Menu_Bar(frame,menu_name,valuse=None,commands=None,return_name=None):
            return_name0=['']
            return_name0[0]=return_name
            valuse0=[]
            if valuse:
                valuse0=valuse.copy()
            commands0=[]
            if commands:
                commands0=commands.copy()
            def menu():
                My_Widget.var=False
                global Frame00
                try:
                    for b in My_Widget.buttons_:
                        b.config(bg=Colors[1],fg=Colors[2])
                    TT['bg']=Colors[0]
                    TT['fg']=Colors[7]
                    Frame00.destroy()
                except:pass
                Frame00=Frame(root,
                            bd=0,
                            bg=Colors[6],
                            highlightbackground=Colors[7],
                            highlightcolor=Colors[7],
                            highlightthickness=1)
                Frame00.place(x=TT.winfo_x(),y=TT.winfo_y()+20)
                Frame00.focus()
                def return_color():
                    My_Widget.var_order=False
                    My_Widget.var=True
                    for b in My_Widget.buttons_:
                        b.config(bg=Colors[1],fg=Colors[2])

                for a in range(len(valuse0)):
                    if valuse0[a] == 'tear':
                        Fr=Frame(Frame00,width=140,height=1,bg=Colors[7])
                        Fr.pack()
                    else:
                        if return_name0[0]:
                            My_Widget.Minu_Button(Uframe=Frame00,
                                                Text=valuse0[a],
                                                my_command=commands0[a],
                                                setings=None,
                                                com_g_click=return_color,
                                                return_name=True)
                        else:
                            My_Widget.Minu_Button(Uframe=Frame00,
                                                Text=valuse0[a],
                                                my_command=commands0[a],
                                                setings=None,
                                                com_g_click=return_color)
                def focusout(event):
                    try:
                        My_Widget.var=True
                        for b in My_Widget.buttons_:
                            b.config(bg=Colors[1],fg=Colors[2])
                        Frame00.destroy()    
                    except:pass
                    My_Widget.var_order=False
                Frame00.bind('<FocusOut>',focusout)
            TT=Label(frame,
                    text=menu_name,
                    bg=Colors[1],
                    padx=2,
                    pady=0,
                    fg=Colors[2])
            TT.pack(side=LEFT, padx=5)
            My_Widget.buttons_.append(TT)
            def TT_Enter(event):
                if My_Widget.var:
                    TT['bg']=Colors[0]
                    TT['fg']=Colors[7]
                if My_Widget.var_order:
                    menu()
            def TT_Leave(event):
                if My_Widget.var:
                    TT['bg']=Colors[1]
                    TT['fg']=Colors[2]
            def click(event):
                if My_Widget.var_order:
                    My_Widget.var_order=False
                    My_Widget.var=True
                    Frame00.destroy()
                else:
                    menu()
                    My_Widget.var_order=True
            TT.bind('<Enter>',TT_Enter)
            TT.bind('<Leave>',TT_Leave)
            TT.bind('<Button-1>',click)
            class config:
                def config(bg=None,fg=None):
                    if bg:
                        TT.config(bg=bg)
                    if fg:
                        TT.config(fg=fg)
                def values_commands(values=None,commands=None,return_name=None):
                    if values:
                        valuse0.clear()
                        for row in values:
                            valuse0.append(row)
                    if commands:
                        commands0.clear()
                        for rowc in commands:
                            commands0.append(rowc)
                    if return_name:
                        return_name0[0]=True
            return config

        def My_Menu(event,values,commands):
            global my_minu_frame
            try:
                my_minu_frame.destroy()
            except:pass
            my_minu_frame=Frame(root,
                                bd=0,
                                bg=Colors[6],
                                highlightbackground=Colors[7],
                                highlightcolor=Colors[7],
                                highlightthickness=1)
            height_of_frame=0
            for i in range(len(values)):
                if values[i] == 'tear':
                    Fr=Frame(my_minu_frame,width=140,height=1,bg=Colors[7])
                    Fr.pack()
                else:
                    My_Widget.Minu_Button(my_minu_frame,f'{values[i]}',commands[i])
                    height_of_frame+=27
            mause_in_root=event.y_root-root.winfo_y()
            root_height=root.winfo_height()
            vaarr=mause_in_root+height_of_frame
            vaarr1=vaarr-root_height
            if vaarr <= root_height:
                my_minu_frame.place(x=event.x_root-root.winfo_x(),y=mause_in_root)
            else:
                my_minu_frame.place(x=event.x_root-root.winfo_x(),y=mause_in_root-vaarr1)
            my_minu_frame.focus()
            def des(event):
                my_minu_frame.destroy()
            my_minu_frame.bind('<FocusOut>',des)

        def Set_Image_Button(label,image_1,image_2,image_3,Size_x2,mycommand=None):
            iiii=['','','','','','']
            iiii[4]=ImageTk.PhotoImage(image_1.resize((Size_x2,Size_x2)))
            label.config(width=Size_x2+2,height=Size_x2-10,image=iiii[4])
            iiii[5]=image_2
            def control_size(size):
                iiii[0]=ImageTk.PhotoImage(iiii[5].resize(size))
                label.config(image=iiii[0])
            lv=[Size_x2-12,True,True,Size_x2]
            def enter(event):
                iiii[1]=ImageTk.PhotoImage(image_2.resize((Size_x2,Size_x2)))
                label.config(image=iiii[1])
                lv[1]=True
                lv[2]=False
                def ent():
                    if lv[0] < Size_x2-8 and  lv[1]:    
                        label.config(height=lv[0]+1)
                        lv[3]+=2
                        lv[0]+=1
                        control_size((lv[3],lv[3]))
                        root.after(30,ent)
                    else:pass
                root.after(30,ent)
            def leave(event):
                lv[1]=False
                lv[2]=True 
                def ent1():
                    if lv[0] > Size_x2-12 and  lv[2]:
                        lv[0]-=1
                        lv[3]-=2
                        label.config(height=lv[0])
                        control_size((lv[3],lv[3]))
                        root.after(30,ent1)
                    else:
                        iiii[2]=ImageTk.PhotoImage(image_1.resize((Size_x2,Size_x2)))   
                        label.config(image=iiii[2])
                ent1()
            def click(event):
                iiii[5]=image_3
                iiii[3]=ImageTk.PhotoImage(iiii[5].resize((lv[3],lv[3])))
                if mycommand:
                    mycommand()
                label.config(image=iiii[3])
                def return_click():
                    iiii[5]=image_2
                    iiii[0]=ImageTk.PhotoImage(image_2.resize((lv[3],lv[3])))
                    label.config(image=iiii[0])
                root.after(150,return_click)
            label.bind('<Enter>',enter)
            label.bind('<Leave>',leave)
            label.bind('<ButtonRelease>',click)

        def Show_Message(show,Text,ask_fonction=None):
            def Round_Frame(object,bg,width,height,highlightbackground=None):
                f_0 =Frame(object,bg=bg,width=width-10,height=1)
                f_1 =Frame(object,bg=bg,width=width-6,height=1)
                f_2 =Frame(object,bg=bg,width=width-4,height=1)
                f_3 =Frame(object,bg=bg,width=width-2,height=1)
                f_4 =Frame(object,bg=bg,width=width-2,height=1)
                f   =Frame(object,bg=bg,width=width,height=height)
                f1_0=Frame(object,bg=bg,width=width-2,height=1)
                f1_1=Frame(object,bg=bg,width=width-2,height=1)
                f1_2=Frame(object,bg=bg,width=width-4,height=1)
                f1_3=Frame(object,bg=bg,width=width-6,height=1)
                f1_4=Frame(object,bg=bg,width=width-10,height=1)
                if highlightbackground:
                    f_0.config(bg=highlightbackground)
                    f1_4.config(bg=highlightbackground)
                    f0_0 =Frame(f,bg=highlightbackground,width=1,height=height).place(x=0,y=0)
                    f0_1 =Frame(f_1,bg=highlightbackground,width=2,height=1).place(x=0,y=0)
                    f0_2 =Frame(f_2,bg=highlightbackground,width=1,height=1).place(x=0,y=0)
                    f0_3 =Frame(f_3,bg=highlightbackground,width=1,height=1).place(x=0,y=0)
                    f0_4 =Frame(f_4,bg=highlightbackground,width=1,height=1).place(x=0,y=0)
                    f0_5 =Frame(f1_0,bg=highlightbackground,width=1,height=1).place(x=0,y=0)
                    f0_6 =Frame(f1_1,bg=highlightbackground,width=1,height=1).place(x=0,y=0)
                    f0_7 =Frame(f1_2,bg=highlightbackground,width=1,height=1).place(x=0,y=0)
                    f0_8 =Frame(f1_3,bg=highlightbackground,width=2,height=1).place(x=0,y=0)
                    f0_10=Frame(f,bg=highlightbackground,width=1,height=height).place(x=width-1,y=0)
                    f0_11=Frame(f_1,bg=highlightbackground,width=2,height=1).place(x=width-8,y=0)
                    f0_12=Frame(f_2,bg=highlightbackground,width=1,height=1).place(x=width-5,y=0)
                    f0_13=Frame(f_3,bg=highlightbackground,width=1,height=1).place(x=width-3,y=0)
                    f0_14=Frame(f_4,bg=highlightbackground,width=1,height=1).place(x=width-3,y=0)
                    f0_15=Frame(f1_0,bg=highlightbackground,width=1,height=1).place(x=width-3,y=0)
                    f0_16=Frame(f1_1,bg=highlightbackground,width=1,height=1).place(x=width-3,y=0)
                    f0_17=Frame(f1_2,bg=highlightbackground,width=1,height=1).place(x=width-5,y=0)
                    f0_18=Frame(f1_3,bg=highlightbackground,width=2,height=1).place(x=width-8,y=0)
                class config:
                    def place(x,y,width=None,height=None):
                        if width:
                            f.place(x=x,y=y,width=width,height=height)
                        else:
                            f.place(x=x,y=y)
                        f_0.place(x=x+5,y=y-5)
                        f_1.place(x=x+3,y=y-4)
                        f_2.place(x=x+2,y=y-3)
                        f_3.place(x=x+1,y=y-2)
                        f_4.place(x=x+1,y=y-1)
                        f1_0.place(x=x+1,y=height+y+0)
                        f1_1.place(x=x+1,y=height+y+1)
                        f1_2.place(x=x+2,y=height+y+2)
                        f1_3.place(x=x+3,y=height+y+3)
                        f1_4.place(x=x+5,y=height+y+4)
                    def bind(bi,fon):
                        f.bind(bi,fon)
                    def frame():
                        return f
                    def destroy():
                        f.destroy()
                        f_0.destroy()
                        f_1.destroy()
                        f_2.destroy()
                        f_3.destroy()
                        f_4.destroy()
                        f1_0.destroy()
                        f1_1.destroy()
                        f1_2.destroy()
                        f1_3.destroy()
                        f1_4.destroy()
                return config
            try:
                Erorr_Frame.destroy()
            except:pass
            Erorr_Frame=Round_Frame(root,Colors[6],300,200,Colors[8])
            varible_x=(root.winfo_width()-300)/2
            varible_y=(root.winfo_height()-200)/2
            Erorr_Frame.place(x=varible_x ,y=varible_y ,width=300,height=200)
            Frametitle=Frame(Erorr_Frame.frame(),bg=Colors[6])
            Frametitle.pack(side=TOP,fill=X,padx=1)
            Label(Frametitle,text=show,bg=Colors[6],fg=Colors[8],font=('tajwal',15,'bold')).pack(side=LEFT,ipadx=2,ipady=5)
            the_list=[]
            vvvvvv=str(Text)
            for title in vvvvvv :
                the_list.append(title)
            if the_list[0] == ' ':
                pass
            else:
                the_list.insert(0,' ')
            global vaa , vaa1 ,the_text
            final_text=[]
            the_text=''
            vaa=40
            vaa1=0
            def get_text():
                while True:
                    global vaa , vaa1 ,the_text
                    if the_list[vaa] == ' ' or  vaa1==vaa : 
                        the_text=''.join(the_list[vaa1+1:vaa+1])
                        if vaa1 == vaa:
                            the_list.insert(vaa+40,' ')
                        else:
                            final_text.append(the_text)
                            final_text.append('\n')
                        vaa1=vaa
                        vaa+=40
                        break
                    else:
                        vaa-=1
            while True:
                if vaa < len(the_list):
                    get_text()
                else:
                    the_text=''.join(the_list[vaa1+1:len(the_list)])
                    final_text.append(the_text)     
                    break
            the_reyllfinal=''.join(final_text[0:])
            def x_command():
                if ask_fonction:
                    ask_fonction('Yes')
                Erorr_Frame.destroy()    
            Label(Erorr_Frame.frame(),text=the_reyllfinal,justify='left',bg=Colors[6],fg=Colors[2]).pack(expand=True)
            Frameb=Frame(Erorr_Frame.frame(),bg=Colors[6])
            Frameb.pack(side=BOTTOM,fill=X,padx=1)
            mes='OK'
            if ask_fonction:
                mes='Yes'
            Ok_Button=Button(Frameb,text=mes,command=x_command,bg=Colors[6],bd=1,fg='red',width=11)
            Ok_Button.pack(side=LEFT,expand=1)
            def entbutton(event):
                Ok_Button.config(bg=Colors[4])
            def levbutton(event):
                Ok_Button.config(bg=Colors[6])
            Ok_Button.bind('<Enter>',entbutton)
            Ok_Button.bind('<Leave>',levbutton)
            if ask_fonction:
                def x_command1():
                    ask_fonction('No')
                    Erorr_Frame.destroy()
                No_Button=Button(Frameb,text='No',command=x_command1,bg=Colors[6],bd=1,fg='red',width=11)
                No_Button.pack(side=LEFT,expand=1)
                def entbutton1(event):
                    No_Button.config(bg=Colors[4])
                def levbutton1(event):
                    No_Button.config(bg=Colors[6])
                No_Button.bind('<Enter>',entbutton1)
                No_Button.bind('<Leave>',levbutton1)
            Erorr_Frame.frame().focus()
            Erorr_Frame.bind('<FocusOut>',lambda e:x_command())

        def White_for_working_onit(where):
            color_w=['red','#ff4646']
            frame=Frame(where,bg=Colors[6],width=30,height=30)
            frame.pack(expand=True)
            def path(the_frame,secondpath):
                frame_x=the_frame.winfo_x()
                frame_y=the_frame.winfo_y()
                the_frame.config(bg=color_w[0])
                if frame_x == 0 and frame_y== 0:
                    parametr=[1,1]
                    def roturn_path():
                        try:
                            if parametr[0] != 1:
                                parametr[0]-=1
                                the_frame.config(width=10+parametr[0])
                                parametr[1]+=1
                                the_frame.place(x=parametr[1],y=0)
                                root.after(10,roturn_path)
                        except:pass
                    def move_in_path():
                        try:
                            if parametr[0] != 20:
                                the_frame.config(width=20+parametr[0])
                                parametr[0]+=1
                                root.after(10,move_in_path)
                            else:
                                the_frame.config(bg=color_w[1])
                                roturn_path()
                                secondpath()
                        except:pass        
                    move_in_path()
                if frame_x ==20 and frame_y== 0:
                    parametr=[1,1]
                    def roturn_path():
                        try:
                            if parametr[0] != 1:
                                parametr[0]-=1
                                the_frame.config(height=10+parametr[0])
                                parametr[1]+=1
                                the_frame.place(x=20,y=parametr[1])
                                root.after(10,roturn_path) 
                        except:pass           
                    def move_in_path():
                        try:
                            if parametr[0] != 20:
                                the_frame.config(height=20+parametr[0])
                                parametr[0]+=1
                                root.after(10,move_in_path)
                            else:
                                the_frame.config(bg=color_w[1])
                                roturn_path()
                                secondpath()
                        except:pass 
                    move_in_path()
                if frame_x ==20 and frame_y==20:
                    parametr=[1,19]
                    def roturn_path():
                        try:
                            if parametr[0] != 1:
                                parametr[0]-=1
                                the_frame.config(width=10+parametr[0]) 
                                root.after(10,roturn_path) 
                        except:pass    
                    def move_in_path():
                        try:
                            if parametr[0] != 20:
                                the_frame.config(width=20+parametr[0])
                                parametr[0]+=1
                                parametr[1]-=1
                                the_frame.place(x=parametr[1],y=20)
                                root.after(10,move_in_path)
                            else:
                                the_frame.config(bg=color_w[1])
                                roturn_path()
                                secondpath()
                        except:pass
                    move_in_path()
                if frame_x == 0 and frame_y==20:
                    parametr=[1,19]
                    def roturn_path():
                        try:
                            if parametr[0] != 1:
                                parametr[0]-=1
                                the_frame.config(height=10+parametr[0])                
                                root.after(10,roturn_path)
                        except:pass
                    def move_in_path():
                        try:
                            if parametr[0] != 20:
                                the_frame.config(height=20+parametr[0])
                                parametr[0]+=1
                                parametr[1]-=1
                                the_frame.place(x=0,y=parametr[1])
                                root.after(10,move_in_path)
                            else:
                                the_frame.config(bg=color_w[1])
                                roturn_path()
                                secondpath()
                        except:pass
                    move_in_path()
            fr1=Frame(frame,bg=color_w[1],width=10,height=10)
            fr1.place(x=0,y=0)
            fr2=Frame(frame,bg=color_w[1],width=10,height=10)
            fr2.place(x=0,y=20)
            fr3=Frame(frame,bg=color_w[1],width=10,height=10)
            fr3.place(x=20,y=20)
            def path_3():
                path(fr3,path_1)
            def path_2():
                path(fr2,path_3)
            def path_1():
                path(fr1,path_2)
            path_1()

        def Entry_round(where,message,thevariable,bg,ifpassword=None,fg=None):
            lab=Label(where,bg=bg,fg='#5b5b5b',image=My_Widget.enter_image)
            Ent=Entry(where,
                            bd=0,
                            bg='white',
                            width=25,
                            justify='center',
                            font=('Microsoft YaHei UI Light',11,'bold'),
                            textvariable=thevariable)
            Ent.config(fg='#969696')
            if fg:
                Ent.config(fg=fg)
            Ent.insert(0,message)
            def focusin_Entry(showent=None):
                lab.config(image=My_Widget.enter_image_fucos)
                vva1=Ent.get()
                if vva1 == message:
                    Ent.delete(0,END)
                    Ent.config(fg='black')
                if showent:
                    Ent.config(show=showent)
            def focusout_Entry():
                lab.config(image=My_Widget.enter_image)
                vva12=Ent.get()
                if vva12 == '':
                    Ent.config(show='')
                    Ent.config(fg='#969696')
                    Ent.insert(0,message)
            if ifpassword:
                Ent.bind('<FocusIn>',lambda e:focusin_Entry('*'))
                Ent.bind('<FocusOut>',lambda e:focusout_Entry())
            else:
                Ent.bind('<FocusIn>',lambda e:focusin_Entry())
                Ent.bind('<FocusOut>',lambda e:focusout_Entry())
            class config:
                def place(x,y):
                    lab.place(x=x,y=y)
                    Ent.place(x=x+12,y=y+4)
                def config(bg=None,fg=None):
                    if bg:
                        lab.config(bg=bg)
                    if fg:
                        Ent.config(fg=fg)

                def winfo_width():
                    return lab.winfo_width()
                def winfo_height():
                    return lab.winfo_height()
            return config

        def Combobox_round(where,message,thevariable,bg,values=None):


            sitngs=['white',True,'',True,values]
            lab=Label(where,bg=bg,fg='#5b5b5b',image=My_Widget.enter_image)
            lab1=Label(where,bg='white',image=My_Widget.flash_down)
            Ent=Entry(where,
                                    bd=0,
                                    bg=sitngs[0],
                                    fg='#969696',
                                    width=24,
                                    justify='center',
                                    font=('Microsoft YaHei UI Light',11,'bold'),
                                    textvariable=thevariable)
            Ent.insert(0,message)
            def focusin_Entry():
                lab.config(image=My_Widget.enter_image_fucos)
                vva1=Ent.get()
                if vva1 == message:
                    Ent.delete(0,END)
                    Ent.config(fg='black')
                else:
                    Ent.config(fg='black')
            def focusout_Entry():
                lab.config(image=My_Widget.enter_image)
                vva12=Ent.get()
                if vva12 == '':
                    Ent.config(fg='#969696')
                    Ent.insert(0,message)
            def enter_flash(event):
                if sitngs[3]:
                    lab1.config(image=My_Widget.flash_up)
            def leave_flash(event):
                if sitngs[3]:
                    lab1.config(image=My_Widget.flash_down)
            def click_flash(event):
                if sitngs[1]:
                    lab1.config(image=My_Widget.flash_up_active)
                    sitngs[3]=False
                    chose()
                else:
                    sitngs[1]=True
                    sitngs[3]=True
                    sitngs[2].destroy()
                    lab1.config(image=My_Widget.flash_down)
            def chose():
                sitngs[1]=False
                frx=Scrolled_Frame(  master=where,
                                    bg='white',
                                    scroll_vertical=True,
                                    highlightbackground='#4e82fa',
                                    highlightcolor='#4e82fa',
                                    highlightthickness=1,
                                    scroll_unit=21)
                frx.place(x=lab.winfo_x()+5,y=lab.winfo_y()+30,width=lab.winfo_width()-10,height=86)
                sitngs[2]=frx
                
                frx.focus()
                def out(event):
                    sitngs[1]=True
                    sitngs[3]=True
                    frx.destroy()
                    lab1.config(image=My_Widget.flash_down)
                frx.bind('<FocusOut>',out)
                
                def button(row):
                    var=Label(frx,text=row,bg='white',justify='center')
                    var.pack(fill=X)
                    def enter(event):
                        var.config(bg='#ffb0b7')
                    def leave(event):
                        var.config(bg='white')
                    def click_chose(event):
                        Ent.focus()
                        Ent.delete(0,END)
                        Ent.insert(0,row)
                    var.bind('<Enter>',enter)
                    var.bind('<Leave>',leave)
                    var.bind('<ButtonRelease-1>',click_chose)
                try:
                    vs=sitngs[4]
                    for row in vs:
                        button(row)
                except:pass

            Ent.bind('<FocusIn>',lambda e:focusin_Entry())
            Ent.bind('<FocusOut>',lambda e:focusout_Entry())
            lab1.bind('<Enter>',enter_flash)
            lab1.bind('<Leave>',leave_flash)
            lab1.bind('<ButtonRelease-1>',click_flash)
            class config:
                def place(x,y):
                    lab.place(x=x,y=y)
                    Ent.place(x=x+12,y=y+4)
                    lab1.place(x=x+232,y=y+10)
                def config(bg=None,values=None):
                    if bg:
                        lab.config(bg=bg)
                    if values:
                        sitngs[4]=values
                def winfo_width():
                    return lab.winfo_width()
                def winfo_height():
                    return lab.winfo_height()
            return config

        def Button_Image(where,button_image,button_image_enter,button_image_click,bg,command=None):
            lab5=Label(where,image=button_image ,bg=bg)
            Varinw=[True]
            my_command=command
            def enter_buttonconnect(event):
                Varinw[0]=True
                lab5.config(image=button_image_enter)
            def leave_buttonconnect(event):
                Varinw[0]=False
                lab5.config(image=button_image)
            def click_buttonconnect(event):
                lab5.config(image=button_image_click)
                if my_command:
                    my_command()
                def return_connect_click():
                    try:   
                        if Varinw[0]:
                            lab5.config(image=button_image_enter)
                        else:
                            lab5.config(image=button_image)
                    except:pass
                root.after(200,return_connect_click)
            lab5.bind('<Enter>',enter_buttonconnect)
            lab5.bind('<Leave>',leave_buttonconnect)
            lab5.bind('<ButtonRelease-1>',click_buttonconnect)
            class config:
                def place(x,y):
                    lab5.place(x=x,y=y)
                def config(bg=None,command=None):
                    if bg:
                        lab5.config(bg=bg)
                def winfo_width():
                    return lab5.winfo_width()
                def winfo_height():
                    return lab5.winfo_height()
            return config

        def Resize_Widget(home_frame,my_entry,dfr_x,dfr_y,size=None):
            if size :
                x_win = home_frame.winfo_width() - size[0]
                y_win = home_frame.winfo_height()- size[1]
            else:
                x_win = home_frame.winfo_width() - my_entry.winfo_width()
                y_win = home_frame.winfo_height()- my_entry.winfo_height()
            differencex=(x_win /2) +dfr_x
            differencey=(y_win /2) +dfr_y
            my_entry.place(x=differencex,y=differencey)

    title_bar = Frame(root, 
                    bg=Colors[1], 
                    bd=0,
                    highlightthickness=0)
    close_button = Button(title_bar, 
                    text='〤',
                    font=('Microsoft YaHei UI Light',9), 
                    command=root.destroy,
                    bg=Colors[1],
                    fg=Colors[2],
                    bd=0,)
    close_button.pack(side=RIGHT,ipadx=10,ipady=0)
    expand_button = Button(title_bar, 
                    text='1',
                    font=('Webdings',8), 
                    command=maximize_me,
                    fg=Colors[2],
                    bg=Colors[1],
                    bd=0,)
    expand_button.pack(side=RIGHT,ipadx=12,ipady=0)
    minimize_button = Button(title_bar, 
                    text='-',
                    font=('Microsoft YaHei UI Light',9,'bold'),
                    command=minimize_me,
                    bg=Colors[1],
                    fg=Colors[2],
                    bd=0,)
    minimize_button.pack(side=RIGHT,ipadx=14,ipady=0)
    global iimage1
    iimage1=PhotoImage(file='images\\Untitled-1111.png')
    title_bar_title = Label(title_bar, 
                    image=iimage1,
                    bd=0, 
                    bg=Colors[1],)
    title_bar_title.pack(side=LEFT, padx=5)

    def open_db():
        closeframe1()
        ask_open_db_file()
    def Open_folder():
        closeframe1()
        ask_open_db_folder()

    def New_DB():
        try:
            Create_DB()
        except:pass

    def New_db_server():
        try:
            if Host_Name.get()=='':
                My_Widget.Show_Message('Error','plasse connect server ferst !')
            else:
                Frame_of_Create_Database()
        except:
            My_Widget.Show_Message('Error','plasse connect server ferst !')

    def exit():
        root.destroy()

    menu_1=My_Widget.Menu_Bar(title_bar,'File',
                        ['New database server',
                        'tear','New db file',
                        'Open db file','Open Folder',
                        'tear','Exit'],
                        [New_db_server,None,New_DB,open_db,Open_folder,None,exit])
    menu_2=My_Widget.Menu_Bar(title_bar,
                        'Edit',
                        ['Meak_Theme'],
                        [Meak_Theme])
    menu_3=My_Widget.Menu_Bar(title_bar,'Themes')
    menu_4=My_Widget.Menu_Bar(title_bar,
                        'Help',
                        ['About us','Help'],
                        [None,None])
    
    def pick_themes_on_menu():
        parser=ConfigParser()
        parser.read('files\\Themes.txt')
        themes=parser.sections()
        themes.remove('Defualt')
        commands=[]
        for row in themes:
            commands.append(Theme)
        menu_3.values_commands(themes,commands,return_name=True)
    pick_themes_on_menu()
    title_frame=Frame(title_bar,bg=Colors[1])
    title_frame.pack(side=LEFT,expand=True)
    title_bar_title1 = Label(title_frame, 
                    text='DatabaseControl  ',
                    bd=0, 
                    bg=Colors[1],
                    fg=Colors[2])
    title_bar_title1.pack(side=LEFT)
    
    def get_posetion(event):
        xwin = root.winfo_x()
        ywin = root.winfo_y()
        startx = event.x_root
        starty = event.y_root
        ywin = ywin - starty
        xwin = xwin - startx
        if root.maximized == True:
            normal=root.normal_size
            geometry=''
            width=''
            v=True
            v1=True
            for row in normal:
                if row == '+':
                    v=False
                if v:
                    geometry+=row
            for i in normal:
                if i =='x':
                    v1=False
                if v1:
                    width+=i
            x=int(int(width)*(startx/root.winfo_screenwidth()))
            xwin = -x
            root.geometry(f'{geometry}+{event.x_root-x}+{event.y_root+ywin}')
            expand_button.config(text="1")
            root.maximized = not root.maximized
            root.after(50,move_widget)
        def move_window(event): 
            root.config(cursor="fleur")
            root.geometry(f'+{event.x_root+xwin}+{event.y_root+ywin}')
        def release_window(event): 
            root.config(cursor="arrow") 
        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)
    title_bar.bind('<Button-1>', get_posetion)
    title_bar_title.bind('<Button-1>', get_posetion) 

    close_button.bind('<Enter>',lambda e:close_button.config(bg='red'))
    close_button.bind('<Leave>',lambda e:close_button.config(bg=Colors[1]))
    expand_button.bind('<Enter>',lambda e:expand_button.config(bg=Colors[0]))
    expand_button.bind('<Leave>',lambda e:expand_button.config(bg=Colors[1]))
    minimize_button.bind('<Enter>',lambda e:minimize_button.config(bg=Colors[0]))
    minimize_button.bind('<Leave>',lambda e:minimize_button.config(bg=Colors[1]))

    resizex_widget = Frame(root,bg=Colors[1],width=2,cursor='sb_h_double_arrow')
    def resizex(event):
        root_width=root.winfo_width()
        difference = (event.x_root - root.winfo_x()) - root_width 
        width=root_width+difference
        if width >= 600 :
            root.geometry(f"{width}x{root.winfo_height()}")
            move_widget()
        else:
            root.geometry(f"{600}x{root.winfo_height()}")
            move_widget()             
    resizex_widget.bind("<B1-Motion>",resizex)   
    resizey_widget = Frame(root,bg=Colors[1],height=2,cursor='sb_v_double_arrow')
    def resizey(event):
        root_height=root.winfo_height()
        difference = (event.y_root - root.winfo_y()) - root_height
        height=root_height+difference
        if height >= 400:
            root.geometry(f"{root.winfo_width()}x{height}")
            move_widget()
        else:
            root.geometry(f"{root.winfo_width()}x{400}")
            move_widget()
    resizey_widget.bind("<B1-Motion>",resizey)
    Frame_1=Frame(root,bg=Colors[6])
    Fra=Frame(root,bg=Colors[9])
    
    Frame_2=Frame(root,bg=Colors[6])
    Frame_3=Frame(root,bg=Colors[6])
    Frame_4=Frame(root,bg=Colors[6])
    Frame_1.bind('<ButtonRelease-1>',lambda e:Frame_1.focus())
    Frame_2.bind('<ButtonRelease-1>',lambda e:Frame_2.focus())
    Frame_3.bind('<ButtonRelease-1>',lambda e:Frame_3.focus())
    Frame_4.bind('<ButtonRelease-1>',lambda e:Frame_4.focus())
    
    st=ttk.Style()
    st.theme_use('default')
    st.configure('Treeview',
                background=Colors[6],
                fieldbackground=Colors[6],
                borderwidth=0,
                borderradius=0,
                foreground=Colors[2])
    st.configure('Treeview.Heading',
                background=Colors[6],
                foreground=Colors[7],
                relief=FLAT,
                font=('tajwal',9,'bold'))
    st.map('Treeview',background=[('selected',Colors[0])],foreground=[('selected',Colors[2])])
    st.map('Treeview.Heading',background=[('active',Colors[0])])



    global check_for_move_focus_button
    check_for_move_focus_button=False

    def closeframe():
        global check_for_move_focus_button
        check_for_move_focus_button=False
        vf=Host_Name.get()
        move_click_frame.place(x=0,y=5)
        try:
            Frame_3.pack_forget()
        except:pass
        try:
            Frame_4.pack_forget()
        except:pass
        Frame_2.pack(side=LEFT,fill=BOTH,expand=True)
        Frame_2.focus()
    
    def closeframe1():
        global check_for_move_focus_button
        check_for_move_focus_button=False
        move_click_frame.place(x=0,y=60)
        try:
            Frame_2.pack_forget()
        except:pass
        try:
            Frame_4.pack_forget()
        except:pass
        Frame_3.pack(side=LEFT,fill=BOTH,expand=True)
        Frame_3.focus()
        
    def closeframe2():
        global check_for_move_focus_button
        check_for_move_focus_button=True
        vw=Frame_1.winfo_height()
        move_click_frame.place(x=0,y=vw-45)
        try:
            Frame_2.pack_forget()
        except:pass
        try:
            Frame_3.pack_forget()
        except:pass
        Frame_4.pack(side=LEFT,fill=BOTH,expand=True)
        Frame_4.focus()
        
    def move_button_focus():
        global check_for_move_focus_button
        if check_for_move_focus_button:
            vava=l2.winfo_y()
            move_click_frame.place(x=0,y=vava-5)

    Frame_focus_click=Frame(Frame_1,width=2,bg=Colors[6])
    Frame_focus_click.pack(side=LEFT,fill=Y,expand=True)
    move_click_frame=Frame(Frame_focus_click,bg='blue',width=2,height=40)
    move_click_frame.place(x=0,y=5)
    image2=Image.open('images\\tttt1.png')
    image1=Image.open('images\\tttt2.png')
    image3=Image.open('images\\tttt3.png')
    image5=Image.open('images\\siting_color1.png')
    image4=Image.open('images\\siting_color2.png')
    image6=Image.open('images\\siting_color3.png')
    image7=Image.open('images\\db1.png')
    image8=Image.open('images\\db.png')
    image9=Image.open('images\\db2.png')
    l1=Label(Frame_1,bg=Colors[6])
    l1.pack(pady=10)
    l2=Label(Frame_1,bg=Colors[6])
    l2.pack(side=BOTTOM,pady=10)
    l3=Label(Frame_1,bg=Colors[6])
    l3.pack(pady=10)

    My_Widget.Set_Image_Button(l1,image1,image2,image3,40,closeframe)
    My_Widget.Set_Image_Button(l2,image4,image5,image6,40,closeframe2)
    My_Widget.Set_Image_Button(l3,image7,image8,image9,42,closeframe1)

    def get_images():
        global search_png, update_png, add_png, change_png, drop_png, create, quit_png
        global text_png, The_Focus_value1, close_folder, open_folder
        global chevron_r, chevron_r_a, chevron_d, chevron_d_a, x_inw


        search_png  =icon_to_image("search-inw", fill=Colors[7],scale_to_width=20)
        add_png     =icon_to_image("add-inw", fill=Colors[7],scale_to_width=18)
        change_png  =icon_to_image("flash2-inw", fill=Colors[7],scale_to_width=18)
        update_png  =icon_to_image("flash1-inw", fill=Colors[7],scale_to_width=18)
        create      =icon_to_image("create-pen-inw", fill=Colors[7],scale_to_width=18)
        quit_png    =icon_to_image("power-off-inw", fill='red',scale_to_width=18)
        text_png    =icon_to_image("text-inw", fill=Colors[7],scale_to_width=15)
        drop_png    =icon_to_image("delete-inw", fill=Colors[7],scale_to_width=16)
        close_folder=icon_to_image("folder-inw", fill=Colors[7],scale_to_width=14)
        open_folder =icon_to_image("folder-open-inw", fill=Colors[7],scale_to_width=16)
    
        chevron_r  = icon_to_image("chevron-right", fill=Colors[2], scale_to_width=6)
        chevron_r_a= icon_to_image("chevron-right", fill=Colors[7], scale_to_width=6)
        chevron_d  = icon_to_image("chevron-down", fill=Colors[2],scale_to_width=10)
        chevron_d_a= icon_to_image("chevron-down", fill=Colors[7],scale_to_width=10)
        x_inw      = icon_to_image("x-inw", fill=Colors[2], scale_to_width=6)

    get_images()
    
    global The_Focus_value
    The_Focus_value=StringVar()
    The_Focus_value1=[]
    
    Host_Name=StringVar()
    User_Name=StringVar()
    User_Password=StringVar()    
    
    def Home_Page():
        try:
            for widget in Frame_2.winfo_children():
                widget.destroy()
        except:pass
        global fr_connect
        try:
            fr_connect.destroy()
        except:pass
        Host_Name.set('')
        User_Name.set('')
        User_Password.set('')

        Frame_one=Frame(Frame_2,bg=Colors[6])
        Frame_one.pack(fill='both',expand=True)

        global image111
        image111=PhotoImage(file='images\\12345.png')
        global er0 , er1 , er2

        er0=Round_Entry(    Frame_one,
                            text='Server Name',
                            bg=Colors[0],
                            fg=Colors[2],
                            outline=Colors[9],
                            outline_focus=Colors[7],
                            font=('Candara',14),
                            justify='center',
                            width=25)
        er1=Round_Entry(    Frame_one,
                            text='User',
                            bg=Colors[0],
                            fg=Colors[2],
                            outline=Colors[9],
                            outline_focus=Colors[7],
                            font=('Candara',14),
                            justify='center',
                            width=25)
        er2=Round_Entry(    Frame_one,
                            text='Password',
                            password=True,
                            bg=Colors[0],
                            fg=Colors[2],
                            outline=Colors[9],
                            outline_focus=Colors[7],
                            font=('Candara',14),
                            justify='center',
                            width=25)
        b_c=Round_Button(   master=Frame_one,
                            fg=Colors[2],
                            width=250,
                            bd=1,
                            text='Connect',
                            font=('Candara',14),
                            outline=Colors[7],
                            bg_active=Colors[0],
                            command=lambda:DB_connect(True),
                            ipadx=4,
                            ipady=4)
        lab_i=Label(Frame_one,image=image111 ,bg=Colors[6])

        er0.place(x=-300,y=30)
        er1.place(x=-300,y=30)
        er2.place(x=-300,y=30)
        b_c.place(x=-300,y=30)
        lab_i.place(x=-300,y=30)
        
        global resize_entrys
        def resize_entrys():
            My_Widget.Resize_Widget(Frame_2,er0,100,-70)
            My_Widget.Resize_Widget(Frame_2,er1,100,-25)
            My_Widget.Resize_Widget(Frame_2,er2,100,20)
            My_Widget.Resize_Widget(Frame_2,b_c,100,70)
            My_Widget.Resize_Widget(Frame_2,lab_i,-160,0)
        def Change_Colors1(colors):
            Frame_one.config(bg=colors[6])
            lab_i.config(bg=colors[6])
            er0.config(bg=colors[0],fg=colors[2],outline=colors[9],outline_focus=colors[7])
            er1.config(bg=colors[0],fg=colors[2],outline=colors[9],outline_focus=colors[7])
            er2.config(bg=colors[0],fg=colors[2],outline=colors[9],outline_focus=colors[7])
            b_c.config(bg=colors[0],fg=colors[2],outline=colors[7],bg_active=colors[0])
        Container_Configer_Color[1]=Change_Colors1

    def DB_Page():
        for widget in Frame_3.winfo_children():
            widget.destroy()
        DB_Frame=Scrolled_Frame(Frame_3,
                                    bg=Colors[6],
                                    scroll_button_bg=Colors[9],
                                    scroll_button_active=Colors[8],
                                    scroll_vertical=True,
                                    scroll_horizontal=True,
                                    scroll_unit=25,
                                    width=200)
        DB_Frame.pack(side=LEFT,fill=Y)
        Frame1=Frame(Frame_3,bg=Colors[6])
        Frame1.pack(side=BOTTOM,fill=X)
        TV_Frame2=Frame(Frame_3,
                        bg=Colors[6],
                        highlightthicknes=1,
                        highlightbackground=Colors[9],
                        highlightcolor=Colors[9])
        TV_Frame2.pack(side=RIGHT,fill=BOTH,expand=1)
        scrol_ver=Scroll(TV_Frame2,
                                orient='vertical',
                                button_bg=Colors[9],
                                button_bg_active=Colors[8])
        scrol_ver.pack(side='right',fill='y')
        scrol_hor=Scroll(TV_Frame2,
                                orient='horizontal',
                                button_bg=Colors[9],
                                button_bg_active=Colors[8])
        scrol_hor.pack(side='bottom',fill='x')
        TV_Frame3=Frame(TV_Frame2,bg=Colors[6])
        TV_Frame3.pack(side=RIGHT,fill=BOTH,expand=1)    
        Frame_open=Frame(DB_Frame,bg=Colors[6])
        Frame_open.pack(fill=X,pady=4)
        laab1=Label(Frame_open,
                    text='OPEN DATABASE',
                    fg=Colors[2],
                    bg=Colors[6],
                    font=('Century Schoolbook',10,'bold italic'))
        laab1.pack(side=LEFT)
        laab=Label(Frame_open,
                    text='          +',
                    fg=Colors[2],
                    bg=Colors[6],
                    font=('Century Schoolbook',12,'bold'))
        laab.pack(side=LEFT)
        laab.bind('<Enter>',lambda e: laab.config(fg=Colors[7]))
        laab.bind('<Leave>',lambda e: laab.config(fg=Colors[2]))
        laab.bind('<Button-1>',lambda e:ask_open_db_file())
        files_frame=Frame(DB_Frame,bg=Colors[6])
        files_frame.pack(fill=X,pady=4)
        Frame_open1=Frame(DB_Frame,bg=Colors[6])
        Frame_open1.pack(fill=X,pady=4)
        laab2=Label(Frame_open1,
                    text='OPEN FOLDERS',
                    fg=Colors[2],
                    bg=Colors[6],
                    font=('Century Schoolbook',10,'bold italic'))
        laab2.pack(side=LEFT)
        laab3=Label(Frame_open1,
                    text='            +',
                    fg=Colors[2],
                    bg=Colors[6],
                    font=('Century Schoolbook',12,'bold'))
        laab3.pack(side=LEFT)
        folders_frame=Frame(DB_Frame,bg=Colors[6])
        folders_frame.pack(fill=X,pady=4)
        laab3.bind('<Enter>',lambda e: laab3.config(fg=Colors[7]))
        laab3.bind('<Leave>',lambda e: laab3.config(fg=Colors[2]))
        laab3.bind('<Button-1>',lambda e:ask_open_db_folder())

        But_1 = Round_Button(   master=Frame1,
                                image=add_png,
                                fg=Colors[2],
                                width=100,
                                text='   Add R ',
                                font=('tajwal',13),
                                outline=Colors[0],
                                bg_active=Colors[0],
                                ipadx=2,
                                ipady=2)
        But_1.pack(side='left',expand=True,pady=1)
        But_2 = Round_Button(   master=Frame1,
                                image=update_png,
                                fg=Colors[2],
                                width=100,
                                text=' Update R',
                                font=('tajwal',13),
                                outline=Colors[0],
                                bg_active=Colors[0],
                                ipadx=2,
                                ipady=2)
        But_2.pack(side='left',expand=True,pady=1)
        But_3 = Round_Button(   master=Frame1,
                                image=drop_png,
                                fg=Colors[2],
                                width=100,
                                text=' Delete R',
                                font=('tajwal',13),
                                outline=Colors[0],
                                bg_active=Colors[0],
                                ipadx=2,
                                ipady=2)
        But_3.pack(side='left',expand=True,pady=1)
        But_4 = Round_Button(   master=Frame1,
                                image=search_png,
                                fg=Colors[2],
                                width=100,
                                text='  Search  ',
                                font=('tajwal',13),
                                outline=Colors[0],
                                bg_active=Colors[0],
                                ipadx=2,
                                ipady=2)
        But_4.pack(side='left',expand=True,pady=1)
        But_5 = Round_Button(   master=Frame1,
                                image=add_png,
                                fg=Colors[2],
                                width=100,
                                text='  Add C  ',
                                font=('tajwal',13),
                                outline=Colors[0],
                                bg_active=Colors[0],
                                ipadx=2,
                                ipady=2)
        But_5.pack(side='left',expand=True,pady=1)
        But_6 = Round_Button(   master=Frame1,
                                image=change_png,
                                fg=Colors[2],
                                width=100,
                                text='Rename C',
                                font=('tajwal',13),
                                outline=Colors[0],
                                bg_active=Colors[0],
                                ipadx=2,
                                ipady=2)
        But_6.pack(side='left',expand=True,pady=1)
        But_7 = Round_Button(   master=Frame1,
                                image=drop_png,
                                fg=Colors[2],
                                width=100,
                                text=' Delete C',
                                font=('tajwal',13),
                                outline=Colors[0],
                                bg_active=Colors[0],
                                ipadx=2,
                                ipady=2)
        But_7.pack(side='left',expand=True,pady=1)

        global table_opend
        table_opend=''
        
        parser=ConfigParser()
        parser.read('files\\Opne_last_folder.txt')

        def show_table(table=None):
            columns=[]
            global table_opend
            table_opend=''
            if table:
                columns=table.Columns()[0]
                data=table.List_Requst()
                table_opend=table.Name()
            try:
                for i in TV_Frame3.winfo_children():
                    i.destroy()
            except:pass
            TV_Frame3.focus()
            

            TV1=ttk.Treeview(TV_Frame3,columns=(columns))
            TV1.pack(side=LEFT,fill=BOTH,expand=True)

            scrol_ver.configure(command=TV1.yview)
            TV1.configure(yscrollcommand=scrol_ver.set)
            scrol_hor.configure(command=TV1.xview)
            TV1.configure(xscrollcommand=scrol_hor.set)

            def Treeview_Menu2(event):
                global The_Focus_v
                row_id=TV1.identify_row(event.y)
                TV1.selection_set(row_id)
                row_values=TV1.item(row_id)
                tt=[row_values['text']]
                va=row_values['values']
                try:
                    v=tt+va
                    v.pop()
                except:
                    v=tt
                The_Focus_v=v
                My_Widget.My_Menu(event,
                                values=['Save','Refresh',
                                        'Add','Update',
                                        'Delete','tear',
                                        'Add Column','Rename Column',
                                        'Delete Column','Search'],
                                commands=[  lambda:table.Commit(),
                                            lambda:show_table(table),
                                            lambda:Add_Row(table),
                                            lambda:Update_Row(table),
                                            lambda:Delete_row(table),
                                            None,
                                            lambda:Add_Column(table),
                                            lambda:Rename_Column(table),
                                            lambda:Delete_Column(table),
                                            lambda:Search(table)])

            TV1.bind('<Button-3>',Treeview_Menu2)
            global The_Focus_v
            The_Focus_v=[]
            def Get_Cursor(event):
                global The_Focus_v
                try:
                    cursor_row=TV1.focus() 
                    contents=TV1.item(cursor_row)
                    tt=[contents['text']]
                    rr=tt+(contents['values'])
                    rr.pop()
                    The_Focus_v=rr
                except:pass
            TV1.bind('<ButtonRelease-1>',Get_Cursor)
            if table:
                for row in range(len(columns)):
                    TV1.heading(f'#{row}',text=columns[row])
                    TV1.column(f'#{row}',width=100)   
                count=0
                for row in data:
                    try:
                        TV1.insert('','end',count,text=row[0])
                        for i in range(1,len(row)):
                            TV1.set(count,f'#{i}',row[i])
                        count+=1
                    except:
                        TV1.insert('','end',count,text='')
                        for i in range(1,len(row)):
                            TV1.set(count,f'#{i}',row[i])
                        count+=1
        show_table()

        def get_path_database(path):
            name_list=[]
            v=True
            for row in range(1,len(path)):
                if path[-row] !='/' and path[-row] != '\\' and v:
                    name_list.append(path[-row])
                else:
                    v=False
            name_list.reverse()
            name=''.join(name_list)
            return name          

        def File_Button(place,text,command,tables=None,command_close=None):
            frame=Frame(place,bg=Colors[6])
            fr=Frame(frame,bg=Colors[6])
            fr.pack(fill=X)
            l1=Label(fr,image=chevron_r,width=10,bg=Colors[6],fg=Colors[2])
            l1.pack(side=LEFT)
            l2=Label(fr,text=text,font=('tajwal',9),anchor=NW,bg=Colors[6],fg=Colors[2],width=22)
            l2.pack(side=LEFT)
            l3=Label(fr,text='x',font=('Consolas',9),bg=Colors[6],fg=Colors[2])
            l3.pack(side=LEFT,ipadx=4)
            container_=[]
            
            def set_tables(tb=None,pack=None):
                try:
                    for i in container_:
                        i.destroy()
                    container_.clear()
                except:
                    container_.clear()
                if tb:
                    for i in tb:
                        def lab():
                            text=i
                            def comand():
                                command(text,'Open Table')
                            l=Frame(frame,bg=Colors[6])
                            l0=Label(l,text='      ',bg=Colors[6])
                            l0.pack(side=LEFT,ipadx=2)
                            def delete_tt(anser):
                                if anser=='Yes':
                                    command(text,'Drop Table')

                            def command_x():
                                My_Widget.Show_Message('Ask',f'do you want to delete {text} table ?',delete_tt)
                            l1=Label(l,text='x',
                                    font=('Consolas',9),
                                    bg=Colors[6],
                                    fg=Colors[2],
                                    anchor=NW)
                            l1.pack(side=LEFT)
                            l2=Label(l,text=f'{text}',
                                    font=('Consolas',9),
                                    bg=Colors[6],
                                    fg=Colors[2],
                                    anchor=NW)
                            l2.pack(side=LEFT,fill=X)
                            def enter():
                                l.config(bg=Colors[0])
                                l0.config(bg=Colors[0])
                                l1.config(bg=Colors[0])
                                l2.config(bg=Colors[0])
                            def leave():
                                l.config(bg=Colors[6])
                                l0.config(bg=Colors[6])
                                l1.config(bg=Colors[6])
                                l2.config(bg=Colors[6])
                            l1.bind('<Enter>',lambda e:l1.config(fg=Colors[7]))
                            l1.bind('<Leave>',lambda e:l1.config(fg=Colors[2]))
                            l.bind('<Enter>',lambda e:enter())
                            l.bind('<Leave>',lambda e:leave())
                            l.bind('<Button-1>', lambda e:comand())
                            l2.bind('<Button-1>', lambda e:comand())
                            l0.bind('<Button-1>', lambda e:comand())
                            l1.bind('<Button-1>', lambda e:command_x())
                            class config:
                                def pack(fill=None):
                                    l.pack(fill=fill)
                                def pack_forget():
                                    l.pack_forget()
                                def destroy():
                                    l.destroy()

                            return config
                        l=lab()
                        container_.append(l)

                def lab():
                    def comand():
                        command('','Add Table')
                    lx=Label(frame,text='    +',
                            font=('Consolas',10),
                            bg=Colors[6],
                            fg=Colors[2],
                            anchor=NW)
                    lx.bind('<Enter>',lambda e:lx.config(bg=Colors[0]))
                    lx.bind('<Leave>',lambda e:lx.config(bg=Colors[6]))
                    lx.bind('<Button-1>', lambda e:comand())
                    class config:
                        def pack(fill=None):
                            lx.pack(fill=fill)
                        def pack_forget():
                            lx.pack_forget()
                        def destroy():
                            lx.destroy()
                    return config
                lx=lab()
                container_.append(lx)
                if pack:
                    for i in container_:
                        i.pack(fill=X)
            set_tables(tables)

            var_rr=[True]
            def open_tables():
                frame.focus()
                if var_rr[0]:
                    var_rr[0]=False
                    l1.config(image=chevron_d)
                    for i in container_:
                        i.pack(fill=X)
                else:
                    var_rr[0]=True
                    l1.config(image=chevron_r)
                    for i in container_:
                        i.pack_forget()
            def on_frame():
                fr.config(bg=Colors[0])
                l1.config(bg=Colors[0])
                l2.config(bg=Colors[0])
                l3.config(bg=Colors[0])
            def out_frame():
                fr.config(bg=Colors[6])
                l1.config(bg=Colors[6])
                l2.config(bg=Colors[6])
                l3.config(bg=Colors[6])
            def close_database():
                frame.focus()
                if command_close:
                    command_close()
                frame.destroy()
            def ent():
                if var_rr[0]:
                   l1.config(image=chevron_r_a)
                else:
                    l1.config(image=chevron_d_a) 
            def lev():
                if var_rr[0]:
                   l1.config(image=chevron_r)
                else:
                    l1.config(image=chevron_d)

            fr.bind('<Enter>',lambda e:on_frame())
            fr.bind('<Leave>',lambda e:out_frame())
            l1.bind('<Enter>',lambda e:ent())
            l1.bind('<Leave>',lambda e:lev())
            l1.bind('<Button-1>', lambda e: open_tables())
            l2.bind('<Button-1>', lambda e: open_tables())
            l3.bind('<Enter>',lambda e:l3.config(fg=Colors[7]))
            l3.bind('<Leave>',lambda e:l3.config(fg=Colors[2]))
            l3.bind('<Button-1>',lambda e:close_database())

            class configt:
                def tables(t):
                    set_tables(t,True)
                def pack(fill=None,side=None,pady=None,padx=None,expand=None):
                    frame.pack(fill=fill,side=side,pady=pady,padx=padx,expand=expand)
            return configt

        def Folder_Button(place,path,command=None,command_close=None,sercl_namber=0):
            frame=Frame(place,bg=Colors[6])
            fr=Frame(frame,bg=Colors[6])
            fr.pack(fill=X)
            fr1=Frame(frame,bg=Colors[6])
            aa=Frame(fr,width=sercl_namber,bg=Colors[6])
            aa.pack(side=LEFT)

            l1=Label(fr,image=chevron_r,bg=Colors[6],width=10,fg=Colors[2])
            l1.pack(side=LEFT)

            l2=Label(fr,text=f' {get_path_database(path)}',
                        font=('Calibri',10),
                        image=close_folder,
                        compound=LEFT,
                        anchor=NW,
                        bg=Colors[6],
                        fg=Colors[2])
            l2.pack(side=LEFT)
            if command_close:
                l2.config(width=152)
                def close_database():
                    frame.focus()
                    command_close(path)
                    frame.destroy()
                l3=Label(fr,text='x',font=('Consolas',8),bg=Colors[6],fg=Colors[2])
                l3.pack(side=LEFT,ipadx=6)
                l3.bind('<Enter>',lambda e:l3.config(fg=Colors[7]))
                l3.bind('<Leave>',lambda e:l3.config(fg=Colors[2]))
                l3.bind('<Button-1>',lambda e:close_database())
            def folder_items(Path):
                for i in os.listdir(Path):
                    if os.path.isdir(os.path.join(Path , i)):
                        folder1=Folder_Button(fr1,f'{Path}/{i}',command=command,sercl_namber=sercl_namber+20)
                        folder1.pack(fill=X)
                    elif i.endswith('.db'):
                        def a():
                            name=i
                            fra=Frame(fr1,bg=Colors[6])
                            fra.pack(fill=X)
                            aa=Frame(fra,width=sercl_namber+20,bg=Colors[6])
                            aa.pack(side=LEFT) 
                            l=Label(fra,text=f'      {name}',anchor=NW,bg=Colors[6],fg=Colors[2])
                            l.pack(side=LEFT,fill=X,expand=True)
                            def on():
                                l.config(bg=Colors[0])
                                fra.config(bg=Colors[0])
                                aa.config(bg=Colors[0])
                            def off():
                                l.config(bg=Colors[6])
                                fra.config(bg=Colors[6])
                                aa.config(bg=Colors[6])
                            def cal_data():
                                if command:
                                    command(f'{Path}/{name}')
                            fra.bind('<Enter>',lambda e:on())
                            fra.bind('<Leave>',lambda e:off())
                            fra.bind('<Button-1>',lambda e:cal_data())
                            l.bind('<Button-1>',lambda e:cal_data())
                        a()
            folder_items(path)
            var_rr=[True]
            
            def open_tables():
                frame.focus()
                if var_rr[0]:
                    var_rr[0]=False
                    l1.config(image=chevron_d)
                    l2.config(image=open_folder)
                    fr1.pack(fill=X)
                else:
                    var_rr[0]=True
                    l1.config(image=chevron_r)
                    l2.config(image=close_folder)
                    fr1.pack_forget()
            
            def on_frame():
                fr.config(bg=Colors[0])
                l1.config(bg=Colors[0])
                l2.config(bg=Colors[0])
                aa.config(bg=Colors[0])
             
                try:
                    l3.config(bg=Colors[0])
                except:pass
            def out_frame():
                fr.config(bg=Colors[6])
                l1.config(bg=Colors[6])
                l2.config(bg=Colors[6])
                aa.config(bg=Colors[6])
                try:
                    l3.config(bg=Colors[6])
                except:pass

            def ent(e):
                if var_rr[0]:
                    l1.config(image=chevron_r_a)
                else:
                    l1.config(image=chevron_d_a)
            def lev(e):
                if var_rr[0]:
                    l1.config(image=chevron_r)
                else:
                    l1.config(image=chevron_d)

            fr.bind('<Enter>',lambda e:on_frame())
            fr.bind('<Leave>',lambda e:out_frame())
            l1.bind('<Enter>',ent)
            l1.bind('<Leave>',lev)
            l1.bind('<Button-1>', lambda e: open_tables())
            l2.bind('<Button-1>', lambda e: open_tables())
            fr.bind('<Button-1>',lambda e: open_tables())


            
            class configt:
                def pack(fill=None,side=None,pady=None,padx=None,expand=None):
                    frame.pack(fill=fill,side=side,pady=pady,padx=padx,expand=expand)
                def pack_forget():
                    frame.pack_forget()
            return configt

        def close_folder_(path):
            parser.remove_option('last_folders',get_path_database(path))
            o=open('files\\Opne_last_folder.txt','w')
            parser.write(o)
        
        def close_database(db,db_name):
            def commit(ask):
                global table_opend
                if ask == 'Yes':
                    if table_opend in db.Tables():
                        show_table()
                    db.Commit()
                    db.close()
                else:
                    if table_opend in db.Tables():
                        show_table()
                    db.close()
            ask=My_Widget.Show_Message('Ask',f'Do you want to save {db_name} changes ?',commit)
            try:
                parser.remove_option('last_opened_databases',db_name)
                with open('files\\Opne_last_folder.txt','w') as config:
                    parser.write(config)
            except:
                print('parser not working')

        def check_if_database_exsete_and_open(path):
            try:
                if parser.has_section('last_opened_databases'):
                    if get_path_database(path).lower() in parser.options('last_opened_databases'):
                        My_Widget.Show_Message('Worning','Database opend alredy !')
                    else:
                        open_database(path)
                        parser.set('last_opened_databases',f'{get_path_database(path)}',path)
                        with open('files\\Opne_last_folder.txt','w') as write:
                            parser.write(write)
                else:
                    open_database(path)
                    parser.add_section('last_opened_databases')
                    parser.add_section('last_folders')
                    parser.set('last_opened_databases',f'{get_path_database(path)}',path)
                    with open('files\\Opne_last_folder.txt','w') as write:
                        parser.write(write)
            except sqlite3.Error as error:
                My_Widget.Show_Message('Error',error)

        def check_if_folder_exsete_and_open(path):
            def oopen():
                folder=Folder_Button(folders_frame,
                                    path,
                                    command=check_if_database_exsete_and_open,
                                    command_close=close_folder_)
                folder.pack(fill=X)
            
            if parser.has_section('last_folders'):
                if get_path_database(path).lower() in parser.options('last_folders'):
                    My_Widget.Show_Message('Worning','Folder opend alredy !')
                else:
                    oopen()
                    parser.set('last_folders',f'{get_path_database(path)}',path)
                    with open('files\\Opne_last_folder.txt','w') as write:
                        parser.write(write)
            else:
                oopen()
                parser.add_section('last_folders')
                parser.add_section('last_opened_databases')
                parser.set('last_folders',f'{get_path_database(path)}',path)
                with open('files\\Opne_last_folder.txt','w') as write:
                    parser.write(write)

        def Add_table(db,up_date=None):
            global Frame_Of_Action2
            try:
                Frame_Of_Action2.destroy()
            except:pass
            Frame_Of_Action2=Frame(root,
                                bg=Colors[1],
                                highlightbackground=Colors[8],
                                highlightcolor=Colors[8],
                                highlightthicknes=2)
            Frame_Of_Action2.place(x=-300,y=0,width=400,height=350)
            Frame_Of_Action2.focus()
            global Move_Frame_Of_Midel
            def Move_Frame_Of_Midel():
                My_Widget.Resize_Widget(root,Frame_Of_Action2,0,0,[400,350])
            Move_Frame_Of_Midel()
            ff=Frame(Frame_Of_Action2,bg=Colors[1])
            ff.pack(side=TOP,fill=X)
            def command_b():
                Frame_Of_Action2.destroy()
            But_1=Button(ff,
                        text='〤',
                        font=('Microsoft YaHei UI Light',10),
                        bg=Colors[1],
                        fg=Colors[8],
                        bd=0,
                        command=command_b)
            But_1.pack(side=RIGHT,ipadx=4)
            def but_1_enter(event):
                But_1.config(bg=Colors[6])
            def but_1_leave(event):
                But_1.config(bg=Colors[1])
            But_1.bind('<Enter>',but_1_enter)
            But_1.bind('<Leave>',but_1_leave)
            Label(ff,text='Create Table',fg=Colors[2],bg=Colors[1],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
            create_table_var=StringVar()
            er1=My_Widget.Entry_round(Frame_Of_Action2,'Table Name',create_table_var,Colors[1])
            er1.place(80,35)
            global the_values111
            the_values111=[]
            frame_columns=Scrolled_Frame(Frame_Of_Action2,
                                    bg=Colors[1],
                                    scroll_button_bg=Colors[9],
                                    scroll_button_active=Colors[8],
                                    scroll_vertical=True,
                                    scroll_unit=65,
                                    width=200)
            frame_columns.place(x=0,y=100,width=396,height=195)
            def get_c():
                global the_values111
                the_values111.clear()
                try:
                    for row in frame_columns.winfo_children():
                        row.destroy()
                except:pass
                for row in range(1,int(er2.get())+1):
                    l=LabelFrame(frame_columns,text=f'Column {row}',bg=Colors[1],fg='red',height=65)
                    l.pack(fill=X,padx=1)
                    f1=Frame(l,bg=Colors[1])
                    f1.pack(side=LEFT)
                    Label(f1,text='Column Name :',bg=Colors[1],fg=Colors[2]).pack()
                    en=Entry(f1,width=15,justify='center')
                    en.pack(pady=3,padx=2)
                    f2=Frame(l,bg=Colors[1])
                    f2.pack(side=LEFT)
                    Label(f2,text='Column Tayp :',bg=Colors[1],fg=Colors[2]).pack()
                    en1=ttk.Combobox(f2,
                                width=12,
                                justify='center',
                                values=['INT','VARCHAR','TEXT','DATE','PRIMARY KEY','INTEGER PRIMARY KEY AUTOINCREMENT'])
                    en1.pack(pady=2,padx=2)
                    f3=Frame(l,bg=Colors[1])
                    f3.pack(side=LEFT)
                    Label(f3,text='Length :',bg=Colors[1],fg=Colors[2]).pack()
                    en2=ttk.Combobox(f3,width=11,justify='center',values=[9,20,100,200,1000,10000])
                    en2.pack(pady=2,padx=2)
                    f4=Frame(l,bg=Colors[1])
                    f4.pack(side=LEFT)
                    Label(f4,text='Defult :',bg=Colors[1],fg=Colors[2]).pack()
                    en3=ttk.Combobox(f4,width=12,justify='center',values=['NULL','NOT NULL'])
                    en3.pack(pady=2,padx=2)
                    the_values111.append([en,en1,en2,en3])

            er2=Entry(Frame_Of_Action2,width=8,justify='center',font=('tajwal',11,'bold'))
            er2.insert(0,1)
            er2.place(x=120,y=70)
            er3=Label(Frame_Of_Action2,text='Column',
                                        highlightbackground='red',
                                        highlightthicknes=1,
                                        fg=Colors[2],bg=Colors[1])
            er3.place(x=240,y=70)
            er3.bind('<Enter>',lambda e:er3.config(bg=Colors[0]))
            er3.bind('<Leave>',lambda e:er3.config(bg=Colors[1]))
            er3.bind('<Button-1>',lambda e:get_c())
            ff1=Frame(Frame_Of_Action2,bg=Colors[1])
            ff1.pack(side=BOTTOM,fill=X)
            def create_d():
                global the_values111
                the_sql_of_col=''
                bb=False
                for row in the_values111:
                    v=[]
                    for i in row:
                        r=i.get()
                        try:
                            v.append(f' ({int(r)})')
                        except:
                            v.append(f' {r}')
                    if v[1] == ' PRIMARY KEY':
                        g=v[2]
                        v.pop(2)
                        v.insert(1,f' INT{g}')

                    elif v[1] ==' INTEGER PRIMARY KEY AUTOINCREMENT':
                        v.pop(2) 

                    elif v[1] == ' DATE':
                        v.pop(2)
                    if bb==True:
                        the_sql_of_col+=','
                    the_sql_of_col+=''.join(v)
                    bb=True
                create=db.Create_Table(create_table_var.get(),the_sql_of_col)
                if create == True:
                    My_Widget.Show_Message('Create',f'Table {create_table_var.get()} created seccesfly')
                    Frame_Of_Action2.destroy()
                    if up_date:
                        up_date()
                else:
                    My_Widget.Show_Message('Error',create)
            bim=My_Widget.Button_of_text_and_image(ff1,'Create',create,Mycommand=create_d )
        
        def Search(table):
            global Frame_Of_Action2
            try:
                Frame_Of_Action2.destroy()
            except:pass
            Frame_Of_Action2=Frame(root,
                                bg=Colors[1],
                                highlightbackground=Colors[8],
                                highlightcolor=Colors[8],
                                highlightthicknes=2)
            Frame_Of_Action2.place(x=-300,y=0,width=600,height=400)
            Frame_Of_Action2.focus()
            global Move_Frame_Of_Midel
            def Move_Frame_Of_Midel():
                My_Widget.Resize_Widget(root,Frame_Of_Action2,0,0,[600,400])
            Move_Frame_Of_Midel()
            ff=Frame(Frame_Of_Action2,bg=Colors[1])
            ff.pack(fill=X)
            ff1=Frame(Frame_Of_Action2,bg=Colors[1])
            ff1.pack(fill=X,padx=2)
            def command_b():
                Frame_Of_Action2.focus()
                Frame_Of_Action2.destroy()
            But_1=Button(ff,
                        text='〤',
                        font=('Microsoft YaHei UI Light',10),
                        bg=Colors[1],
                        fg=Colors[8],
                        bd=0,
                        command=command_b)
            But_1.pack(side=RIGHT,ipadx=4)
            def but_1_enter(event):
                But_1.config(bg=Colors[6])
            def but_1_leave(event):
                But_1.config(bg=Colors[1])
            But_1.bind('<Enter>',but_1_enter)
            But_1.bind('<Leave>',but_1_leave)
            Label(ff,text='Search',fg=Colors[2],bg=Colors[1],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
            TV_Frame2=Frame(Frame_Of_Action2,bg=Colors[1])
            TV_Frame2.pack(fill=BOTH,expand=1)
            global The_Focus_value22
            The_Focus_value22=[]
            global column_names_list11
            column_names_list11=[]
            def get_searched(search=None):
                for wedget in TV_Frame2.winfo_children():
                    wedget.destroy()
                cour=table.Columns()[0]
                scroll_v=Scroll(TV_Frame2,button_bg=Colors[9],button_bg_active=Colors[8])
                scroll_v.pack(side=RIGHT,fill=Y)
                scroll_h=Scroll(TV_Frame2,orient='horizontal',button_bg=Colors[9],button_bg_active=Colors[8])
                scroll_h.pack(side=BOTTOM,fill=X)
                count :int
                global column_names_list11
                column_names_list11=[]
                col_count=[]
                count=0
                for row in cour:
                    column_names_list11.append(row)
                    col_count.append(f'#{count}')
                    count+=1
                TV2=ttk.Treeview(TV_Frame2,columns=(col_count))
                scroll_v.configure(command=TV2.yview)
                TV2.configure(yscrollcommand=scroll_v.set)
                scroll_h.configure(command=TV2.xview)
                TV2.configure(xscrollcommand=scroll_h.set)
                TV2.pack(side=LEFT,fill=BOTH,expand=True)
                for row in range(len(column_names_list11)):
                    TV2.heading(f'#{row}',text=column_names_list11[row])
                    TV2.column(f'#{row}',width=100)   
                def Treeview_Menu2(event):
                    try:
                        row_id=TV2.identify_row(event.y)
                        TV2.selection_set(row_id)
                        row_values=TV2.item(row_id)
                        tt=[row_values['text']]
                        rr=tt+(row_values['values'])
                        rr.pop()
                        global The_Focus_v
                        The_Focus_v=rr

                        My_Widget.My_Menu(event,
                                        values=['Add','Update','Delete'],
                                        commands=[  lambda:Add_Row(table),
                                                    lambda:Update_Row(table),
                                                    lambda:Delete_row(table)])
                    except:pass
                TV2.bind('<Button-3>',Treeview_Menu2)
                def Get_Cursor(event):
                    try:
                        cursor_row=TV2.focus() 
                        contents=TV2.item(cursor_row)
                        tt=[contents['text']]
                        rr=tt+(contents['values'])
                        rr.pop()
                        global The_Focus_value22
                        The_Focus_value22=rr
                    except:pass
                TV2.bind('<ButtonRelease-1>',Get_Cursor)
                if search:
                    count=0
                    for row in table.Search(search[0],search[1]):
                        TV2.insert('','end',count,text=row[0])
                        for i in range(1,len(column_names_list11)):
                            TV2.set(count,f'#{i}',row[i])
                        count+=1      
            get_searched()
            global searchfor
            searchfor=StringVar()
            def get_it():
                get_searched([searchfor.get(),entry_i.get()])
            fr=Frame(ff1,bg=Colors[1])
            fr.pack(side=LEFT,padx=5)
            bim2 = Round_Button(    master=fr,
                                    image=search_png,
                                    fg=Colors[2],
                                    width=100,
                                    text='  Search  ',
                                    font=('tajwal',13),
                                    outline=Colors[0],
                                    bg_active=Colors[0],
                                    command=get_it,
                                    ipadx=2,
                                    ipady=2)
            bim2.pack(side= 'left')
            entry_i=Round_Entry  (  master=ff1,
                                    bg=Colors[0],
                                    fg=Colors[2],
                                    font=('tajwal',12,'normal'),
                                    justify='center',
                                    outline=Colors[9],
                                    width=26,
                                    outline_focus=Colors[7])
            entry_i.pack(side='left',pady=4,padx=4)
            lib=Label(ff1,text='search for',bg=Colors[6],fg=Colors[2])
            lib.pack(side=LEFT)
            def ent(event):
                lib.config(bg=Colors[0])
            def lev(event):
                lib.config(bg=Colors[6])
            try:
                searchfor.set(column_names_list11[0])
            except:pass
            def frame_ch(event):
                f5=Frame(root,bg=Colors[1],
                            highlightbackground=Colors[7],
                            highlightcolor=Colors[7],
                            highlightthicknes=1)
                f5.place(x=lib.winfo_x()+lib.winfo_width()+ff1.winfo_x()+Frame_Of_Action2.winfo_x(),
                    y=lib.winfo_y()+ff1.winfo_y()+Frame_Of_Action2.winfo_y())
                f5.focus() 
                def f_out():
                    f5.destroy()
                try:
                    global column_names_list11                    
                    for row in column_names_list11:
                        Checkbutton(f5,text=row,bg=Colors[1],fg=Colors[7],
                                onvalue=row,offvalue='',variable=searchfor,command=f_out).pack(anchor=NW)
                except:pass
                f5.bind('<FocusOut>',lambda e:f_out())
            lib.bind('<Enter>',ent)
            lib.bind('<Leave>',lev)
            lib.bind('<Button-1>',frame_ch)

        def Add_Row(table):
            global Frame_Of_Action2
            try:
                Frame_Of_Action2.destroy()
            except:pass
            Frame_Of_Action2=Frame(root,
                                bg=Colors[1],
                                highlightbackground=Colors[8],
                                highlightcolor=Colors[8],
                                highlightthicknes=2)
            Frame_Of_Action2.place(x=-300,y=0,width=400,height=302)
            Frame_Of_Action2.focus()
            global Move_Frame_Of_Midel
            def Move_Frame_Of_Midel():
                My_Widget.Resize_Widget(root,Frame_Of_Action2,0,0,[400,302])
            Move_Frame_Of_Midel()
            ff=Frame(Frame_Of_Action2,bg=Colors[1])
            ff.pack(fill=X)
            ff1=Frame(Frame_Of_Action2,bg=Colors[1])
            ff1.pack(side=BOTTOM,fill=X)
            frame_sc=Scrolled_Frame(Frame_Of_Action2,
                                    bg=Colors[6],
                                    scroll_vertical=True,
                                    scroll_button_bg=Colors[9],
                                    scroll_button_active=Colors[8],
                                    scroll_unit=41)
            frame_sc.pack(side=LEFT,fill=BOTH)
            def command_b():
                Frame_Of_Action2.destroy()
            But_1=Button(ff,
                        text='〤',
                        font=('Microsoft YaHei UI Light',10),
                        bg=Colors[1],
                        fg=Colors[8],
                        bd=0,
                        command=command_b)
            But_1.pack(side=RIGHT,ipadx=4)
            def but_1_enter(event):
                But_1.config(bg=Colors[6])
            def but_1_leave(event):
                But_1.config(bg=Colors[1])
            But_1.bind('<Enter>',but_1_enter)
            But_1.bind('<Leave>',but_1_leave)
            Label(ff,text='Add Row',fg=Colors[2],bg=Colors[1],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
            the_columns=[]
            the_values=[]
            y=2
            pry=table.Columns()[1]
            col=table.Columns()[0]
            mes=''
            for row in col:
                Frame(frame_sc,bg=Colors[6],height=39).pack()
                if row == pry:
                    er1=Round_Entry  (       
                                            master=frame_sc,
                                            bg=Colors[0],
                                            fg=Colors[2],
                                            text=f'{row} - PRIMARY KEY AUTOINCREMENT',
                                            font=('tajwal',12,'normal'),
                                            justify='center',
                                            outline=Colors[9],
                                            width=26,
                                            outline_focus=Colors[7],
                                        )
                    er1.place(x=70,y=y)
                    the_columns.append(row[0])
                    the_values.append(er1)
                    y+=40
                else:
                    er1=Round_Entry  (       
                                            master=frame_sc,
                                            bg=Colors[0],
                                            fg=Colors[2],
                                            text=row,
                                            font=('tajwal',12,'normal'),
                                            justify='center',
                                            outline=Colors[9],
                                            width=26,
                                            outline_focus=Colors[7],
                                        )
                    er1.place(x=70,y=y)
                    the_columns.append(row[0])
                    the_values.append(er1)
                    y+=40
            def add_row():
                values_=[]
                cols=[]
                for i in range(len(the_values)) :
                    va=the_values[i].get()
                    if va == mes or va == '' or va in col :
                        pass
                    else:
                        values_.append(va)
                        cols.append(col[i])
                add=table.Add(cols,values_)
                if add == True:
                    My_Widget.Show_Message('insert','info inserted successfully')
                    show_table(table)
                    Frame_Of_Action2.destroy()
                else:
                    My_Widget.Show_Message('Error',add)
            But_1 = Round_Button(   master=ff1,
                                    image=create,
                                    fg=Colors[2],
                                    width=90,
                                    text='   Save ',
                                    font=('tajwal',13),
                                    outline=Colors[0],
                                    bg_active=Colors[0],
                                    command=add_row,
                                    ipadx=2,
                                    ipady=2)
            But_1.pack(side='left',expand=True,pady=1)

        def Delete_row(table):
            global Frame_Of_Action2
            try:
                Frame_Of_Action2.destroy()
            except:pass
            global The_Focus_v
            if The_Focus_v:
                list_inw =table.Columns()[0]

                nomber=0
                def Delete_Row(ask):
                    if ask == 'Yes':
                        d=table.Delete(list_inw[nomber],The_Focus_v[nomber])
                        if d ==True:
                            show_table(table)
                        else:
                            My_Widget.Show_Message('Error',d)
                            
                while True:
                    try:
                        list_select=table.Search(list_inw[nomber],The_Focus_v[nomber])
                        if len(list_select) == 1:
                            My_Widget.Show_Message('Delete',
                            f'Are you sure you want to delete row {The_Focus_v[0]}?',
                            Delete_Row)
                            break
                        if nomber == len(list_inw)-1:
                            My_Widget.Show_Message('Delete',
                            f'there is {len(list_inw)} rows {The_Focus_v[0]} have the same data do you want to delete all of them inywhay?',Delete_Row)
                            break
                        nomber+=1
                    except mysql.connector.Error as error :
                        My_Widget.Show_Message('Error',error)
                        break
            
            else:
                My_Widget.Show_Message('Worning','Plasse selecte the row')

        def Update_Row(table):
            global Frame_Of_Action2
            try:
                Frame_Of_Action2.destroy()
            except:pass
            global The_Focus_v
            if The_Focus_v:
                Frame_Of_Action2=Frame(root,
                                    bg=Colors[1],
                                    highlightbackground=Colors[8],
                                    highlightcolor=Colors[8],
                                    highlightthicknes=2)
                Frame_Of_Action2.place(x=-300,y=0,width=400,height=308)
                Frame_Of_Action2.focus()
                global Move_Frame_Of_Midel
                def Move_Frame_Of_Midel():
                    My_Widget.Resize_Widget(root,Frame_Of_Action2,0,0,[400,308])
                Move_Frame_Of_Midel()
                ff=Frame(Frame_Of_Action2,bg=Colors[1])
                ff.pack(fill=X)
                ff1=Frame(Frame_Of_Action2,bg=Colors[1])
                ff1.pack(side=BOTTOM,fill=X)
                frame_scr=Scrolled_Frame(Frame_Of_Action2,
                                            bg=Colors[1],
                                            scroll_vertical=True,
                                            scroll_button_bg=Colors[9],
                                            scroll_button_active=Colors[8],
                                            scroll_unit=60)
                frame_scr.pack(side=LEFT,fill=BOTH)
                def command_b():
                    global The_Focus_v
                    The_Focus_v=[]
                    Frame_Of_Action2.destroy()
                But_1=Button(ff,
                            text='〤',
                            font=('Microsoft YaHei UI Light',10),
                            bg=Colors[1],
                            fg=Colors[8],
                            bd=0,
                            command=command_b)
                But_1.pack(side=RIGHT,ipadx=4)
                But_1.bind('<Enter>',lambda e:But_1.config(bg=Colors[6]))
                But_1.bind('<Leave>',lambda e:But_1.config(bg=Colors[1]))
                Label(ff,text='Update Row',
                        fg=Colors[2],
                        bg=Colors[1],
                        font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
                the_columns=[]
                the_values=[]
                y=10
                count_=0 
                va=table.Columns()[1]
                for row in table.Columns()[0]:
                    lb=Label(frame_scr,text=f'{row} :',fg=Colors[7],bg=Colors[1],font=('tajwal',11))
                    lb.place(x=90,y=y)
                    er1=Round_Entry  (       
                                            master=frame_scr,
                                            bg=Colors[0],
                                            fg=Colors[2],
                                            font=('tajwal',12,'normal'),
                                            justify='center',
                                            outline=Colors[9],
                                            width=26,
                                            outline_focus=Colors[7],
                                        )
                    er1.place(x=80,y=y+20)
                    try:
                        er1.insert(0,The_Focus_v[count_])
                    except:pass

                    if row == va:
                        lb.config(text=f'{row} : PRIMARY KEY AUTOINCREMENT')
                        er1.config(fg='red')
                    the_columns.append(row)
                    the_values.append(er1)
                    frame_scr.config(height=y+50)
                    y+=60
                    count_+=1   
                def add_row():
                    vl=[]
                    for row in the_values:
                        vl.append(row.get())
                    er=table.Update(the_columns,vl,the_columns[0],The_Focus_v[0])
                    if er ==True:
                        My_Widget.Show_Message('insert',f'row {The_Focus_v[0]} updated seccesfly')
                        show_table(table)
                        command_b()
                    else:
                        My_Widget.Show_Message('Error',er)
                But_1 = Round_Button(   master=ff1,
                                        image=create,
                                        fg=Colors[2],
                                        width=90,
                                        text='   Save ',
                                        font=('tajwal',13),
                                        outline=Colors[0],
                                        bg_active=Colors[0],
                                        command=add_row,
                                        ipadx=2,
                                        ipady=2)
                But_1.pack(side='left',expand=True,pady=1)
            else:My_Widget.Show_Message('Error','Plasse selecte the column')

        def Add_Column(table):
            global Frame_Of_Action2
            try:
                Frame_Of_Action2.destroy()
            except:pass
            Frame_Of_Action2=Frame(root,
                                bg=Colors[6],
                                highlightbackground=Colors[8],
                                highlightcolor=Colors[8],
                                highlightthicknes=2)
            Frame_Of_Action2.place(x=-300,y=0,width=400,height=300)
            Frame_Of_Action2.focus()
            global Move_Frame_Of_Midel
            def Move_Frame_Of_Midel():
                My_Widget.Resize_Widget(root,Frame_Of_Action2,0,0,[400,300])
            Move_Frame_Of_Midel()
            ff=Frame(Frame_Of_Action2,bg=Colors[6])
            ff.pack(side=TOP,fill=X)
            ff1=Frame(Frame_Of_Action2,bg=Colors[6])
            ff1.pack(side=TOP,fill=X)
            ff3=Frame(Frame_Of_Action2,bg=Colors[6])
            ff3.pack(side=BOTTOM,fill=X)
            ff2=Frame(Frame_Of_Action2,bg=Colors[6])
            ff2.pack(fill=BOTH,expand=True)
            def command_b():
                Frame_Of_Action2.focus()
                Frame_Of_Action2.destroy()
            But_1=Button(ff,
                        text='〤',
                        font=('Microsoft YaHei UI Light',10),
                        bg=Colors[6],
                        fg=Colors[8],
                        bd=0,
                        command=command_b)
            But_1.pack(side=RIGHT,ipadx=4)
            But_1.bind('<Enter>',lambda e:But_1.config(bg=Colors[4]))
            But_1.bind('<Leave>',lambda e:But_1.config(bg=Colors[6]))
            Label(ff,text='Add Column',fg=Colors[2],bg=Colors[6],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
            def create_t(sql):
                print(sql)
                create=table.Add_Column(sql)
                if create == True:
                    Frame_Of_Action2.destroy()
                    show_table(table)
                    My_Widget.Show_Message('Create',f'column is add seccesfly')
                else:
                    My_Widget.Show_Message('Error',create)
            def use_enters():
                Column_Name=StringVar()
                Column_Type=StringVar()
                Length=StringVar()
                Defult=StringVar()
                er1=My_Widget.Entry_round(ff2,'Column Name',Column_Name,bg=Colors[6])
                er1.place(80,30)
                er2=My_Widget.Combobox_round(ff2,
                            'Column Type',
                            Column_Type,bg=Colors[6],
                            values=['INT','VARCHAR',
                                    'TEXT','DATE',
                                    'PRIMARY KEY',
                                    'PRIMARY KEY AUTO_INCREMENT'])
                er2.place(x=80,y=70)
                er3=My_Widget.Combobox_round(ff2,
                            'Length',
                            Length,bg=Colors[6],
                            values=['11','100','200','500','1000','10000','100000'])
                er3.place(x=80,y=110)
                er4=My_Widget.Combobox_round(ff2,
                            'Defult',
                            Defult,bg=Colors[6],
                            values=['NULL','NOT NULL'])
                er4.place(x=80,y=150)

                def get_text_execute():
                    infovar1=Column_Name.get()
                    if infovar1 =='Column Name':
                        infovar1 =''
                    infovar2=Column_Type.get()
                    if infovar2 =='Column Type':
                        infovar2 =''
                    infovar3=Length.get()
                    if infovar3 and infovar3!='Length':
                        infovar3=f'({infovar3})'
                    else:
                        infovar3=''
                    infovar4=Defult.get()
                    if infovar4 =='Defult':
                        infovar4 =''

                    if infovar2 == 'DATE':
                        infovar3=''
                    if infovar2 in ['PRIMARY KEY','PRIMARY KEY AUTO_INCREMENT']:
                        infovar3=f'INT{infovar3}'
                        return f'{infovar1} {infovar3} {infovar2} {infovar4} '
                    else:
                        return f'{infovar1} {infovar2} {infovar3} {infovar4} '
                def send_execute_info():
                    create_t(get_text_execute())
                But_1 = Round_Button(   master=ff3,
                                        image=add_png,
                                        fg=Colors[2],
                                        width=90,
                                        text='   Add  ',
                                        font=('tajwal',13),
                                        outline=Colors[0],
                                        bg_active=Colors[0],
                                        command=send_execute_info,
                                        ipadx=2,
                                        ipady=2)
                But_1.pack(side='left',expand=True,pady=1)
                
            use_enters()

        def Rename_Column(table):
            global Frame_Of_Action2
            try:
                Frame_Of_Action2.destroy()
            except:pass
            Frame_Of_Action2=Frame(root,
                                bg=Colors[6],
                                highlightbackground=Colors[8],
                                highlightcolor=Colors[8],
                                highlightthicknes=2)
            Frame_Of_Action2.place(x=-300,y=0,width=400,height=300)
            Frame_Of_Action2.focus()
            global Move_Frame_Of_Midel
            def Move_Frame_Of_Midel():
                My_Widget.Resize_Widget(root,Frame_Of_Action2,0,0,[400,300])
            Move_Frame_Of_Midel()
            ff=Frame(Frame_Of_Action2,bg=Colors[6])
            ff.pack(side=TOP,fill=X)
            ff1=Frame(Frame_Of_Action2,bg=Colors[6])
            ff1.pack(side=TOP,fill=X)
            ff3=Frame(Frame_Of_Action2,bg=Colors[6])
            ff3.pack(side=BOTTOM,fill=X)
            ff2=Frame(Frame_Of_Action2,bg=Colors[6])
            ff2.pack(fill=BOTH,expand=True)
            def command_b():
                Frame_Of_Action2.focus()
                Frame_Of_Action2.destroy()
            But_1=Button(ff,
                        text='〤',
                        font=('Microsoft YaHei UI Light',10),
                        bg=Colors[6],
                        fg=Colors[8],
                        bd=0,
                        command=command_b)
            But_1.pack(side=RIGHT,ipadx=4)
            But_1.bind('<Enter>',lambda e:But_1.config(bg=Colors[4]))
            But_1.bind('<Leave>',lambda e:But_1.config(bg=Colors[6]))
            Label(ff,text='Rename Column',
                    fg=Colors[2],
                    bg=Colors[6],
                    font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
            Column=StringVar()
            new_name=StringVar()
            get_col=My_Widget.Combobox_round(ff2,
                        'Column Name',
                        Column,bg=Colors[6],
                        values=table.Columns()[0])
            get_col.place(80,60)

            ent_n=My_Widget.Entry_round(ff2,'New Name',new_name,bg=Colors[6])
            ent_n.place(80,90)
            
            def Rename(anser):
                if anser == 'Yes':
                    er=table.Rename_Column(Column.get(),new_name.get())
                    if er == True:
                        My_Widget.Show_Message('Deleted',f'Column \'{Column.get()}\' Renamed seccesfuly !')
                        command_b()
                        root.after(100,lambda:show_table(table))
                    else:
                        My_Widget.Show_Message('Error',er)
            def ask_for_Rename():
                My_Widget.Show_Message('Ask',
                    f'Are you sure you want to rename \'{Column.get()}\' to \'{new_name.get()}\' ?',Rename)
            But_1 = Round_Button(   master=ff3,
                                    image=change_png,
                                    fg=Colors[2],
                                    width=90,
                                    text='  Rename ',
                                    font=('tajwal',13),
                                    outline=Colors[0],
                                    bg_active=Colors[0],
                                    command=ask_for_Rename,
                                    ipadx=2,
                                    ipady=2)
            But_1.pack(side='left',expand=True,pady=1)

        def Delete_Column(table):
            global Frame_Of_Action2
            try:
                Frame_Of_Action2.destroy()
            except:pass
            Frame_Of_Action2=Frame(root,
                                bg=Colors[6],
                                highlightbackground=Colors[8],
                                highlightcolor=Colors[8],
                                highlightthicknes=2)
            Frame_Of_Action2.place(x=-300,y=0,width=400,height=300)
            Frame_Of_Action2.focus()
            global Move_Frame_Of_Midel
            def Move_Frame_Of_Midel():
                My_Widget.Resize_Widget(root,Frame_Of_Action2,0,0,[400,300])
            Move_Frame_Of_Midel()
            ff=Frame(Frame_Of_Action2,bg=Colors[6])
            ff.pack(side=TOP,fill=X)
            ff1=Frame(Frame_Of_Action2,bg=Colors[6])
            ff1.pack(side=TOP,fill=X)
            ff3=Frame(Frame_Of_Action2,bg=Colors[6])
            ff3.pack(side=BOTTOM,fill=X)
            ff2=Frame(Frame_Of_Action2,bg=Colors[6])
            ff2.pack(fill=BOTH,expand=True)
            def command_b():
                Frame_Of_Action2.focus()
                Frame_Of_Action2.destroy()
            But_1=Button(ff,
                        text='〤',
                        font=('Microsoft YaHei UI Light',10),
                        bg=Colors[6],
                        fg=Colors[8],
                        bd=0,
                        command=command_b)
            But_1.pack(side=RIGHT,ipadx=4)
            But_1.bind('<Enter>',lambda e:But_1.config(bg=Colors[4]))
            But_1.bind('<Leave>',lambda e:But_1.config(bg=Colors[6]))
            Label(ff,text='Delete Column',fg=Colors[2],bg=Colors[6],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
            Column=StringVar()
            get_col=My_Widget.Combobox_round(ff2,
                        'Column Name',
                        Column,bg=Colors[6],
                        values=table.Columns()[0])
            get_col.place(80,80)
            def delete(anser):
                if anser == 'Yes':
                    er=table.Drop_Column(Column.get())
                    if er == True:
                        My_Widget.Show_Message('Deleted',f'Column {Column.get()} is deleted seccesfuly !')
                        command_b()
                        root.after(100,lambda:show_table(table))
                    else:
                        My_Widget.Show_Message('Error',er)
            def ask_for_delete():
                My_Widget.Show_Message('Ask',f'Are you sure you want to delete {Column.get()} ?',delete)
            But_2 = Round_Button(   master=ff3,
                                    image=drop_png,
                                    fg=Colors[2],
                                    width=90,
                                    text='   Delete  ',
                                    font=('tajwal',13),
                                    outline=Colors[0],
                                    bg_active=Colors[0],
                                    command=ask_for_delete,
                                    ipadx=2,
                                    ipady=2)
            But_2.pack(side='left',expand=True,pady=1)
        
        def open_database(DB):
            db=DB_Connect.connect(DB)
            tables=db.Tables()
            
            def Opend_table(table_name):
                _table_=db.Open(table_name)
                show_table(_table_)
                But_1.configure(command=lambda :Add_Row(_table_))
                But_2.configure(command=lambda :Update_Row(_table_))
                But_3.configure(command=lambda :Delete_row(_table_))
                But_4.configure(command=lambda :Search(_table_))
                But_5.configure(command=lambda :Add_Column(_table_))
                But_6.configure(command=lambda :Rename_Column(_table_))
                But_7.configure(command=lambda :Delete_Column(_table_))

            def command_table(table_name,command):
                if command == 'Open Table':
                    Opend_table(table_name)
                elif command == 'Add Table':
                    def update():
                        file_b.tables(db.Tables())
                    Add_table(db,update)
                elif command == 'Drop Table':
                    global table_opend
                    if table_opend == table_name:
                        show_table()
                    db.Drop_Table(table_name)
                    file_b.tables(db.Tables())

            file_b=File_Button(files_frame,
                        text=f'{get_path_database(DB)}',
                        command=command_table,
                        tables=tables,
                        command_close=lambda:close_database(db,get_path_database(DB)))
            file_b.pack(fill=X)

        global Create_DB
        def Create_DB():
            var=filedialog.askdirectory()
            if var:
                closeframe1()
                global Frame_Of_Action2
                try:
                    Frame_Of_Action2.destroy()
                except:pass
                Frame_Of_Action2=Frame(root,
                                    bg=Colors[1],
                                    highlightbackground=Colors[8],
                                    highlightcolor=Colors[8],
                                    highlightthicknes=2)
                Frame_Of_Action2.place(x=-300,y=0,width=400,height=300)
                Frame_Of_Action2.focus()
                global Move_Frame_Of_Midel
                def Move_Frame_Of_Midel():
                    My_Widget.Resize_Widget(root,Frame_Of_Action2,0,0,[400,300])
                Move_Frame_Of_Midel()
                ff=Frame(Frame_Of_Action2,bg=Colors[1])
                ff.pack(side=TOP,fill=X)
                But_1=Button(ff,
                            text='〤',
                            font=('Microsoft YaHei UI Light',10),
                            bg=Colors[1],
                            fg=Colors[8],
                            bd=0,
                            command=lambda:Frame_Of_Action2.destroy())
                But_1.pack(side=RIGHT,ipadx=4)
                But_1.bind('<Enter>',lambda e:But_1.config(bg=Colors[6]))
                But_1.bind('<Leave>',lambda e:But_1.config(bg=Colors[1]))
                Label(ff,text='Create DB',fg=Colors[2],bg=Colors[1],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
                
                create_db=StringVar()
                er=My_Widget.Entry_round(Frame_Of_Action2,'DB Name',create_db,Colors[1])
                er.place(80,100)

                ff1=Frame(Frame_Of_Action2,bg=Colors[1])
                ff1.pack(side=BOTTOM,fill=X)
                
                def create_d():
                    db=create_db.get()
                    try:
                        if f'{db[-3]+db[-2]+db[-1]}'=='.db':
                            Db=db
                        else:
                            Db=f'{db}.db'
                    except:
                        Db=f'{db}.db'
                    check_if_database_exsete_and_open(f'{var}/{Db}')
                    DB_Frame.Up_Scroll()
                    Frame_Of_Action2.destroy()
                bim=My_Widget.Button_of_text_and_image(ff1,'Create',create,Mycommand=create_d )
                bim.config(bg=Colors[1],bg_on=Colors[6])

        global ask_open_db_file
        def ask_open_db_file():
            file=filedialog.askopenfilename(title='Datavase Files',
                                        filetypes=(('db files','*.db'),('all files','*.*')))
            if file:
                check_if_database_exsete_and_open(file)

        global ask_open_db_folder
        def ask_open_db_folder():
            file=filedialog.askdirectory()
            if file:
                check_if_folder_exsete_and_open(file)

        def get_last_all_opend():
            try:
                rr=parser.options('last_opened_databases')
                for i in rr:
                    var=parser.get('last_opened_databases', i)
                    try:
                        open_database(var)
                    except:pass
                r1=parser.options('last_folders')
                for ii in r1:
                    var1=parser.get('last_folders',ii)
                    try:
                        folder=Folder_Button(folders_frame,
                                            var1,
                                            command=check_if_database_exsete_and_open,
                                            command_close=close_folder_)
                        folder.pack(fill=X)
                    except:pass
            except:pass
        get_last_all_opend()

        def Change_Colors5(colors):
            Frame_3.config(bg=colors[6])
            Frame1.config(bg=colors[6])
            DB_Frame.config(bg=colors[6],scroll_button_bg=colors[9],scroll_button_active=colors[8])
            Frame_open.config(bg=colors[6])
            laab1.config(bg=colors[6],fg=colors[2])
            laab.config(bg=colors[6],fg=colors[2])
            scrol_ver.configure(button_bg=colors[9],button_bg_active=colors[8])
            scrol_hor.configure(button_bg=colors[9],button_bg_active=colors[8])
            But_1.configure(fg=colors[2],image=add_png,outline=colors[0],bg_active=colors[0])
            But_2.configure(fg=colors[2],image=update_png,outline=colors[0],bg_active=colors[0])
            But_3.configure(fg=colors[2],image=drop_png,outline=colors[0],bg_active=colors[0])
            But_4.configure(fg=colors[2],image=search_png,outline=colors[0],bg_active=colors[0])
            But_5.configure(fg=colors[2],image=add_png,outline=colors[0],bg_active=colors[0])
            But_6.configure(fg=colors[2],image=change_png,outline=colors[0],bg_active=colors[0])
            But_7.configure(fg=colors[2],image=drop_png,outline=colors[0],bg_active=colors[0])
            TV_Frame2.config(bg=colors[6],highlightbackground=colors[9],highlightcolor=colors[9])
            TV_Frame3.config(bg=colors[6])
        Container_Configer_Color[5]=Change_Colors5


    def Parametr_Page():
        Label(Frame_4,text='second Frame',bg=Colors[6],fg='red').pack(expand=True)
        Frame_4.focus()   

    DB_Page()
    Parametr_Page()
    
    def connect_server():
        Fr_one=Frame(Frame_2,
                    highlightthickness=1,
                    highlightcolor=Colors[9],
                    highlightbackground=Colors[9],
                    bg=Colors[6])
        Fr3=Frame(Frame_2,
                    highlightthickness=1,
                    highlightcolor=Colors[9],
                    highlightbackground=Colors[9],
                    bg=Colors[6])
        Fr4=Frame(Frame_2,
                    highlightthickness=1,
                    highlightcolor=Colors[9],
                    highlightbackground=Colors[9],
                    bg=Colors[6])
        Fr_one.pack(side=LEFT,fill=Y,padx=1,pady=1)

        title_label=Label(Fr_one,
                            text='Databases',
                            font=('Century Schoolbook',12,'bold italic'),
                            bg=Colors[4],
                            fg=Colors[7])
        title_label.pack(side='top',fill='x',ipady=1)
        Fr21=Frame(Fr_one,bg=Colors[6])
        Fr21.pack(side=BOTTOM,fill=BOTH,pady=2)
        def quit():
            Home_Page()
            root.after(100,resize_entrys)
        but11 = Round_Button(   master=Fr21,
                                image=create,
                                fg=Colors[2],
                                width=100,
                                text='  Create  ',
                                font=('tajwal',13),
                                outline=Colors[0],
                                bg_active=Colors[0],
                                ipadx=2,
                                ipady=2)
        but11.pack(side='left',expand=True)
        but21 = Round_Button(   master=Fr21,
                                image=quit_png,
                                fg=Colors[2],
                                width=100,
                                text='  Quit  ',
                                font=('tajwal',13),
                                outline=Colors[0],
                                bg_active=Colors[0],
                                command=quit,
                                ipadx=2,
                                ipady=2)
        but21.pack(side='left',expand=True)
        frame_with=Scrolled_Frame(  master=Fr_one,
                                    width=260,
                                    bg=Colors[6],
                                    scroll_vertical=True,
                                    scroll_unit=32,
                                    scroll_button_bg=Colors[9],
                                    scroll_button_active=Colors[8])
        frame_with.pack(side=LEFT,fill=Y)

        title_label1=Label(Fr3,
                        text='',
                        font=('Century Schoolbook',12,'bold italic'),
                        bg=Colors[4],
                        fg=Colors[7])
        title_label1.pack(side=TOP,fill=X,ipady=1)
        Fr2_1=Frame(Fr3,bg=Colors[6])
        Fr2_1.pack(side=BOTTOM,fill=BOTH,pady=2)
        but1 = Round_Button(master=Fr2_1,
                            image=create,
                            fg=Colors[2],
                            width=100,
                            text='  Create  ',
                            font=('tajwal',13),
                            outline=Colors[0],
                            bg_active=Colors[0],
                            ipadx=2,
                            ipady=2)
        but1.pack(side='left',expand=True)
        but2 = Round_Button(master=Fr2_1,
                            image=drop_png,
                            fg=Colors[2],
                            width=100,
                            text='    Drop  ',
                            font=('tajwal',13),
                            outline=Colors[0],
                            bg_active=Colors[0],
                            ipadx=2,
                            ipady=2)
        but2.pack(side='left',expand=True)
        Fr2=Scrolled_Frame( master=Fr3,
                            width=260,
                            bg=Colors[6],
                            scroll_vertical=True,
                            scroll_unit=32,
                            scroll_button_bg=Colors[9],
                            scroll_button_active=Colors[8])
        Fr2.pack(side=LEFT,fill=Y)



        def Search(Database_Name,Table_Name):
            global Frame_Of_Action
            try:
                Frame_Of_Action.destroy()
            except:pass
            Frame_Of_Action=Frame(root,
                                bg=Colors[1],
                                highlightbackground=Colors[8],
                                highlightcolor=Colors[8],
                                highlightthicknes=2)
            Frame_Of_Action.place(x=-300,y=0,width=600,height=400)
            Frame_Of_Action.focus()
            global Move_Frame_Of_Midel
            def Move_Frame_Of_Midel():
                My_Widget.Resize_Widget(root,Frame_Of_Action,0,0,[600,400])
            Move_Frame_Of_Midel()
            ff=Frame(Frame_Of_Action,bg=Colors[1])
            ff.pack(fill=X)
            ff1=Frame(Frame_Of_Action,bg=Colors[1])
            ff1.pack(fill=X,padx=2)
            def command_b():
                Frame_Of_Action.focus()
                Frame_Of_Action.destroy()
            But_1=Button(ff,
                        text='〤',
                        font=('Microsoft YaHei UI Light',10),
                        bg=Colors[1],
                        fg=Colors[8],
                        bd=0,
                        command=command_b)
            But_1.pack(side=RIGHT,ipadx=4)
            def but_1_enter(event):
                But_1.config(bg=Colors[6])
            def but_1_leave(event):
                But_1.config(bg=Colors[1])
            But_1.bind('<Enter>',but_1_enter)
            But_1.bind('<Leave>',but_1_leave)
            Label(ff,text='Search',fg=Colors[2],bg=Colors[1],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
            TV_Frame2=Frame(Frame_Of_Action,bg=Colors[1])
            TV_Frame2.pack(fill=BOTH,expand=1)
            global The_Focus_value2
            The_Focus_value2=[]
            global column_names_list1
            column_names_list1=[]
            def get_searched(search=None):
                try:
                    for widget in TV_Frame2.winfo_children():
                        widget.destroy()
                    MyDatabase3=mysql.connector.connect(host=Host_Name.get(),
                                                        user=User_Name.get(),
                                                        password=User_Password.get(),
                                                        database=Database_Name)
                    cour=MyDatabase3.cursor()
                    cour.execute(f'describe {Table_Name}')
                    scroll_v=Scroll(TV_Frame2,button_bg=Colors[9],button_bg_active=Colors[8])
                    scroll_v.pack(side=RIGHT,fill=Y)
                    scroll_h=Scroll(TV_Frame2,orient='horizontal',button_bg=Colors[9],button_bg_active=Colors[8])
                    scroll_h.pack(side=BOTTOM,fill=X)
                    count :int
                    global column_names_list1
                    column_names_list1=[]
                    col_count=[]
                    count=0
                    for row in cour:
                        column_names_list1.append(row[0])
                        col_count.append(f'#{count}')
                        count+=1
                    cour.close()
                    TV1=ttk.Treeview(TV_Frame2,columns=(col_count))
                    TV1.configure(yscrollcommand=scroll_v.set,xscrollcommand=scroll_h.set)
                    scroll_v.configure(command=TV1.yview)
                    scroll_h.configure(command=TV1.xview)

                    TV1.pack(side=LEFT,fill=BOTH,expand=True)
                    for row in range(len(column_names_list1)):
                        TV1.heading(f'#{row}',text=column_names_list1[row])
                        TV1.column(f'#{row}',width=100)   
                    def Treeview_Menu2(event):
                        try:
                            row_id=TV1.identify_row(event.y)
                            TV1.selection_set(row_id)
                            row_values=TV1.item(row_id)
                            tt=[row_values['text']]
                            rr=tt+(row_values['values'])
                            rr.pop()
                            global The_Focus_value1
                            The_Focus_value1=rr
                            My_Widget.My_Menu(event,
                                            values=['Add','Update','Delete'],
                                            commands=[lambda:Add_Row(Database_Name,Table_Name),
                                                    lambda:Update_Row(Database_Name,Table_Name),
                                                    lambda:Delete_row_in_tible(Database_Name,Table_Name)])
                        except:pass
                    TV1.bind('<Button-3>',Treeview_Menu2)
                    def Get_Cursor(event):
                        try:
                            cursor_row=TV1.focus() 
                            contents=TV1.item(cursor_row)
                            tt=[contents['text']]
                            rr=tt+(contents['values'])
                            rr.pop()
                            global The_Focus_value2
                            The_Focus_value2=rr
                        except:pass
                    TV1.bind('<ButtonRelease-1>',Get_Cursor)
                    if search:
                        MyDatabase4=mysql.connector.connect(host=Host_Name.get(),
                                                    user=User_Name.get(),
                                                    password=User_Password.get(),
                                                    database=Database_Name)
                        cour01=MyDatabase4.cursor()
                        cour01.execute(f'select * from {Table_Name} where {search[0]} like \'{search[1]}\' ')
                        count=0
                        for row in cour01:
                            TV1.insert('','end',count,text=row[0])
                            for i in range(1,len(column_names_list1)):
                                TV1.set(count,f'#{i}',row[i])
                            count+=1
                        cour01.close()          
                except mysql.connector.Error as error:
                    My_Widget.Show_Message('Error',error)        
            get_searched()
            global searchfor
            searchfor=StringVar()
            def get_it():
                get_searched([searchfor.get(),entry_i.get()])
            fr=Frame(ff1,bg=Colors[1])
            fr.pack(side=LEFT,padx=5)
            bim2 = Round_Button(   master=fr,
                                    image=search_png,
                                    fg=Colors[2],
                                    width=100,
                                    text='  Search  ',
                                    font=('tajwal',13),
                                    outline=Colors[0],
                                    bg_active=Colors[0],
                                    command=get_it,
                                    ipadx=2,
                                    ipady=2)
            bim2.pack(side='left',expand=True,pady=1)
            entry_i=Entry(ff1,bg=Colors[0],fg=Colors[2],font=('tajwal',12))
            entry_i.pack(side=LEFT,pady=4,padx=4)
            lib=Label(ff1,text='search for',bg=Colors[6],fg=Colors[2])
            lib.pack(side=LEFT)
            def ent(event):
                lib.config(bg=Colors[0])
            def lev(event):
                lib.config(bg=Colors[6])
            try:
                searchfor.set(column_names_list1[0])
            except:pass
            def frame_ch(event):
                f5=Frame(root,bg=Colors[1],
                            highlightbackground=Colors[7],
                            highlightcolor=Colors[7],
                            highlightthicknes=1)
                f5.place(x=lib.winfo_x()+lib.winfo_width()+ff1.winfo_x()+Frame_Of_Action.winfo_x(),
                    y=lib.winfo_y()+ff1.winfo_y()+Frame_Of_Action.winfo_y())
                f5.focus() 
                def f_out():
                    f5.destroy()
                try:
                    global column_names_list1                    
                    for row in column_names_list1:
                        Checkbutton(f5,text=row,bg=Colors[1],fg=Colors[7],
                                onvalue=row,offvalue='',variable=searchfor,command=f_out).pack(anchor=NW)
                except:pass
                f5.bind('<FocusOut>',lambda e:f_out())
            lib.bind('<Enter>',ent)
            lib.bind('<Leave>',lev)
            lib.bind('<Button-1>',frame_ch)

        def Delete_row_in_tible(Database_Name,Table_Name):
            global The_Focus_value1
            if The_Focus_value1:
                try:
                    Database_D=mysql.connector.connect(host=Host_Name.get(),
                                                        user=User_Name.get(),
                                                        password=User_Password.get(),
                                                        database=Database_Name)
                    curs0=Database_D.cursor()
                    curs0.execute(f'describe {Table_Name}')
                    list_inw =[]
                    for row in curs0:
                        list_inw.append(row)
                    nomber=0
                    def Delete_Row(ask):
                        if ask == 'Yes':
                            curs2=Database_D.cursor()
                            curs2.execute(F'DELETE FROM {Table_Name} WHERE {list_inw[nomber][0]} =\'{The_Focus_value1[nomber]}\'')
                            Database_D.commit()
                            Show_Table_Info_In_Table()
                    while True:
                        try:
                            curs1=Database_D.cursor()
                            curs1.execute(f'select * from {Table_Name} where {list_inw[nomber][0]} like \'{The_Focus_value1[nomber]}\'')
                            list_select=[]
                            for row in curs1:
                                list_select.append(row)
                            if len(list_select) == 1:
                                My_Widget.Show_Message('Delete',
                                f'Are you sure you want to delete row {The_Focus_value1[0]}?',
                                Delete_Row)
                                break
                            if nomber == len(list_inw)-1:
                                My_Widget.Show_Message('Delete',
                                f'there is {len(list_inw)} rows {The_Focus_value1[0]} have the same data do you want to delete all of them inywhay?',Delete_Row)
                                break
                            nomber+=1
                        except mysql.connector.Error as error :
                            My_Widget.Show_Message('Error',error)
                            break
                except mysql.connector.Error as error:
                    My_Widget.Show_Message('Error',error)
            else:
                My_Widget.Show_Message('Worning','Plasse selecte the row')

        def Add_Row(Database_Name,Table_Name):
            global Frame_Of_Action
            try:
                Frame_Of_Action.destroy()
            except:pass
            Frame_Of_Action=Frame(root,
                                bg=Colors[1],
                                highlightbackground=Colors[8],
                                highlightcolor=Colors[8],
                                highlightthicknes=2)
            Frame_Of_Action.place(x=-300,y=0,width=400,height=308)
            Frame_Of_Action.focus()
            global Move_Frame_Of_Midel
            def Move_Frame_Of_Midel():
                My_Widget.Resize_Widget(root,Frame_Of_Action,0,0,[400,308])
            Move_Frame_Of_Midel()
            ff=Frame(Frame_Of_Action,bg=Colors[1])
            ff.pack(fill=X)
            ff1=Frame(Frame_Of_Action,bg=Colors[1])
            ff1.pack(side=BOTTOM,fill=X)
            fff1=Scrolled_Frame(Frame_Of_Action,
                                bg=Colors[1],
                                scroll_vertical=True,
                                scroll_button_bg=Colors[9],
                                scroll_button_active=Colors[8],
                                scroll_unit=40)
            fff1.pack(side=LEFT,fill=BOTH)
            def command_b():
                Frame_Of_Action.destroy()
            But_1=Button(ff,
                        text='〤',
                        font=('Microsoft YaHei UI Light',10),
                        bg=Colors[1],
                        fg=Colors[8],
                        bd=0,
                        command=command_b)
            But_1.pack(side=RIGHT,ipadx=4)
            def but_1_enter(event):
                But_1.config(bg=Colors[6])
            def but_1_leave(event):
                But_1.config(bg=Colors[1])
            But_1.bind('<Enter>',but_1_enter)
            But_1.bind('<Leave>',but_1_leave)
            Label(ff,text='Add Row',fg=Colors[2],bg=Colors[1],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
            
            the_columns=[]
            the_values=[]
            try:
                database_cr=mysql.connector.connect(host=Host_Name.get(),
                                                    user=User_Name.get(),
                                                    password=User_Password.get(),
                                                    database=Database_Name)
                cursor5=database_cr.cursor()
                cursor5.execute(f'describe {Table_Name}')
                y=10
                count_=0 
                h=40
                for row in cursor5:
                    the_v=StringVar()
                    er1=My_Widget.Entry_round(fff1,row[0],the_v,Colors[1])
                    er1.place(x=70,y=y)
                    the_columns.append(row[0])
                    the_values.append(the_v)
                    fff1.configure(height=h)
                    y+=40
                    count_+=1
                    h+=40
            except mysql.connector.Error as error:
                My_Widget.Show_Message('Error',error)

            def add_row():
                try:
                    database_=mysql.connector.connect(host=Host_Name.get(),
                                                        user=User_Name.get(),
                                                        password=User_Password.get(),
                                                        database=Database_Name)
                    cursor6=database_.cursor()
                    cols_var=''
                    vals_var=''
                    for i in range(len(the_columns)) :
                        if i == 0 :
                            cols_var+=f'{the_columns[i]}'
                            
                            if str(the_columns[i]) == str(the_values[i].get()):
                                vals_var+='\' \''
              
                            else:
                                vals_var+=f'\'{the_values[i].get()}\''
                   
                        else:
                            cols_var+=f',{the_columns[i]}'
                            
                            if str(the_columns[i]) == str(the_values[i].get()):
                                vals_var+=',\' \''
                        
                            else:
                                vals_var+=f',\'{the_values[i].get()}\''

                    cursor6.execute(f'INSERT INTO {Table_Name} ({cols_var}) VALUES ({vals_var})')
                    database_.commit()
                    Show_Table_Info_In_Table()
                    command_b()
                    My_Widget.Show_Message('insert',f'valuse inserted to {Table_Name} seccesfly')
                except mysql.connector.Error as error:
                    My_Widget.Show_Message('Error',error) 
            bim2 = Round_Button(   master=ff1,
                                    image=create,
                                    fg=Colors[2],
                                    width=100,
                                    text='   Save  ',
                                    font=('tajwal',13),
                                    outline=Colors[0],
                                    bg_active=Colors[0],
                                    command=add_row,
                                    ipadx=2,
                                    ipady=2)
            bim2.pack(side='left',expand=True,pady=1)

        def Update_Row(Database_Name,Table_Name):
            global Frame_Of_Action
            try:
                Frame_Of_Action.destroy()
            except:pass
            global The_Focus_value1
            if The_Focus_value1:
                Frame_Of_Action=Frame(root,
                                    bg=Colors[1],
                                    highlightbackground=Colors[8],
                                    highlightcolor=Colors[8],
                                    highlightthicknes=2)
                Frame_Of_Action.place(x=-300,y=0,width=400,height=308)
                Frame_Of_Action.focus()
                global Move_Frame_Of_Midel
                def Move_Frame_Of_Midel():
                    My_Widget.Resize_Widget(root,Frame_Of_Action,0,0,[400,308])
                Move_Frame_Of_Midel()
                ff=Frame(Frame_Of_Action,bg=Colors[1])
                ff.pack(fill=X)
                ff1=Frame(Frame_Of_Action,bg=Colors[1])
                ff1.pack(side=BOTTOM,fill=X)
                fff1=Scrolled_Frame(Frame_Of_Action,
                                bg=Colors[1],
                                scroll_vertical=True,
                                scroll_button_bg=Colors[9],
                                scroll_button_active=Colors[8],
                                scroll_unit=60)
                fff1.pack(side=LEFT,fill=BOTH)
                def command_b():
                    global The_Focus_value1
                    The_Focus_value1=[]
                    Frame_Of_Action.destroy()
                But_1=Button(ff,
                            text='〤',
                            font=('Microsoft YaHei UI Light',10),
                            bg=Colors[1],
                            fg=Colors[8],
                            bd=0,
                            command=command_b)
                But_1.pack(side=RIGHT,ipadx=4)
                def but_1_enter(event):
                    But_1.config(bg=Colors[6])
                def but_1_leave(event):
                    But_1.config(bg=Colors[1])
                But_1.bind('<Enter>',but_1_enter)
                But_1.bind('<Leave>',but_1_leave)
                Label(ff,text='Update Row',
                        fg=Colors[2],
                        bg=Colors[1],
                        font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
                
                the_columns=[]
                the_values=[]
                try:
                    database_cr=mysql.connector.connect(host=Host_Name.get(),
                                                        user=User_Name.get(),
                                                        password=User_Password.get(),
                                                        database=Database_Name)
                    cursor5=database_cr.cursor()
                    cursor5.execute(f'describe {Table_Name}')
                    y=10
                    count_=0 
                    for row in cursor5:
                        the_v=StringVar()
                        lb=Label(fff1,text=f'{row[0]} :',fg=Colors[7],bg=Colors[1],font=('tajwal',11))
                        lb.place(x=90,y=y)
                        the_v.set(The_Focus_value1[count_])
                        er1=My_Widget.Entry_round(fff1,'',the_v,Colors[1])
                        er1.place(x=80,y=y+20)
                        the_columns.append(row[0])
                        the_values.append(the_v)
                        fff1.config(height=y+50)
                        y+=60
                        count_+=1
                    
                except mysql.connector.Error as error:
                    My_Widget.Show_Message('Error',error)

                def add_row():
                    try:
                        database_=mysql.connector.connect(host=Host_Name.get(),
                                                            user=User_Name.get(),
                                                            password=User_Password.get(),
                                                            database=Database_Name)
                        cursor6=database_.cursor()
                        cols_var=''
                        vals_var=[]
                        for i in range(len(the_columns)) :
                            if i == 0 :
                                cols_var+=f'{the_columns[i]}=%s'
                                if str(the_columns[i]) == str(the_values[i].get()):
                                    vals_var.append('')
                                else:
                                    vals_var.append(the_values[i].get())
                            else:
                                cols_var+=f',{the_columns[i]}=%s'
                                if str(the_columns[i]) == str(the_values[i].get()):
                                    vals_var.append('')
                                else:
                                    vals_var.append(the_values[i].get())
                        vals_var.append(f'{The_Focus_value1[0]}')
                        v=f'UPDATE {Table_Name} SET {cols_var} WHERE {the_columns[0]}=%s '
                        cursor6.execute( v , vals_var )
                        database_.commit()
                        Show_Table_Info_In_Table()
                        command_b()
                        My_Widget.Show_Message('insert',
                            f'row {vals_var[-1]} updated seccesfly')
                    except mysql.connector.Error as error:
                        My_Widget.Show_Message('Error',error)
                bim2 = Round_Button(    master=ff1,
                                        image=create,
                                        fg=Colors[2],
                                        width=100,
                                        text='   Save  ',
                                        font=('tajwal',13),
                                        outline=Colors[0],
                                        bg_active=Colors[0],
                                        command=add_row,
                                        ipadx=2,
                                        ipady=2)
                bim2.pack(side='left',expand=True,pady=1)
            else:My_Widget.Show_Message('Error','Plasse selecte the column')

        def Delete_Column(Database_Name,Table_Name):
            try:
                Frame_Of_Action.destroy()
            except:pass
            the_varinw=The_Focus_value.get()
            def The_Inser(inser):
                if inser=='Yes':
                    Databb=mysql.connector.connect(host=Host_Name.get(),
                                                    user=User_Name.get(),
                                                    password=User_Password.get(),
                                                    database=Database_Name)
                    cor1=Databb.cursor()
                    cor1.execute(f'ALTER TABLE {Table_Name} DROP {the_varinw}')
                    The_Focus_value.set('')
                    Show_Table(Table_Name,Database_Name)
                else:
                    pass
            if the_varinw:
                My_Widget.Show_Message('Promtion',
                            f'Are you sure you want to delete column {the_varinw}?',
                            The_Inser)
            else:
                My_Widget.Show_Message('Error','Plasse selecte the column')

        def Delete_Database(Database_Name,Table_Name=None):
            try:
                if Table_Name:
                    my_Database=mysql.connector.connect(host=Host_Name.get(),
                                                        user=User_Name.get(),
                                                        password=User_Password.get(),
                                                        database=Database_Name)
                    cors=my_Database.cursor()
                    cors.execute(f'drop table {Table_Name}')
                    Database_Tabels_Command(Database_Name)
                    My_Widget.Show_Message('Delete',f'Table {Table_Name} is deleted')
                else:
                    my_Database=mysql.connector.connect(host=Host_Name.get(),
                                                        user=User_Name.get(),
                                                        password=User_Password.get())
                    cors=my_Database.cursor()
                    cors.execute(f'drop database {Database_Name}')
                    Connect_And_ChowTable()
                    My_Widget.Show_Message('Delete',f'Table {Database_Name} is deleted')
            except mysql.connector.Error as error:
                My_Widget.Show_Message('Error',error)
        
        def Frame_of_change_column(_database_1,Table__name1):
            global Frame_Of_Action
            try:
                Frame_Of_Action.destroy()
            except:pass
            v_focus_value=''
            try:
                global The_Focus_value
                v_focus_value=The_Focus_value.get()
            except:pass
            if v_focus_value:
                Frame_Of_Action=Frame(root,
                                    bg=Colors[6],
                                    highlightbackground=Colors[8],
                                    highlightcolor=Colors[8],
                                    highlightthicknes=2)
                Frame_Of_Action.place(x=-300,y=0,width=400,height=400)
                Frame_Of_Action.focus()
                global Move_Frame_Of_Midel
                def Move_Frame_Of_Midel():
                    My_Widget.Resize_Widget(root,Frame_Of_Action,0,0,[400,400])
                Move_Frame_Of_Midel()
                ff=Frame(Frame_Of_Action,bg=Colors[6])
                ff.pack(side=TOP,fill=X)
                ff1=Frame(Frame_Of_Action,bg=Colors[6])
                ff1.pack(side=TOP,fill=X)
                ff3=Frame(Frame_Of_Action,bg=Colors[6])
                ff3.pack(side=BOTTOM,fill=X)
                ff2=Frame(Frame_Of_Action,bg=Colors[0])
                ff2.pack(fill=BOTH,expand=True)
                def command_b():
                    Frame_Of_Action.destroy()
                But_1=Button(ff,
                            text='〤',
                            font=('Microsoft YaHei UI Light',10),
                            bg=Colors[6],
                            fg=Colors[8],
                            bd=0,
                            command=command_b)
                But_1.pack(side=RIGHT,ipadx=4)
                def but_1_enter(event):
                    But_1.config(bg=Colors[4])
                def but_1_leave(event):
                    But_1.config(bg=Colors[6])
                But_1.bind('<Enter>',but_1_enter)
                But_1.bind('<Leave>',but_1_leave)
                Label(ff,text='Add Column',fg=Colors[2],bg=Colors[6],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
                v1=StringVar()
                v2=StringVar()
                v3=StringVar()
                v4=StringVar()
                v5=StringVar()
                def get_values_of_col():
                    try:
                        database_var=mysql.connector.connect(host=Host_Name.get(),
                                                            user=User_Name.get(),
                                                            password=User_Password.get(),
                                                            database=_database_1)
                        cor=database_var.cursor()
                        cor.execute(f'describe {Table__name1}')
                        place_of_col=''
                        for row4 in cor:
                            if row4[0] == v_focus_value:
                                v1.set(row4[0])
                                li_0=[]
                                li_1=[]
                                if row4[1]:
                                    v=True
                                    for i in row4[1]:
                                        if v:
                                            if i != '(':
                                                li_0.append(i)
                                            else:
                                                v=False
                                        elif i != ')':
                                            li_1.append(i)
                                v2.set(''.join(li_0))
                                v3.set(''.join(li_1))
                                if row4[2]=='NO' :
                                    v4.set('NOT NULL')
                                else:
                                    v4.set('NULL')
                                if place_of_col:
                                    v5.set(f'After {place_of_col}')
                                else:
                                    v5.set('First')
                                if row4[3]=='PRI':
                                    v2.set('PRIMARY KEY')
                                if row4[5]=='auto_increment':
                                    v2.set('PRIMARY KEY AUTO_INCREMENT')
                            place_of_col=row4[0]
                    except mysql.connector.Error as error:
                        My_Widget.Show_Message('Error',error)
                get_values_of_col()
                def create_t(data_execute):
                    try:
                        database_cr_t=mysql.connector.connect(host=Host_Name.get(),
                                                            user=User_Name.get(),
                                                            password=User_Password.get(),
                                                            database=_database_1)
                        cursor=database_cr_t.cursor()
                        cursor.execute(data_execute)
                        Show_Table(Table__name1,_database_1)
                        Frame_Of_Action.destroy()
                        My_Widget.Show_Message('Create',f'column is changed seccesfly')
                    except mysql.connector.Error as error:
                        My_Widget.Show_Message('Error',error)
                def use_enters():
                    try:
                        for widget in ff2.winfo_children():
                            widget.destroy()
                    except:pass
                    BB1.config(bg=Colors[0])
                    BB2.config(bg=Colors[6])
                    Column_Name=StringVar()
                    Column_Type=StringVar()
                    Length=StringVar()
                    Defult=StringVar()
                    Column_Size=StringVar()
                    er1=My_Widget.Entry_round(ff2,'Column Name',Column_Name,Colors[0])
                    er1.place(80,30)
                    er2=My_Widget.Combobox_round(ff2,
                                                'Column Type',
                                                Column_Type,
                                                Colors[0],
                                                values=['INT','VARCHAR','TEXT','DATE','PRIMARY KEY','PRIMARY KEY AUTO_INCREMENT'])
                    er2.place(x=80,y=70)
                    er3=My_Widget.Combobox_round(ff2,
                                                'Length',
                                                Length,
                                                Colors[0],
                                                values=['11','100','200','500','1000','10000','100000'])
                    er3.place(x=80,y=110)
                    er4=My_Widget.Combobox_round(ff2,
                                                'Defult',
                                                Defult,
                                                Colors[0],
                                                values=['NULL','NOT NULL'])
                    er4.place(x=80,y=150)
                    er5=My_Widget.Combobox_round(ff2,
                                                'Size',
                                                Column_Size,
                                                Colors[0],)
                    er5.place(x=80,y=190)
                    def get_values():
                        Column_Name.set(v1.get())
                        Column_Type.set(v2.get())
                        Length.set(v3.get())
                        Defult.set(v4.get())
                        Column_Size.set(v5.get())
                    get_values()
                    def get_size_of_column():
                        try:
                            database_var=mysql.connector.connect(host=Host_Name.get(),
                                                                user=User_Name.get(),
                                                                password=User_Password.get(),
                                                                database=_database_1)
                            cor=database_var.cursor()
                            cor.execute(f'describe {Table__name1}')
                            column_list=['First']
                            for row in cor:
                                column_list.append(f'After {row[0]}')
                            er5.config(values=column_list)
                        except mysql.connector.Error as error:
                            My_Widget.Show_Message('Error',error)
                    get_size_of_column()
                    def get_text_execute():
                        infovar1=Column_Name.get()
                        if infovar1 =='Column Name':
                            infovar1 =''
                        infovar2=Column_Type.get()
                        if infovar2 =='Column Type':
                            infovar2 =''
                        infovar3=Length.get()
                        if infovar3 and infovar3!='Length':
                            infovar3=f'({infovar3})'
                        else:
                            infovar3=''
                        infovar4=Defult.get()
                        if infovar4 =='Defult':
                            infovar4 =''
                        infovar5=Column_Size.get()
                        if infovar5 =='Size':
                            infovar5 =''
                        if infovar2 == 'DATE':
                            infovar3=''
                        if infovar2 in ['PRIMARY KEY','PRIMARY KEY AUTO_INCREMENT']:
                            infovar3=f'INT{infovar3}'
                            return f'ALTER TABLE {Table__name1} CHANGE {v_focus_value} {infovar1} {infovar3} {infovar2} {infovar4} {infovar5}'
                        else:
                            return f'ALTER TABLE {Table__name1} CHANGE {v_focus_value} {infovar1} {infovar2} {infovar3} {infovar4} {infovar5}'
                    def send_execute_info():
                        create_t(get_text_execute())
                    def get_text():
                        use_text(get_text_execute())
                    try:
                        for widget in ff3.winfo_children():
                            widget.destroy()
                    except:pass
                    bim2 = Round_Button(    master=ff3,
                                            image=create,
                                            fg=Colors[2],
                                            width=100,
                                            text='  Create ',
                                            font=('tajwal',13),
                                            outline=Colors[0],
                                            bg_active=Colors[0],
                                            command=send_execute_info,
                                            ipadx=2,
                                            ipady=2)
                    bim2.pack(side='left',expand=True,pady=1)

                    bim3 = Round_Button(    master=ff3,
                                            image=text_png,
                                            fg=Colors[2],
                                            width=100,
                                            text=' SQL Text',
                                            font=('tajwal',13),
                                            outline=Colors[0],
                                            bg_active=Colors[0],
                                            command=get_text,
                                            ipadx=2,
                                            ipady=2)
                    bim3.pack(side='left',expand=True,pady=1)
                def use_text(text=None):
                    try:
                        for widget in ff2.winfo_children():
                            widget.destroy()
                    except:pass
                    BB2.config(bg=Colors[0])
                    BB1.config(bg=Colors[6])
                    Label(ff2,fg=Colors[2],bg=Colors[0],text='SQL Text :').place(x=40,y=20)
                    text_entry=Text(ff2,
                                    fg=Colors[3],
                                    bg=Colors[0],
                                    highlightthicknes=1,
                                    highlightbackground=Colors[7],
                                    highlightcolor=Colors[7],
                                    bd=0,
                                    font=('Microsoft YaHei UI Light',12),
                                    width=35,
                                    height=11)
                    text_entry.place(x=40,y=50)
                    if text :
                        text_entry.insert(END,text)
                    else:
                        def get_text_execute():
                            infovar1=v1.get()
                            infovar2=v2.get()
                            infovar3=v3.get()
                            if infovar3 :
                                infovar3=f'({infovar3})'
                            infovar4=v4.get()
                            infovar5=v5.get()
                            if infovar2 == 'DATE':
                                infovar3=''
                            if infovar2 in ['PRIMARY KEY','PRIMARY KEY AUTO_INCREMENT']:
                                infovar3=f'INT{infovar3}'
                                return f'ALTER TABLE {Table__name1} CHANGE {v_focus_value} {infovar1} {infovar3} {infovar2} {infovar4} {infovar5}'
                            else:
                                return f'ALTER TABLE {Table__name1} CHANGE {v_focus_value} {infovar1} {infovar2} {infovar3} {infovar4} {infovar5}'
                        vvc=get_text_execute()
                        text_entry.insert(END,vvc)
                    def send_text_execute_info():
                        create_t(text_entry.get(0.1,END))
                    try:
                        for widget1 in ff3.winfo_children():
                            widget1.destroy()
                    except:pass
                    bim2 = Round_Button(    master=ff3,
                                            image=create,
                                            fg=Colors[2],
                                            width=100,
                                            text='  Create ',
                                            font=('tajwal',13),
                                            outline=Colors[0],
                                            bg_active=Colors[0],
                                            command=send_text_execute_info,
                                            ipadx=2,
                                            ipady=2)
                    bim2.pack(side='left',expand=True,pady=1)
                BB1=Label(ff1,
                            bg=Colors[6],
                            fg=Colors[2],
                            text='Default',
                            font=('Microsoft YaHei UI Light',10,'bold'))
                BB1.pack(side=LEFT,fill=X,expand=1)
                BB2=Label(ff1,
                            bg=Colors[6],
                            fg=Colors[2],
                            text='Use Text',
                            font=('Microsoft YaHei UI Light',10,'bold'))
                BB2.pack(side=RIGHT,fill=X,expand=1)
                def ChangeColor(button):
                    button.config(cursor='hand2',fg=Colors[7])
                def ResetColor(button):
                    button.config(cursor='',fg=Colors[2])
                BB1.bind('<Enter>',lambda e: ChangeColor(BB1))
                BB2.bind('<Enter>',lambda e: ChangeColor(BB2))
                BB1.bind('<Leave>',lambda e: ResetColor(BB1))
                BB2.bind('<Leave>',lambda e: ResetColor(BB2))
                BB1.bind('<ButtonRelease-1>',lambda e:use_enters())
                BB2.bind('<ButtonRelease-1>',lambda e:use_text())
                use_enters()
                The_Focus_value.set('')
            else:
                My_Widget.Show_Message('','Plasse selecte row first')

        def Frame_Of_Add_Column(Database_Name,Table_Name):
            global Frame_Of_Action
            try:
                Frame_Of_Action.destroy()
            except:pass
            Frame_Of_Action=Frame(root,
                                bg=Colors[6],
                                highlightbackground=Colors[8],
                                highlightcolor=Colors[8],
                                highlightthicknes=2)
            Frame_Of_Action.place(x=-300,y=0,width=400,height=400)
            Frame_Of_Action.focus()
            global Move_Frame_Of_Midel
            def Move_Frame_Of_Midel():
                My_Widget.Resize_Widget(root,Frame_Of_Action,0,0,[400,400])
            Move_Frame_Of_Midel()
            ff=Frame(Frame_Of_Action,bg=Colors[6])
            ff.pack(side=TOP,fill=X)
            ff1=Frame(Frame_Of_Action,bg=Colors[6])
            ff1.pack(side=TOP,fill=X)
            ff3=Frame(Frame_Of_Action,bg=Colors[6])
            ff3.pack(side=BOTTOM,fill=X)
            ff2=Frame(Frame_Of_Action,bg=Colors[0])
            ff2.pack(fill=BOTH,expand=True)
            def command_b():
                Frame_Of_Action.destroy()
            But_1=Button(ff,
                        text='〤',
                        font=('Microsoft YaHei UI Light',10),
                        bg=Colors[6],
                        fg=Colors[8],
                        bd=0,
                        command=command_b)
            But_1.pack(side=RIGHT,ipadx=4)
            def but_1_enter(event):
                But_1.config(bg=Colors[4])
            def but_1_leave(event):
                But_1.config(bg=Colors[6])
            But_1.bind('<Enter>',but_1_enter)
            But_1.bind('<Leave>',but_1_leave)
            Label(ff,text='Add Column',fg=Colors[2],bg=Colors[6],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
            def create_t(data_execute):
                try:
                    database_cr_t=mysql.connector.connect(host=Host_Name.get(),
                                                        user=User_Name.get(),
                                                        password=User_Password.get(),
                                                        database=Database_Name)
                    cursor=database_cr_t.cursor()
                    cursor.execute(data_execute)
                    Show_Table(Table_Name,Database_Name)
                    Frame_Of_Action.destroy()
                    My_Widget.Show_Message('Create',f'column is created seccesfly')
                except mysql.connector.Error as error:
                    My_Widget.Show_Message('Error',error)
            def use_enters():
                try:
                    for widget in ff2.winfo_children():
                        widget.destroy()
                except:pass
                BB1.config(bg=Colors[0])
                BB2.config(bg=Colors[6])
                Column_Name=StringVar()
                Column_Type=StringVar()
                Length=StringVar()
                Defult=StringVar()
                Column_Size=StringVar()
                er1=My_Widget.Entry_round(ff2,'Column Name',Column_Name,Colors[0])
                er1.place(80,30)
                er2=My_Widget.Combobox_round(ff2,
                                                    'Column Type',
                                                    Column_Type,Colors[0],
                                                    values=['INT','VARCHAR','TEXT','DATE','PRIMARY KEY','PRIMARY KEY AUTO_INCREMENT'])
                er2.place(x=80,y=70)
                er3=My_Widget.Combobox_round(ff2,
                                                    'Length',
                                                    Length,Colors[0],
                                                    values=['11','100','200','500','1000','10000','100000'])
                er3.place(x=80,y=110)
                er4=My_Widget.Combobox_round(ff2,
                                                    'Defult',
                                                    Defult,Colors[0],
                                                    values=['NULL','NOT NULL'])
                er4.place(x=80,y=150)
                er5=My_Widget.Combobox_round(ff2,
                                                    'Size',
                                                    Column_Size,Colors[0],
                                                    )
                er5.place(x=80,y=190)
                def get_size_of_column():
                    try:
                        database_var=mysql.connector.connect(host=Host_Name.get(),
                                                            user=User_Name.get(),
                                                            password=User_Password.get(),
                                                            database=Database_Name)
                        cor=database_var.cursor()
                        cor.execute(f'describe {Table_Name}')
                        column_list=['First']
                        for row in cor:
                            column_list.append(f'After {row[0]}')
                        er5.config(values=column_list)
                    except mysql.connector.Error as error:
                        My_Widget.Show_Message('Error',error)
                get_size_of_column()

                def get_text_execute():
                    infovar1=Column_Name.get()
                    if infovar1 =='Column Name':
                        infovar1 =''
                    infovar2=Column_Type.get()
                    if infovar2 =='Column Type':
                        infovar2 =''
                    infovar3=Length.get()
                    if infovar3 and infovar3!='Length':
                        infovar3=f'({infovar3})'
                    else:
                        infovar3=''
                    infovar4=Defult.get()
                    if infovar4 =='Defult':
                        infovar4 =''
                    infovar5=Column_Size.get()
                    if infovar5 =='Size':
                        infovar5 =''
                    if infovar2 == 'DATE':
                        infovar3=''
                    if infovar2 in ['PRIMARY KEY','PRIMARY KEY AUTO_INCREMENT']:
                        infovar3=f'INT{infovar3}'
                        return f'ALTER TABLE {Table_Name} ADD {infovar1} {infovar3} {infovar2} {infovar4} {infovar5}'
                    else:
                        return f'ALTER TABLE {Table_Name} ADD {infovar1} {infovar2} {infovar3} {infovar4} {infovar5}'
                def send_execute_info():
                    create_t(get_text_execute())
                def get_text():
                    use_text(get_text_execute())
                try:
                    for widget in ff3.winfo_children():
                        widget.destroy()
                except:pass
                bim2 = Round_Button(    master=ff3,
                                        image=create,
                                        fg=Colors[2],
                                        width=100,
                                        text='   Create  ',
                                        font=('tajwal',13),
                                        outline=Colors[0],
                                        bg_active=Colors[0],
                                        command=send_execute_info,
                                        ipadx=2,
                                        ipady=2)
                bim2.pack(side='left',expand=True,pady=1)
                bim2 = Round_Button(    master=ff3,
                                        image=text_png,
                                        fg=Colors[2],
                                        width=100,
                                        text=' SQL Text ',
                                        font=('tajwal',13),
                                        outline=Colors[0],
                                        bg_active=Colors[0],
                                        command=get_text,
                                        ipadx=2,
                                        ipady=2)
                bim2.pack(side='left',expand=True,pady=1)

            def use_text(text=None):
                try:
                    for widget in ff2.winfo_children():
                        widget.destroy()
                except:pass
                BB2.config(bg=Colors[0])
                BB1.config(bg=Colors[6])
                Label(ff2,fg=Colors[2],bg=Colors[0],text='SQL Text :').place(x=40,y=20)
                text_entry=Text(ff2,
                                fg=Colors[3],
                                bg=Colors[0],
                                highlightthicknes=1,
                                highlightbackground=Colors[7],
                                highlightcolor=Colors[7],
                                bd=0,
                                font=('Microsoft YaHei UI Light',12),
                                width=35,
                                height=11)
                text_entry.place(x=40,y=50)
                if text :
                    text_entry.insert(END,text)
                else:
                    text_entry.insert(END,f'ALTER TABLE {Table_Name} ')

                def send_text_execute_info():
                    create_t(text_entry.get(0.1,END))
                try:
                    for widget1 in ff3.winfo_children():
                        widget1.destroy()
                except:pass
                bim2 = Round_Button(    master=ff3,
                                        image=create,
                                        fg=Colors[2],
                                        width=100,
                                        text='   Create  ',
                                        font=('tajwal',13),
                                        outline=Colors[0],
                                        bg_active=Colors[0],
                                        command=send_text_execute_info,
                                        ipadx=2,
                                        ipady=2)
                bim2.pack(side='left',expand=True,pady=1)
            BB1=Label(ff1,
                        bg=Colors[6],
                        fg=Colors[2],
                        text='Default',
                        font=('Microsoft YaHei UI Light',10,'bold'))
            BB1.pack(side=LEFT,fill=X,expand=1)
            BB2=Label(ff1,
                        bg=Colors[6],
                        fg=Colors[2],
                        text='Use Text',
                        font=('Microsoft YaHei UI Light',10,'bold'))
            BB2.pack(side=RIGHT,fill=X,expand=1)
            def ChangeColor(button):
                button.config(cursor='hand2',fg=Colors[7])
            def ResetColor(button):
                button.config(cursor='',fg=Colors[2])
            BB1.bind('<Enter>',lambda e: ChangeColor(BB1))
            BB2.bind('<Enter>',lambda e: ChangeColor(BB2))
            BB1.bind('<Leave>',lambda e: ResetColor(BB1))
            BB2.bind('<Leave>',lambda e: ResetColor(BB2))
            BB1.bind('<ButtonRelease-1>',lambda e:use_enters())
            BB2.bind('<ButtonRelease-1>',lambda e:use_text())
            use_enters()

        def Frame_of_Create_Table(Database_Name):
            global Frame_Of_Action
            try:
                Frame_Of_Action.destroy()
            except:pass
            Frame_Of_Action=Frame(root,
                                bg=Colors[6],
                                highlightbackground=Colors[8],
                                highlightcolor=Colors[8],
                                highlightthicknes=2)
            Frame_Of_Action.place(x=-300,y=0,width=400,height=400)
            Frame_Of_Action.focus()
            global Move_Frame_Of_Midel
            def Move_Frame_Of_Midel():
                My_Widget.Resize_Widget(root,Frame_Of_Action,0,0,[400,400])
            Move_Frame_Of_Midel()
            ff=Frame(Frame_Of_Action,bg=Colors[6])
            ff.pack(side=TOP,fill=X)
            ff1=Frame(Frame_Of_Action,bg=Colors[6])
            ff1.pack(side=TOP,fill=X)
            ff3=Frame(Frame_Of_Action,bg=Colors[6])
            ff3.pack(side=BOTTOM,fill=X)
            ff2=Frame(Frame_Of_Action,bg=Colors[0])
            ff2.pack(fill=BOTH,expand=True)
            def command_b():
                Frame_Of_Action.destroy()
            But_1=Button(ff,
                        text='〤',
                        font=('Microsoft YaHei UI Light',10),
                        bg=Colors[6],
                        fg=Colors[8],
                        bd=0,
                        command=command_b)
            But_1.pack(side=RIGHT,ipadx=4)
            def but_1_enter(event):
                But_1.config(bg=Colors[4])
            def but_1_leave(event):
                But_1.config(bg=Colors[6])
            But_1.bind('<Enter>',but_1_enter)
            But_1.bind('<Leave>',but_1_leave)
            Label(ff,text='Create Table',fg=Colors[2],bg=Colors[6],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
            def create_t(data_execute):
                try:
                    database_cr_t=mysql.connector.connect(host=Host_Name.get(),
                                                        user=User_Name.get(),
                                                        password=User_Password.get(),
                                                        database=Database_Name)
                    cursor=database_cr_t.cursor()
                    cursor.execute(data_execute)
                    Database_Tabels_Command(Database_Name)
                    Frame_Of_Action.destroy()
                    My_Widget.Show_Message('Create','Table is created seccesfly')
                except mysql.connector.Error as error:
                    My_Widget.Show_Message('Error',error)
            def use_enters():
                try:
                    for widget in ff2.winfo_children():
                        widget.destroy()
                except:pass
                BB1.config(bg=Colors[0])
                BB2.config(bg=Colors[6])
                Table_Name=StringVar()
                Column_Name=StringVar()
                Column_Type=StringVar()
                Length=StringVar()
                Defult=StringVar()
                er1=My_Widget.Entry_round(ff2,'Table Name',Table_Name,Colors[0])
                er1.place(80,30)
                er2=My_Widget.Entry_round(ff2,'Column Name',Column_Name,Colors[0])
                er2.place(80,70)
                er3=My_Widget.Combobox_round(ff2,
                                                'Column Type',
                                                Column_Type,Colors[0],
                                                values=['INT','VARCHAR','TEXT','DATE','PRIMARY KEY','PRIMARY KEY AUTO_INCREMENT'])
                er3.place(x=80,y=110)
                er4=My_Widget.Combobox_round(ff2,
                                                'Length',
                                                Length,Colors[0],
                                                values=['11','100','200','500','1000','10000','100000'])
                er4.place(x=80,y=150)
                er5=My_Widget.Combobox_round(ff2,
                                                'Defult',
                                                Defult,Colors[0],
                                                values=['NULL','NOT NULL'])
                er5.place(x=80,y=190)  
                def get_text_execute():
                    infovar1=Table_Name.get()
                    if infovar1 =='Table Name':
                        infovar1 =''
                    infovar2=Column_Name.get()
                    if infovar2 =='Column Name':
                        infovar2 =''
                    infovar3=Column_Type.get()
                    if infovar3 =='Column Type':
                        infovar3 =''
                    infovar4=Length.get()
                    if infovar4 and infovar4!='Length':
                        infovar4=f'({infovar4})'
                    else:
                        infovar4=''  
                    infovar5=Defult.get()
                    if infovar5 =='Defult':
                        infovar5 =''
                    if infovar3 == 'DATE':
                        infovar4=''
                    if infovar3 in ['PRIMARY KEY','PRIMARY KEY AUTO_INCREMENT']:
                        infovar4=f'INT{infovar4}'
                        return f'CREATE TABLE {infovar1} ({infovar2} {infovar4} {infovar3} {infovar5})'
                    else:
                        return f'CREATE TABLE {infovar1} ( {infovar2} {infovar3} {infovar4} {infovar5})'
                def send_execute_info():
                    create_t(get_text_execute())
                def get_text():
                    use_text(get_text_execute())
                try:
                    for widget in ff3.winfo_children():
                        widget.destroy()
                except:pass
                bim2 = Round_Button(    master=ff3,
                                        image=create,
                                        fg=Colors[2],
                                        width=100,
                                        text='   Create  ',
                                        font=('tajwal',13),
                                        outline=Colors[0],
                                        bg_active=Colors[0],
                                        command=send_execute_info,
                                        ipadx=2,
                                        ipady=2)
                bim2.pack(side='left',expand=True,pady=1)
                bim2 = Round_Button(    master=ff3,
                                        image=text_png,
                                        fg=Colors[2],
                                        width=100,
                                        text=' SQL Text ',
                                        font=('tajwal',13),
                                        outline=Colors[0],
                                        bg_active=Colors[0],
                                        command=get_text,
                                        ipadx=2,
                                        ipady=2)
                bim2.pack(side='left',expand=True,pady=1)
            def use_text(text=None):
                try:
                    for widget in ff2.winfo_children():
                        widget.destroy()
                except:pass

                BB2.config(bg=Colors[0])
                BB1.config(bg=Colors[6])
                Label(ff2,fg=Colors[2],bg=Colors[0],text='SQL Text :').place(x=40,y=20)
                text_entry=Text(ff2,
                                fg=Colors[3],
                                bg=Colors[0],
                                highlightthicknes=1,
                                highlightbackground=Colors[7],
                                highlightcolor=Colors[7],
                                bd=0,
                                font=('Microsoft YaHei UI Light',12),
                                width=35,
                                height=11)
                text_entry.place(x=40,y=50)
                if text :
                    text_entry.insert(END,text)
                def send_text_execute_info():
                    create_t(text_entry.get(0.1,END))
                try:
                    for widget1 in ff3.winfo_children():
                        widget1.destroy()
                except:pass
                bim2 = Round_Button(    master=ff3,
                                        image=create,
                                        fg=Colors[2],
                                        width=100,
                                        text='  Create  ',
                                        font=('tajwal',13),
                                        outline=Colors[0],
                                        bg_active=Colors[0],
                                        command=send_text_execute_info,
                                        ipadx=2,
                                        ipady=2)
                bim2.pack(side='left',expand=True,pady=1)
            BB1=Label(ff1,
                        bg=Colors[6],
                        fg=Colors[2],
                        text='Default',
                        font=('Microsoft YaHei UI Light',10,'bold'))
            BB1.pack(side=LEFT,fill=X,expand=1)
            BB2=Label(ff1,
                        bg=Colors[6],
                        fg=Colors[2],
                        text='Use Text',
                        font=('Microsoft YaHei UI Light',10,'bold'))
            BB2.pack(side=RIGHT,fill=X,expand=1)
            def ChangeColor(button):
                button.config(cursor='hand2',fg=Colors[7])
            def ResetColor(button):
                button.config(cursor='',fg=Colors[2])
            BB1.bind('<Enter>',lambda e: ChangeColor(BB1))
            BB2.bind('<Enter>',lambda e: ChangeColor(BB2))
            BB1.bind('<Leave>',lambda e: ResetColor(BB1))
            BB2.bind('<Leave>',lambda e: ResetColor(BB2))
            BB1.bind('<ButtonRelease-1>',lambda e:use_enters())
            BB2.bind('<ButtonRelease-1>',lambda e:use_text())
            use_enters()

        def Frame_of_Drop_tabel(Database_Name):
            global Frame_Of_Action
            try:
                Frame_Of_Action.destroy()
            except:pass
            Frame_Of_Action=Frame(root,
                                bg=Colors[6],
                                highlightbackground=Colors[8],
                                highlightcolor=Colors[8],
                                highlightthicknes=2)
            Frame_Of_Action.place(x=-300,y=0,width=400,height=300)
            Frame_Of_Action.focus()
            global Move_Frame_Of_Midel
            def Move_Frame_Of_Midel():
                My_Widget.Resize_Widget(root,Frame_Of_Action,0,0,[400,300])
            Move_Frame_Of_Midel()
            ff=Frame(Frame_Of_Action,bg=Colors[1])
            ff.pack(side=TOP,fill=X)
            ff1=Frame(Frame_Of_Action,bg=Colors[1])
            ff1.pack(side=TOP,fill=X)
            ff3=Frame(Frame_Of_Action,bg=Colors[1])
            ff3.pack(side=BOTTOM,fill=X)
            ff2=Frame(Frame_Of_Action,bg=Colors[1])
            ff2.pack(fill=BOTH,expand=True)
            def command_b():
                Frame_Of_Action.destroy()
            But_1=Button(ff,
                        text='〤',
                        font=('Microsoft YaHei UI Light',10),
                        bg=Colors[1],
                        fg=Colors[8],
                        bd=0,
                        command=command_b)
            But_1.pack(side=RIGHT,ipadx=4)
            def but_1_enter(event):
                But_1.config(bg=Colors[4])
            def but_1_leave(event):
                But_1.config(bg=Colors[1])
            But_1.bind('<Enter>',but_1_enter)
            But_1.bind('<Leave>',but_1_leave)
            Label(ff,text='Drop Table',fg=Colors[2],bg=Colors[1],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)

            drop_table_var=StringVar()
            combobox_var=My_Widget.Combobox_round(where=ff2,
                                        message='Table Name',
                                        thevariable=drop_table_var,
                                        bg=Colors[1])
            combobox_var.place(x=80,y=70)
            def drop_table():
                try:
                    data_var1=mysql.connector.connect(host=Host_Name.get(),
                                                    user=User_Name.get(),
                                                    password=User_Password.get(),
                                                    database=Database_Name)
                    corsor1=data_var1.cursor()
                    corsor1.execute(f'drop table {drop_table_var.get()}')
                    Database_Tabels_Command(Database_Name)
                    command_b()
                    My_Widget.Show_Message('Delete',f'Table {drop_table_var.get()} is droped seccesfly')
                except mysql.connector.Error as error:
                    My_Widget.Show_Message('Error', error )

            bim2 = Round_Button(    master=ff3,
                                    image=drop_png,
                                    fg=Colors[2],
                                    width=100,
                                    text='  Drop  ',
                                    font=('tajwal',13),
                                    outline=Colors[0],
                                    bg_active=Colors[0],
                                    command=drop_table,
                                    ipadx=2,
                                    ipady=2)
            bim2.pack(side='left',expand=True,pady=1)

            def try_get_tables():
                data_var=mysql.connector.connect(host=Host_Name.get(),
                                                user=User_Name.get(),
                                                password=User_Password.get(),
                                                database=Database_Name)
                corsor=data_var.cursor()
                corsor.execute('show tables')
                list_tables=[]
                for i in corsor:
                    list_tables.append(i)
                combobox_var.config(values=list_tables)
            try_get_tables()

        def Show_Table(table,Database_Name):
            Fr4.pack(side=LEFT,fill=BOTH,padx=1,pady=1,expand=True)
            for widget in Fr4.winfo_children():
                widget.destroy()
            title_frame2=Frame(Fr4,bd=1,bg=Colors[4])
            title_frame2.pack(side=TOP,fill=X)
            title_label2=Label(title_frame2,
                                text=table,
                                font=('Century Schoolbook',12,'bold italic'),
                                bg=Colors[4],
                                fg=Colors[7])
            title_label2.pack()
            Table_Frame=Frame(Fr4,bg=Colors[6])
            Table_Frame.pack(fill=BOTH)
            container_wedget2=['']
            global Show_Col_Info_In_Table
            def Show_Col_Info_In_Table():
                global The_Focus_value
                The_Focus_value.set('')
                try:
                    global TV
                    try:
                        TV.destroy()
                    except:pass
                    BB1.config(fg=Colors[7])
                    BB2.config(fg=Colors[2])
                    MyDatabase2=mysql.connector.connect(host=Host_Name.get(),
                                                        user=User_Name.get(),
                                                        password=User_Password.get(),
                                                        database=Database_Name)
                    cursor2=MyDatabase2.cursor()
                    cursor2.execute(f' describe {table}')
                    for row in Fr7.winfo_children():
                        row.destroy()
                    Fr8=Frame(Fr7,bg=Colors[6])
                    Fr8.pack(side=BOTTOM,fill=BOTH)
                    But_1 = Round_Button(    master=Fr8,
                                            image=add_png,
                                            fg=Colors[2],
                                            width=100,
                                            text='     Add   ',
                                            font=('tajwal',13),
                                            outline=Colors[0],
                                            bg_active=Colors[0],
                                            command=lambda:Frame_Of_Add_Column(Database_Name,table),
                                            ipadx=2,
                                            ipady=2)
                    But_1.pack(side='left',expand=True,pady=1)
                    But_2 = Round_Button(    master=Fr8,
                                            image=change_png,
                                            fg=Colors[2],
                                            width=100,
                                            text='  Change ',
                                            font=('tajwal',13),
                                            outline=Colors[0],
                                            bg_active=Colors[0],
                                            command=lambda:Frame_of_change_column(Database_Name,table),
                                            ipadx=2,
                                            ipady=2)
                    But_2.pack(side='left',expand=True,pady=1)
                    But_3 = Round_Button(    master=Fr8,
                                            image=drop_png,
                                            fg=Colors[2],
                                            width=100,
                                            text='    Delete  ',
                                            font=('tajwal',13),
                                            outline=Colors[0],
                                            bg_active=Colors[0],
                                            command=lambda :Delete_Column(Database_Name,table),
                                            ipadx=2,
                                            ipady=2)
                    But_3.pack(side='left',expand=True,pady=1)
                    TV=ttk.Treeview(TV_Frame,columns=('#0','#1','#2','#3','#4','#5','#6'))
                    scroll_vertical.configure(command=TV.yview)
                    TV.configure(yscrollcommand=scroll_vertical.set)
                    scroll_horizontal.configure(command=TV.xview)
                    TV.configure(xscrollcommand=scroll_horizontal.set)
                    TV.tag_configure('odd',background='green')
                    TV.pack(side=LEFT,fill=BOTH)
                    TV.heading('#0',text='ID')
                    TV.heading('#1',text='Name')
                    TV.heading('#2',text='Type')
                    TV.heading('#3',text='Null')
                    TV.heading('#4',text='Index key')
                    TV.heading('#5',text='Default')
                    TV.heading('#6',text='Extra')
                    TV.column('#0',width=100)
                    TV.column('#1',width=100)
                    TV.column('#2',width=100)
                    TV.column('#3',width=100)
                    TV.column('#4',width=100)
                    TV.column('#5',width=100)
                    TV.column('#6',width=100)
                    def Treeview_Menu1(event):
                        try:
                            row_id=TV.identify_row(event.y)
                            TV.selection_set(row_id)
                            contents=TV.item(row_id)
                            val=contents['values']
                            The_Focus_value.set(val[0])
                            My_Widget.My_Menu(event,
                                            values=['Refresh','Add','Change','Drop'],
                                            commands=[Show_Col_Info_In_Table,
                                                    lambda:Frame_Of_Add_Column(Database_Name,table),
                                                    lambda:Frame_of_change_column(Database_Name,table),
                                                    lambda:Delete_Column(Database_Name,table)])
                        except:pass
                    TV.bind('<Button-3>',Treeview_Menu1)
                    def Get_Cursor(event):
                        try:
                            cursor_row=TV.focus() 
                            contents=TV.item(cursor_row)
                            rr=contents['values']
                            The_Focus_value.set(rr[0])
                        except:pass
                    TV.bind('<ButtonRelease-1>',Get_Cursor)
                    count=1
                    for row in cursor2:
                        TV.insert('',END,count,text=count)
                        TV.set(count,'#1',row[0])
                        TV.set(count,'#2',row[1])
                        TV.set(count,'#3',row[2])
                        TV.set(count,'#4',row[3])
                        TV.set(count,'#5',row[4])
                        TV.set(count,'#6',row[5])
                        if row[4] == None:
                            TV.set(count,'#5','None')
                        count+=1
                    cursor2.close()
                    def widget_1(colors):
                        BB1.config(fg=colors[7])
                        But_1.configure(fg=colors[2],outline=colors[0],bg_active=colors[0],image=add_png)
                        But_2.configure(fg=colors[2],outline=colors[0],bg_active=colors[0],image=change_png)
                        But_3.configure(fg=colors[2],outline=colors[0],bg_active=colors[0],image=drop_png)
                        Fr8.config(bg=colors[6])
                    container_wedget2[0]=widget_1
                except mysql.connector.Error as error:
                    My_Widget.Show_Message('Error',error)
            global Show_Table_Info_In_Table
            def Show_Table_Info_In_Table():
                global The_Focus_value1
                The_Focus_value1=[]
                try:
                    global TV
                    try:
                        TV.destroy()
                    except:pass
                    BB2.config(fg=Colors[7])
                    BB1.config(fg=Colors[2])
                    MyDatabase3=mysql.connector.connect(host=Host_Name.get(),
                                                        user=User_Name.get(),
                                                        password=User_Password.get(),
                                                        database=Database_Name)
                    cour=MyDatabase3.cursor()
                    cour.execute(f'describe {table}')
                    for row in Fr7.winfo_children():
                        row.destroy()
                    Fr8=Frame(Fr7,bg=Colors[6])
                    Fr8.pack(side=BOTTOM,fill=BOTH)
                    But_1 = Round_Button(    master=Fr8,
                                            image=add_png,
                                            fg=Colors[2],
                                            width=100,
                                            text='     Add   ',
                                            font=('tajwal',13),
                                            outline=Colors[0],
                                            bg_active=Colors[0],
                                            command=lambda:Add_Row(Database_Name,table),
                                            ipadx=2,
                                            ipady=2)
                    But_1.pack(side='left',expand=True,pady=1)
                    But_2 = Round_Button(   master=Fr8,
                                            image=update_png,
                                            fg=Colors[2],
                                            width=100,
                                            text='   Update ',
                                            font=('tajwal',13),
                                            outline=Colors[0],
                                            bg_active=Colors[0],
                                            command=lambda:Update_Row(Database_Name,table),
                                            ipadx=2,
                                            ipady=2)
                    But_2.pack(side='left',expand=True,pady=1)
                    But_3 = Round_Button(   master=Fr8,
                                            image=drop_png,
                                            fg=Colors[2],
                                            width=100,
                                            text='   Delete ',
                                            font=('tajwal',13),
                                            outline=Colors[0],
                                            bg_active=Colors[0],
                                            command=lambda:Delete_row_in_tible(Database_Name,table),
                                            ipadx=2,
                                            ipady=2)
                    But_3.pack(side='left',expand=True,pady=1)
                    But_4 = Round_Button(   master=Fr8,
                                            image=search_png,
                                            fg=Colors[2],
                                            width=100,
                                            text='  Search  ',
                                            font=('tajwal',13),
                                            outline=Colors[0],
                                            bg_active=Colors[0],
                                            command=lambda:Search(Database_Name,table),
                                            ipadx=2,
                                            ipady=2)
                    But_4.pack(side='left',expand=True,pady=1)
                    count :int
                    column_names_list=[]
                    col_count=[]
                    count=0
                    for row in cour:
                        column_names_list.append(row[0])
                        col_count.append(f'#{count}')
                        count+=1
                    cour.close()
                    cursor3=MyDatabase3.cursor()
                    cursor3.execute(f'select * from {table}')
                    TV=ttk.Treeview(TV_Frame,columns=(col_count))
                    scroll_vertical.configure(command=TV.yview)
                    TV.configure(yscrollcommand=scroll_vertical.set)
                    scroll_horizontal.configure(command=TV.xview)
                    TV.configure(xscrollcommand=scroll_horizontal.set)
                    TV.pack(side=LEFT,fill=BOTH,expand=True)
                    for row in range(len(column_names_list)):
                        TV.heading(f'#{row}',text=column_names_list[row])
                        TV.column(f'#{row}',width=100) 
                    
                    def Treeview_Menu2(event):
                        try:
                            row_id=TV.identify_row(event.y)
                            TV.selection_set(row_id)
                            row_values=TV.item(row_id)
                            tt=[row_values['text']]
                            rr=tt+(row_values['values'])
                            rr.pop()
                            global The_Focus_value1
                            The_Focus_value1=rr
                            My_Widget.My_Menu(event,
                                            values=['Refresh','Add','Update','Delete','Search'],
                                            commands=[Show_Table_Info_In_Table,
                                                        lambda:Add_Row(Database_Name,table),
                                                        lambda:Update_Row(Database_Name,table),
                                                        lambda:Delete_row_in_tible(Database_Name,table),
                                                        lambda:Search(Database_Name,table)])
                        except:pass
                    TV.bind('<Button-3>',Treeview_Menu2)
                    def Get_Cursor(event):
                        try:
                            cursor_row=TV.focus() 
                            contents=TV.item(cursor_row)
                            tt=[contents['text']]
                            rr=tt+(contents['values'])
                            rr.pop()
                            global The_Focus_value1
                            The_Focus_value1=rr
                        except:pass
                    TV.bind('<ButtonRelease-1>',Get_Cursor)
                    count=0
                    for row in cursor3:
                        TV.insert('','end',count,text=row[0])
                        for i in range(1,len(column_names_list)):
                            TV.set(count,f'#{i}',row[i])
                        count+=1
                    cursor3.close()
                    def widget_2(colors):
                        BB2.config(fg=colors[7])
                        Fr8.config(bg=colors[6])
                        But_1.configure(fg=colors[2],outline=colors[0],bg_active=colors[0],image=add_png)
                        But_2.config(fg=colors[2],outline=colors[0],bg_active=colors[0],image=update_png)
                        But_3.config(fg=colors[2],outline=colors[0],bg_active=colors[0],image=drop_png)
                        But_4.config(fg=colors[2],outline=colors[0],bg_active=colors[0],image=search_png)
                    container_wedget2[0]=widget_2          
                except mysql.connector.Error as error:
                    My_Widget.Show_Message('Error',error)
            BB1=Label(Table_Frame,
                        bg=Colors[6],
                        fg=Colors[2],
                        text='Columns Table',
                        font=('Consolas',12))
            BB1.pack(side=RIGHT,fill=X,expand=1)
            BB2=Label(Table_Frame,
                        bg=Colors[6],
                        fg=Colors[2],
                        text='Table information',
                        font=('Consolas',12))
            BB2.pack(side=LEFT,fill=X,expand=1)
            TV_Frame=Frame(Fr4,bd=0,bg=Colors[6])
            TV_Frame.pack(side=BOTTOM,fill=BOTH,expand=True)
            Fr7=Frame(TV_Frame,bg=Colors[6])
            Fr7.pack(side=BOTTOM,fill=BOTH,padx=1,pady=1)
            scroll_vertical=Scroll(master=TV_Frame,
                                            button_bg=Colors[9],
                                            button_bg_active=Colors[8])
            scroll_vertical.pack(side='right',fill='y')
            scroll_horizontal=Scroll(master=TV_Frame,
                                            orient='horizontal',
                                            button_bg=Colors[9],
                                            button_bg_active=Colors[8])
            scroll_horizontal.pack(side='bottom',fill='x')
            Show_Table_Info_In_Table()
            BB1.bind('<ButtonRelease-1>',lambda e:Show_Col_Info_In_Table())
            BB2.bind('<ButtonRelease-1>',lambda e:Show_Table_Info_In_Table())
            BB1.bind('<Enter>',lambda e: BB1.config(bg=Colors[0]))
            BB2.bind('<Enter>',lambda e: BB2.config(bg=Colors[0]))
            BB1.bind('<Leave>',lambda e: BB1.config(bg=Colors[6]))
            BB2.bind('<Leave>',lambda e: BB2.config(bg=Colors[6]))
            def Change_Colors4(colors):
                Fr4.config(bg=colors[6],
                            highlightcolor=colors[9],
                            highlightbackground=colors[9])
                title_frame2.config(bg=colors[4])
                title_label2.config(bg=colors[4],fg=colors[7])
                Table_Frame.config(bg=colors[6])
                BB1.config(bg=colors[6],fg=colors[2])
                BB2.config(bg=colors[6],fg=colors[2])
                TV_Frame.config(bg=colors[6])
                scroll_vertical.config(button_bg=colors[9],button_bg_active=colors[8])
                scroll_horizontal.config(button_bg=colors[9],button_bg_active=colors[8])
                container_wedget2[0](colors)
                Fr7.config(bg=colors[6])
            Container_Configer_Color[4]=Change_Colors4

        def Database_Tabels_Command(open_Database):
            try:
                Fr3.pack(side=LEFT,fill=Y,padx=1,pady=1)
                try:
                    for widget in Fr2.winfo_children():
                        widget.destroy()
                except:pass
                MyDatabase1=mysql.connector.connect(host=Host_Name.get(),
                                                    user=User_Name.get(),
                                                    password=User_Password.get(),
                                                    database=open_Database)
                cursor1=MyDatabase1.cursor()
                cursor1.execute('show tables')
                #-------------------------------
                title_label1.config(text=f'{open_Database} Tables')
                but1.configure(command=lambda:Frame_of_Create_Table(open_Database))
                but2.configure(command=lambda:Frame_of_Drop_tabel(open_Database))

                def My_menu_(event,database,table):
                    My_Widget.My_Menu(event,
                                        values=['New table','Delete table','Open table'],
                                        commands=[lambda:Frame_of_Create_Table(database),
                                                lambda:Delete_Database(database,table),
                                                lambda:Show_Table(table,database)])
                container_wedget1=[]
                for row1 in cursor1:
                    but_2=My_Widget.My_Button(place= Fr2 ,
                                        Text= row1[0] ,
                                        command= Show_Table ,
                                        Database_name=open_Database ,
                                        right_command=My_menu_)
                    container_wedget1.append(but_2.config)
                cursor1.close()
                def Change_Colors3(colors):
                    Fr3.config(bg=colors[6],highlightcolor=colors[9],highlightbackground=colors[9])
                    title_label1.config(bg=colors[4],fg=colors[7])
                    Fr2.config(bg=colors[6],scroll_button_bg=colors[9],scroll_button_active=colors[8])
                    but1.config(fg=colors[2],outline=colors[0],bg_active=colors[0],image=create)
                    but2.config(fg=colors[2],outline=colors[0],bg_active=colors[0],image=drop_png)
                    Fr2_1.config(bg=colors[6])
                    
                    for b in container_wedget1:
                        b(bg=colors[6],fg=colors[2],highlightbackground=colors[5])
                Container_Configer_Color[3]=Change_Colors3
            except mysql.connector.Error as error:
                My_Widget.Show_Message('Error',error)
        
        global Frame_of_Create_Database
        def Frame_of_Create_Database():
            global Frame_Of_Action
            try:
                Frame_Of_Action.destroy()
            except:pass
            Frame_Of_Action=Frame(root,
                                bg=Colors[1],
                                highlightbackground=Colors[8],
                                highlightcolor=Colors[8],
                                highlightthicknes=2)
            Frame_Of_Action.place(x=-300,y=0,width=400,height=300)
            Frame_Of_Action.focus()
            global Move_Frame_Of_Midel
            def Move_Frame_Of_Midel():
                My_Widget.Resize_Widget(root,Frame_Of_Action,0,0,[400,300])
            Move_Frame_Of_Midel()
            ff=Frame(Frame_Of_Action,bg=Colors[1])
            ff.pack(side=TOP,fill=X)
            def command_b():
                Frame_Of_Action.destroy()
            But_1=Button(ff,
                        text='〤',
                        font=('Microsoft YaHei UI Light',10),
                        bg=Colors[1],
                        fg=Colors[8],
                        bd=0,
                        command=command_b)
            But_1.pack(side=RIGHT,ipadx=4)
            def but_1_enter(event):
                But_1.config(bg=Colors[6])
            def but_1_leave(event):
                But_1.config(bg=Colors[1])
            But_1.bind('<Enter>',but_1_enter)
            But_1.bind('<Leave>',but_1_leave)
            Label(ff,text='Create Database',fg=Colors[2],bg=Colors[1],font=('Microsoft YaHei UI Light',16,'bold')).pack(expand=1)
            create_database_var=StringVar()
            er1=My_Widget.Entry_round(Frame_Of_Action,'Database Name',create_database_var,Colors[1])
            er1.place(80,100)
            ff1=Frame(Frame_Of_Action,bg=Colors[1])
            ff1.pack(side=BOTTOM,fill=X)
            def create_d():
                try:
                    database_cr=mysql.connector.connect(host=Host_Name.get(),
                                                        user=User_Name.get(),
                                                        password=User_Password.get())
                    cursor=database_cr.cursor()
                    cursor.execute(f'create database {create_database_var.get()}')
                    Frame_Of_Action.destroy()
                    Connect_And_ChowTable()
                    My_Widget.Show_Message('Create',f'Database {create_database_var.get()} created seccesfly')
                except mysql.connector.Error as error:
                    My_Widget.Show_Message('Error',error)
            but1 = Round_Button(    master=ff1,
                                    image=create,
                                    fg=Colors[2],
                                    width=100,
                                    text='  Create  ',
                                    font=('tajwal',13),
                                    outline=Colors[0],
                                    bg_active=Colors[0],
                                    command=create_d,
                                    ipadx=2,
                                    ipady=2)
            but1.pack(side='left',expand=True,padx=1,pady=1)

        def Connect_And_ChowTable():
            for windget in frame_with.winfo_children():
                windget.destroy()
            but11.configure(command=Frame_of_Create_Database)
            container_wedget=[]
            def My_menu_1(event,database):
                My_Widget.My_Menu(event,
                                values=['New database','Delete database','Open database'],
                                commands=[Frame_of_Create_Database,
                                        lambda:Delete_Database(database),
                                        lambda:Database_Tabels_Command(database)])
            try:
                MyDatabase=mysql.connector.connect( host=Host_Name.get(),
                                                    user=User_Name.get(),
                                                    password=User_Password.get())
                cursor=MyDatabase.cursor()
                cursor.execute('show Databases')
                container_wedget=[]
                for row in cursor:
                    database_button=My_Widget.My_Button(place= frame_with , 
                                        Text= row[0] , 
                                        command= Database_Tabels_Command ,
                                        right_command=My_menu_1)
                    container_wedget.append(database_button.config)
                cursor.close()
            except mysql.connector.Error as error:
                My_Widget.Show_Message('Error',error)
            
            def Change_Colors2(colors):
                but11.configure(fg=colors[2],image=create,outline=colors[0],bg_active=colors[0])
                but21.configure(fg=colors[2],outline=colors[0],bg_active=colors[0])
                Fr_one.config(bg=colors[6],highlightcolor=colors[9],highlightbackground=colors[9])
                Fr3.config(bg=colors[6],highlightcolor=colors[9],highlightbackground=colors[9])
                Fr4.config(bg=colors[6],highlightcolor=colors[9],highlightbackground=colors[9])
                title_label.config(bg=colors[4],fg=colors[7])
                Fr21.config(bg=colors[6])
                frame_with.config(bg=colors[6],scroll_button_bg=colors[9],scroll_button_active=colors[8])
                for b in container_wedget:
                    b(bg=colors[6],fg=colors[2],highlightbackground=colors[5])
                try:
                    Frame_Of_Action.destroy()
                except:pass
            Container_Configer_Color[2]=Change_Colors2
        Connect_And_ChowTable()

    def check_connect(message=None):
        try:
            if User_Password.get() == "Password":
                User_Password.set('')
            MyDatabase=mysql.connector.connect( host=Host_Name.get(),
                                                user=User_Name.get(),
                                                password=User_Password.get())
            cursor=MyDatabase.cursor()    
            for widget in Frame_2.winfo_children():
                widget.destroy()
            connect_server()
            global fr_connect , title2 , title3
            fr_connect=Frame(title_frame,bg=Colors[1])
            fr_connect.pack(side=LEFT,padx=6)
            title2 = Label(fr_connect, 
                                text='=',
                                bd=0, 
                                bg=Colors[1],
                                fg='green',
                                font=('Webdings',10))
            title2.pack(side=LEFT)
            title3 = Label(fr_connect, 
                                text=f'{Host_Name.get()}',
                                bd=0, 
                                bg=Colors[1],
                                fg=Colors[2])
            title3.pack(side=LEFT)

            if message:
                messagebox.showinfo('Connected','Database Server connnected secsesfly')
        except mysql.connector.Error as error:
            Home_Page()
            root.after(50,move_widget)
            messagebox.showerror('Error',error)
    
    def DB_connect(check_mes=None):
        Host_Name.set(er0.get())
        User_Name.set(er1.get())
        User_Password.set(er2.get())
        
        Host_Name.set('localhost')
        User_Name.set('root')
        User_Password.set('')

        for widget in Frame_2.winfo_children():
            widget.destroy()
        My_Widget.White_for_working_onit(Frame_2) 
        if check_mes:
            root.after(1000,lambda:check_connect(True))
        else:
            root.after(1000,check_connect)
    Home_Page()

    def Change_Colors0(colors):
        try:
            get_images()
        except:pass
        root.config(bg=colors[1])
        title_bar.config(bg=colors[1])
        title_frame.config(bg=colors[1])
        Frame_1.config(bg=colors[6])
        Fra.config(bg=colors[9])
        Frame_2.config(bg=colors[6])
        close_button.config(bg=colors[1],fg=colors[2])
        expand_button.config(bg=colors[1],fg=colors[2])
        minimize_button.config(bg=colors[1],fg=colors[2])
        title_bar_title.config(bg=colors[1])
        title_bar_title1.config(bg=colors[1],fg=colors[2])
        menu_1.config(bg=colors[1],fg=colors[2])
        menu_2.config(bg=colors[1],fg=colors[2])
        menu_3.config(bg=colors[1],fg=colors[2])
        menu_4.config(bg=colors[1],fg=colors[2])
        l1.config(bg=colors[6])
        l2.config(bg=colors[6])
        l3.config(bg=colors[6])
        resizex_widget.config(bg=colors[6])
        resizey_widget.config(bg=colors[6])
        Frame_focus_click.config(bg=colors[6])
        st=ttk.Style()
        st.theme_use('default')
        st.configure('Treeview',
                    background=colors[6],
                    fieldbackground=colors[6],
                    foreground=colors[2])
        st.configure('Treeview.Heading',
                    background=colors[6],
                    foreground=colors[7],
                    relief=FLAT,
                    font=('tajwal',9,'bold'))
        st.map('Treeview',background=[('selected',colors[0])],foreground=[('selected',colors[2])])
        st.map('Treeview.Heading',background=[('active',colors[0])])
        try:
            global fr_connect , title2 , title3
            fr_connect.config(bg=colors[1])
            title2.config(bg=colors[1])
            title3.config(bg=colors[1],fg=colors[2])
        except:pass
    Container_Configer_Color[0]=Change_Colors0

    global move_widget
    def move_widget():
        try:
           resize_entrys() 
        except:pass
        try:
            move_button_focus()
        except:pass
        try:
            Move_Frame_Of_Midel()
        except:pass

    def Up_window():
        def pack_all():
            title_bar.pack(fill=X)
            resizex_widget.pack(side=RIGHT,fill=Y)
            resizey_widget.pack(side=BOTTOM,fill=X)   
            Frame_1.pack(side=LEFT,fill=Y)
            Fra.pack(side=LEFT,fill=Y)
            Frame_2.pack(side=LEFT,fill=BOTH,expand=True)
            root.after(80,move_widget)
        def get_up(w,h):
            root.geometry(Size_midel(w,h))   
        root.after(20,lambda:get_up(800,450))
        root.after(30,lambda:get_up(900,500))
        root.after(40,lambda:get_up(1000,520))
        root.after(50,lambda:get_up(1080,540))
        root.after(60,lambda:get_up(1120,560))
        root.after(70,lambda:get_up(1140,570))
        root.after(80,lambda:get_up(1160,580))
        root.after(90,lambda:get_up(1180,590))
        root.after(100,lambda:get_up(1186,592))
        root.after(110,lambda:get_up(1192,594))
        root.after(120,lambda:get_up(1196,596))
        root.after(130,lambda:get_up(1200,608))
        root.after(200,pack_all)
    Up_window()

if __name__ == "__main__" :
    root.mainloop()
