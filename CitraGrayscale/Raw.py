from cProfile import label
from cgitb import text
from ctypes.wintypes import RGB
from hashlib import new
from tkinter import *
from PIL import Image
import PIL.Image
from PIL import ImageTk
import tkinter.filedialog
from array import *
from pathlib import Path
from tkinter import simpledialog


from numpy import pad

root = Tk()
root.title("Aplikasi Image Enchanment")
root.configure(background='#242424')
root.geometry("1000x800")
    
    
def pixel(pics):
    global arr 
    
    x = 0
    y = 0
    arr = []
    
    for i in range(w):
        for j in range(h):
            rvalue = pics.getpixel((x,y))[0]
            gvalue = pics.getpixel((x,y))[1]
            bvalue = pics.getpixel((x,y))[2]
            arr.append([x, y, rvalue, gvalue, bvalue])
            j += 1
            y += 1
        x += 1
        i += 1
        y = 0
        j = 0   

def open_file():
    global arr, w, h
    
    file_path = tkinter.filedialog.askopenfilename()
    pics = (PIL.Image.open(file_path))
    pics = pics.convert('RGB')
    sizing = pics.resize((204,204))
    
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 0, column= 1, padx= 2, pady= 2)
    
    w, h = pics.size
    
    pixel(pics)
    
def grayscale ():
    global rvalue, gvalue, bvalue
    size = w, h
        
    pics2 = PIL.Image.new('RGB', size)
    load = pics2.load()

    for cr in arr:
        x, y, rvalue, gvalue, bvalue = cr   
        gray = (rvalue + gvalue +bvalue)//3
        load[x,y] = (gray, gray, gray)
        
    sizing2 = pics2.resize((204,204))
    photo2 = PIL.ImageTk.PhotoImage(sizing2)
    my_label2 = Label(image=photo2)
    my_label2.image = photo2
    my_label2.grid(row= 0, column= 2, padx= 2, pady= 2)
    
def bradj():
    global gray
    
    size = w, h
    
    userinput = simpledialog.askinteger(title="Input", prompt="input")
        
    pics3 = PIL.Image.new('RGB', size)
    load = pics3.load()
    
    for cr in arr:
        x, y, gray, gray, gray = cr   

        adj = gray + userinput

        load[x,y] = (adj, adj, adj)
        # print(x, y, userinput, gray, adj)
    
    sizing3 = pics3.resize((204,204))
    photo3 = PIL.ImageTk.PhotoImage(sizing3)
    my_label3 = Label(image=photo3)
    my_label3.image = photo3
    my_label3.grid(row= 0, column= 3)
    
def negation():
    size = w, h
        
    pics4 = PIL.Image.new('RGB', size)
    load = pics4.load()

    for cr in arr:
        x, y, gray, gray, gray = cr   
        ngtn = 255 - gray
        load[x,y] = (ngtn, ngtn, ngtn)
    
    sizing4 = pics4.resize((204,204))
    photo4 = PIL.ImageTk.PhotoImage(sizing4)
    my_label4 = Label(image=photo4)
    my_label4.image = photo4
    my_label4.grid(row= 0, column= 4, padx= 2, pady= 2)
    

open_file()
grayscale()

tombol = Button(root, text="click here", command=bradj, height=1, width=10)
tombol.grid(row=2, column=1)

negation()

root.mainloop()
