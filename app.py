import tkinter as tk
import main as mn

from tkinter.filedialog import askopenfilename
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkImage
from tkinter import *
from PIL import Image

root= CTk()
c_negro = '#010101'
c_morado='#7f5af0'
c_verde='#2cb67d'
c_blancoHueso='#F9F5F5'
c_negroBajo='#343434'

##funciones
def inicio():
    mn.run()
    root.withdraw()


root.geometry('580x600+450+20')
root.minsize(580,600)
root.config(bg=c_negro)
root.title("Inicio de sesión")


frame = CTkFrame(root, fg_color=c_negro, corner_radius=12)
frame.grid(column=0, row = 0, sticky = 'nsew', padx = 50, pady= 50)

frame.columnconfigure([0,1], weight=1)
frame.rowconfigure([0,1,2], weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
logoP=CTkImage(light_image=Image.open("assets/img/logo.png"),
                                  dark_image=Image.open("assets/img/logo.png"),
                                  size=(500, 500))
#logo= PhotoImage(file='logo.png')
logo2= PhotoImage(file='logo2.png')


CTkLabel(frame, text="", image=logoP).grid(columnspan=2, row=0)

#BOTÓN INCIO
bt_iniciar= CTkButton(frame, text="Empezar a escanear",border_color=c_verde,fg_color=c_negro,
                      hover_color=c_verde,corner_radius=12, border_width=2,width=50,height=40, command=inicio)

bt_iniciar.grid( columnspan=2, row=4, pady=4,padx=4)

#NUEVA VENTA

root.call('wm','iconphoto', root._w, logo2)
root.mainloop()

