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
from matplotlib.pyplot import gray


from numpy import pad

root = Tk()
root.title("Aplikasi Image Enchanment")
root.configure(background='#242424')
root.geometry("1000x800")
    
    
def pixel(pics, validation):
    global arr, arr_gray
    
    x = 0
    y = 0
    arr = []
    arr_gray = []
    
    for i in range(w):
        for j in range(h):
            if(validation == 1):
                rvalue = pics.getpixel((x,y))[0]
                gvalue = pics.getpixel((x,y))[1]
                bvalue = pics.getpixel((x,y))[2]
                arr.append([x, y, rvalue, gvalue, bvalue])
            elif(validation == 2):
                r_grag = pics2.getpixel((x,y))[0]
                g_grag = pics2.getpixel((x,y))[1]
                b_grag = pics2.getpixel((x,y))[2]
                arr_gray.append([x, y, r_grag, g_grag, b_grag])
            
            j += 1
            y += 1
        x += 1
        i += 1
        y = 0
        j = 0   

def open_file():
    global arr, w, h, pics
    
    file_path = tkinter.filedialog.askopenfilename()
    pics = (PIL.Image.open(file_path))
    pics = pics.convert('RGB')
    sizing = pics.resize((204,204))
    
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 0, column= 1, padx= 2, pady= 2)
    
    w, h = pics.size
    
def grayscale ():
    global rvalue, gvalue, bvalue, gray_b, gray_g, gray_r, pics2, arr_gray 
    size = w, h
        
    pics2 = PIL.Image.new('RGB', size)
    load = pics2.load()

    for cr in arr:
        x, y, rvalue, gvalue, bvalue = cr   
        gray_r = (rvalue + gvalue +bvalue)//3
        gray_g = (rvalue + gvalue +bvalue)//3
        gray_b = (rvalue + gvalue +bvalue)//3
        load[x,y] = (gray_r, gray_g, gray_b)
        
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
    
    for cr in arr_gray:
        x, y, gray_r, gray_g, gray_b = cr   
        
        print(gray_r, gray_g, gray_b)
        
        adj_r = gray_r + userinput
        adj_g = gray_g + userinput
        adj_b = gray_b + userinput

        load[x,y] = (adj_r, adj_g, adj_b)
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

    for cr in arr_gray:
        x, y, gray_r, gray_g, gray_b = cr   
        
        print(gray_r, gray_g, gray_b)
        
        r_ngtn = 255 - gray_r
        g_ngtn = 255 - gray_g
        b_ngtn = 255 - gray_b
        load[x,y] = (r_ngtn, g_ngtn, b_ngtn)
    
    sizing4 = pics4.resize((204,204))
    photo4 = PIL.ImageTk.PhotoImage(sizing4)
    my_label4 = Label(image=photo4)
    my_label4.image = photo4
    my_label4.grid(row= 0, column= 4, padx= 2, pady= 2)
    

open_file()
pixel(pics, 1)

grayscale()
pixel(pics, 2)
tombol = Button(root, text="click here", command=bradj, height=1, width=10)
tombol.grid(row=2, column=1)

negation()

root.mainloop()
