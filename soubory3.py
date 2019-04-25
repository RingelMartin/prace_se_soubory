# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:50:52 2019

@author: martin412
"""
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd

#Funkce pro otevírání souboru
def Open():
    
    text.delete(1.0,END)
    route=fd.askopenfilename(title="Otevřit soubor")
    try:
        file=open(route,"r")
        for line in file:
            text.insert(END,line)
        file.close()
    except:
        pass

#Funkce pro ukládání
def Save():
    
    f=fd.asksaveasfile(title="Uložit soubor",defaultextension="txt")
    try:
        textf = str(text.get(1.0, END))
        f.write(textf)
        f.close()
    except:
        pass


#Funkce pro ukončení aplikace
def Kill():
    
    x=mb.askyesno("Exit","Chcete odejít?")
    if x:
        main.destroy()
 

#Funkce pro velká písmena
def Capitalise():
    
    a=text.get(1.0,END)
    a=a.upper()
    
    text.delete(1.0,END)
    text.insert(1.0,a)
   
#funkce pro otevření okna Nahrazení znaku
def Replace():
    
    global origin
    global replacement
    global replacementwindow
    
    replacementwindow=Toplevel()
    replacementwindow.title("Replace character")
    
    t1=Label(replacementwindow,text="Replace character: ")
    t1.pack(pady=3)
    
    origin=Entry(replacementwindow)
    origin.pack(pady=3)
    
    t2=Label(replacementwindow,text="With this: ")
    t2.pack(pady=3)
    
    replacement=Entry(replacementwindow)
    replacement.pack(pady=3)
    
    execute=Button(replacementwindow,command=Rewrite,text="Do it!",width=10)
    execute.pack(pady=3)
    
def Rewrite():
    var = text.get(1.0,END)
    var = str.replace(var, origin.get(), replacement.get())
    text.delete(1.0,END)
    text.insert(1.0,var)
    
def Statistics():
    pass
        

main=Tk()

abeceda=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#Vzhled aplikace
text=Text(main,font="Arial10")
text.pack()

#hlavní lišta
hornimenu=Menu(main)
#tlačítko FILE
menusoubor=Menu(hornimenu,tearoff=0)

hornimenu.add_cascade(label="Soubor",menu=menusoubor)

menusoubor.add_command(label="Otevřit soubor",command=Open)

menusoubor.add_command(label="Uložit soubor",command=Save)

menusoubor.add_separator()

menusoubor.add_command(label="Odejít",command=Kill)

#tlačítko EDIT
menuoperace=Menu(hornimenu,tearoff=0)

hornimenu.add_cascade(label="Úpravy",menu=menuoperace)

menuoperace.add_command(label="Zvětšit písmena",command=Capitalise)

menuoperace.add_command(label="Nahradit",command=Replace)

menuoperace.add_command(label="Statistics(access denied)",command=Statistics)

menuoperace.add_command(label="Generate text(access denied)")


main.config(menu=hornimenu)



main.mainloop()