#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.5
#  in conjunction with Tcl version 8.6
#    Oct 27, 2020 01:20:33 PM +1100  platform: Windows NT

import sys
from image_processing import *
from tkinter import filedialog
from PIL import ImageTk,Image
from filemanagement import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import GUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

# ===============================================
# change image based on the slider value
def slider_show_image(value):
    top = GUI_support.w
    top.image_file_state.set_current_img_num(int(value) - 1)
    top.image_label.configure(image=top.image_file_state.get_current_img())
# ===============================================

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        # top.geometry("1083x802+330+136")
        top.geometry("1500x660")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(False,  False)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.028, rely=0.15, relheight=0.818, relwidth=0.753)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        # self.Menu = tk.Button(top)
        # self.Menu.place(relx=0.028, rely=0.025, height=34, width=77)
        # self.Menu.configure(activebackground="#ececec")
        # self.Menu.configure(activeforeground="#000000")
        # self.Menu.configure(background="#000000")
        # self.Menu.configure(disabledforeground="#a3a3a3")
        # self.Menu.configure(font="-family {Segoe UI} -size 9 -weight bold")
        # self.Menu.configure(foreground="#ffffff")
        # self.Menu.configure(highlightbackground="#d9d9d9")
        # self.Menu.configure(highlightcolor="black")
        # self.Menu.configure(pady="0")
        # self.Menu.configure(text='''Menu''')


        self.Slider = tk.Scale(top, from_=0.0, to=100.0)
        self.Slider.place(relx=0.222, rely=0.025, relwidth=0.175, relheight=0.0
                , height=42, bordermode='ignore')
        self.Slider.configure(activebackground="#ececec")
        self.Slider.configure(background="#d9d9d9")
        self.Slider.configure(command=slider_show_image)    # do image showing
        self.Slider.configure(cursor="fleur")
        self.Slider.configure(foreground="#000000")
        self.Slider.configure(highlightbackground="#d9d9d9")
        self.Slider.configure(highlightcolor="black")
        self.Slider.configure(orient="horizontal")
        self.Slider.configure(troughcolor="#d9d9d9")

        # image show =================================
        self.image_file_state = ImageFileState()
        self.image_label = tk.Label(top)
        self.image_label.place(relx=0.028, rely=0.15, relheight=0.818, relwidth=0.753)
        # =============================================

        # menu =======================================
        self.menubar = tk.Menu(top)
        # create a pulldown menu, and add it to the menu bar
        self.filemenu = Menu(self.menubar, tearoff=0)

        self.filemenu.add_command(label="Upload Images", command = lambda: upload_images(self.Slider, self.image_label, self.image_file_state))
        self.filemenu.add_command(label="Upload weight, name and config files as a zip", command=lambda: upload_config_files(self.image_file_state))
        self.filemenu.add_command(label="export", command=lambda: export_file())

        self.menubar.add_cascade(label="Menu", menu=self.filemenu)

        top.config(menu=self.menubar)
        # =============================================

        self.Left_Arrow = tk.Button(top)
        self.Left_Arrow.place(relx=0.259, rely=0.087, height=34, width=47)
        self.Left_Arrow.configure(activebackground="#ececec")
        self.Left_Arrow.configure(activeforeground="#000000")
        self.Left_Arrow.configure(background="#000000")
        self.Left_Arrow.configure(command=lambda: prev_image(self.Slider, self.image_label, self.image_file_state))    # prev image
        self.Left_Arrow.configure(disabledforeground="#a3a3a3")
        self.Left_Arrow.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Left_Arrow.configure(foreground="#ffffff")
        self.Left_Arrow.configure(highlightbackground="#d9d9d9")
        self.Left_Arrow.configure(highlightcolor="black")
        self.Left_Arrow.configure(pady="0")
        self.Left_Arrow.configure(text='''<''')

        self.Right_Arrow = tk.Button(top)
        self.Right_Arrow.place(relx=0.314, rely=0.087, height=34, width=47)
        self.Right_Arrow.configure(activebackground="#ececec")
        self.Right_Arrow.configure(activeforeground="#000000")
        self.Right_Arrow.configure(background="#000000")
        self.Right_Arrow.configure(command=lambda: next_image(self.Slider, self.image_label, self.image_file_state))   # next image
        self.Right_Arrow.configure(disabledforeground="#a3a3a3")
        self.Right_Arrow.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Right_Arrow.configure(foreground="#ffffff")
        self.Right_Arrow.configure(highlightbackground="#d9d9d9")
        self.Right_Arrow.configure(highlightcolor="black")
        self.Right_Arrow.configure(pady="0")
        self.Right_Arrow.configure(text='''>''')


        # self.Frame2 = tk.Frame(top)
        # self.Frame2.place(relx=0.803, rely=0.15, relheight=0.358, relwidth=0.169)

        # self.Frame2.configure(relief='groove')
        # self.Frame2.configure(borderwidth="2")
        # self.Frame2.configure(relief="groove")
        # self.Frame2.configure(background="#ffffff")
        # self.Frame2.configure(highlightbackground="#d9d9d9")
        # self.Frame2.configure(highlightcolor="black")

        self.Output = tk.Text(top)
        self.Output.place(relx=0.803, rely=0.20, relheight=0.358, relwidth=0.169)
        self.Output.configure(background="white")
        self.Output.configure(font="TkTextFont")
        self.Output.configure(foreground="black")
        self.Output.configure(highlightbackground="#d9d9d9")
        self.Output.configure(highlightcolor="black")
        self.Output.configure(insertbackground="black")
        self.Output.configure(relief="flat")
        self.Output.configure(selectbackground="blue")
        self.Output.configure(selectforeground="white")
        self.Output.configure(wrap="word")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.803, rely=0.15, height=32, relwidth=0.169)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#808080")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Output''')

        self.Run = tk.Button(top)
        self.Run.place(relx=0.12, rely=0.025, height=34, width=77)
        self.Run.configure(activebackground="#ececec")
        self.Run.configure(activeforeground="#000000")
        self.Run.configure(background="#000000")
        self.Run.configure(command = lambda: image_detect(self.image_file_state)) # Detecting the images
        self.Run.configure(cursor="fleur")
        self.Run.configure(disabledforeground="#a3a3a3")
        self.Run.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Run.configure(foreground="#ffffff")
        self.Run.configure(highlightbackground="#d9d9d9")
        self.Run.configure(highlightcolor="black")
        self.Run.configure(pady="0")
        self.Run.configure(text='''Label''')

if __name__ == '__main__':
    vp_start_gui()





