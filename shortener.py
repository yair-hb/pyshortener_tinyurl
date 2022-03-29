import pyperclip 
import webbrowser
import pyshorteners
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ventana = Tk()
ventana.minsize(400,360)
ventana.title('Acotador de Enlaces by Yair-hb')
ventana.resizable(0,0)

s = pyshorteners.Shortener()

def acortamiento ():
    acortado = s.tinyurl.short(acortar_entry.get())
    resultado_label = Label(ventana, text=acortado)
    resultado_label.grid(row=8, column=0)
    resultado_label.config(fg='black', bg='#8ac9db', font=('Arial, 20'),padx=210, pady=20)

    boton = Button(ventana, text='Abrir enlace', command=abrir_enlace, font=13)
    boton.grid (row=9, column=0, pady=5)

    boton = Button(ventana, text="Copiar Enlace", command=copiar_enlace, font=13)
    boton.grid (row=10, column=0, pady=5)

def abrir_enlace():
    resp = messagebox.askyesno(message='Quieres abrir el navegador?', title='Deseas salir?')
    if resp == True:
        webbrowser.open(s.tinyurl.short(acortar_entry.get()))

def copiar_enlace():
    pyperclip.copy(s.tinyurl.short(acortar_entry.get()))
    messagebox.showinfo(message='Enlace copiado!', title='Copiado!')

def link():
    webbrowser.open('https://github.com/yair-hb')

home_label = Label(ventana, text='Acortador de enlaces')
home_label.config(fg='white', bg='#2166fa', font=('Arial', 30),padx=210, pady=20)
home_label.grid(row=0,column=0)

acortar_label = Label(ventana, text='¿Qué quieres acortar?', bg='#339eff', font='15')
acortar_entry = Entry(ventana)
acortar_label.grid(row=1, column=0, padx=5, pady=5)
acortar_entry.grid(row=2, column=0, padx=5, pady=5)
acortar_entry.config(fg='blue', bg='#d1d8df', font='Calibri, 20')

boton = Button(ventana, text='¡Acorta!', command=acortamiento, font=('15'))
boton.grid(row=6, column=0)

boton2 = Button(ventana, text='Github', command=link, font=(5), fg='red')
boton2.grid(row=7, column=0, padx=5, pady=5)

ventana.config(bg='#339eff')
ventana.mainloop()
