from ctypes.wintypes import RGB
from tkinter import *
import tkinter as tk
from turtle import right
from PIL import Image
import PIL.Image
from PIL import ImageTk
import tkinter.filedialog
from array import *
from tkinter import simpledialog
from matplotlib import image
from matplotlib.pyplot import fill, gray
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.scrolledtext as st
import numpy as np

root = Tk()
root.title("IMAGE ENHANCEMENT APPLICATION (Grayscale, Brightness Adjustment, Negation)")
root.wm_iconbitmap("C:/Users/Wahyu/Downloads/logo.ico")
root.geometry("1310x600")

def getRed(redVal):
    return '#%02x%02x%02x' % (0, redVal, 0)

def histo(pics):
    histogram = pics.histogram()

    l1 = histogram[0:256]

    plt.figure(0)

    for i in range(0, 256):
        plt.bar(i, l1[i], color = getRed(i), edgecolor=getRed(i), alpha=0.3)

    plt.show()
    
def pixel(pics):
    global arr, arr_text, arr_gray
    
    x = 0
    y = 0
    arr = []
    arr_text = []
    arr_gray = []
    
    for i in range(w):
        for j in range(h):
            rvalue = pics.getpixel((x,y))[0]
            gvalue = pics.getpixel((x,y))[1]
            bvalue = pics.getpixel((x,y))[2]
            arr.append([x, y, rvalue, gvalue, bvalue])
            arr_text.append([rvalue])
            arr_gray.append([x, y, rvalue])
            j += 1
            y += 1
        x += 1
        i += 1
        y = 0
        j = 0 

def text():
    label1 = Label(root, text = "CITRA ASLI")
    label1.grid(row= 0, column= 1)
    label2 = Label(root, text = "CITRA GRAYSCALE")
    label2.grid(row = 0, column= 2)
    label3 = Label(root, text = "CITRA HASIL")
    label3.grid(row = 0, column=3)

def frame():
    frame1 = Frame(root, width=206, height=206, background="#242424")
    frame1.grid(row= 1, column= 1, padx= 20, pady= 2)
    frame2 = Frame(root, width=206, height=206, background="#242424")
    frame2.grid(row= 1, column= 2, padx= 20, pady= 2)
    frame3 = Frame(root, width=206, height=206, background="#242424")
    frame3.grid(row= 1, column= 3, padx= 20, pady= 2)

def open_file():
    global w, h, pics
    
    file_path = tkinter.filedialog.askopenfilename()
    pics = (PIL.Image.open(file_path))
    pics = pics.convert('RGB')
    
    sizing = pics.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 1, column= 1, pady= 2)
    
    w, h = pics.size
    
def grayscale ():
    global pics2 
    
    size = w, h
    
    pixel(pics)
    
    pics2 = PIL.Image.new('RGB', size)
    load = pics2.load()

    for cr in arr:
        x, y, rvalue, gvalue, bvalue = cr   
        gray = (rvalue + gvalue +bvalue)//3
        load[x,y] = (gray, gray, gray)
    
    sizing = pics2.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo        
    my_label.grid(row= 1, column= 2, pady= 2)
    
    text_area.delete(1.0, END)
    pixel(pics2)
    text_area.insert(tk.INSERT, arr_text)
    
    histo(pics2)
    
def bradj():
    size = w, h
    
    pixel(pics2)
    
    userinput = simpledialog.askinteger(title="Input", prompt="Nilai Peningkatan")
        
    pics3 = PIL.Image.new('RGB', size)
    load = pics3.load()
    
    for cr in arr_gray:
        x, y, gray = cr  
        adj = gray + userinput
        load[x,y] = (adj, adj, adj)
    
    sizing = pics3.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 1, column= 3)
    
    text_area2.delete(1.0, END)
    pixel(pics3)
    text_area2.insert(tk.INSERT, arr_text)
    
    histo(pics3)
    
def negation():
    size = w, h
    
    pixel(pics2)
        
    pics4 = PIL.Image.new('RGB', size)
    load = pics4.load()

    for cr in arr_gray:
        x, y, gray = cr
        ntn = 255 - gray
        load[x,y] = (ntn, ntn, ntn)
    
    sizing = pics4.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 1, column= 3, pady= 2)
    
    text_area2.delete(1.0, END)
    pixel(pics4)
    text_area2.insert(tk.INSERT, arr_text)
    
    histo(pics4)
    
def gammacorrection():
    size = w, h
    
    pixel(pics2)
    
    userinput2 = simpledialog.askfloat(title="Input", prompt="Nilai Gamma")
    
    pics5 = PIL.Image.new('RGB', size)
    load = pics5.load()

    for cr in arr_gray:
        x, y, gray = cr
        gcr = round((gray)**(1/userinput2))
        print(gcr)
        load[x, y] = (gcr, gcr, gcr)
    
    sizing = pics5.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 1, column= 3, pady= 2)
    
    text_area2.delete(1.0, END)
    pixel(pics5)
    text_area2.insert(tk.INSERT, arr_text)

def contraststrech1():
    size = w, h
    
    pixel(pics2)
    
    minimum = min(arr_text)
    maximum = max(arr_text)
    
    str_min = ' '.join(str(l) for l in minimum)
    str_max = ' '.join(str(l) for l in maximum)
    
    integer_min = int(str_min)
    integer_max = int(str_max)
    
    pics6 = PIL.Image.new('RGB', size)
    load = pics6.load()
    
    for cr in arr_gray:
        x, y, gray = cr
        csr = round((gray-integer_min)/(integer_max-integer_min)*(255))
        print(csr)
        load[x, y] = (csr, csr, csr)
    
    sizing = pics6.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 1, column= 3, pady= 2)
    
    text_area2.delete(1.0, END)
    pixel(pics6)
    text_area2.insert(tk.INSERT, arr_text)
    
def contraststrech2():
    size = w, h
    
    pixel(pics2)
    
    userinput = simpledialog.askinteger(title="Input", prompt="Persentasi c")
    userinput2 = simpledialog.askinteger(title="Input", prompt="Persentasi d")
    
    persen_c = userinput/100
    persen_d = userinput2/100
    
    minimum = min(arr_text)
    maximum = max(arr_text)
    
    str_min = ' '.join(str(l) for l in minimum)
    str_max = ' '.join(str(l) for l in maximum)
    
    integer_min = int(str_min)
    integer_max = int(str_max)
    
    p_min = round(integer_min + (persen_c*integer_min))
    p_max = round(integer_max - (persen_d*integer_max))
    
    pics7 = PIL.Image.new('RGB', size)
    load = pics7.load()
    
    for cr in arr_gray:
        x, y, gray = cr
        
        if p_min <= gray <= p_max :
            hasil = round((gray - p_min)/(p_max - p_min)*255)
        elif gray <= p_min :
            hasil = 0
        elif gray >= p_max :
            hasil = 255
        load[x, y] = (hasil, hasil, hasil)
    
    sizing = pics7.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 1, column= 3, pady= 2)
    
    text_area2.delete(1.0, END)
    pixel(pics7)
    text_area2.insert(tk.INSERT, arr_text)

def intensityslice1():
    size = w, h
    
    pixel(pics2)
    
    userinput = simpledialog.askinteger(title="Input", prompt="Interval Terkecil")
    userinput2 = simpledialog.askinteger(title="Input", prompt="Interval Terbesar")
    
    pics8 = PIL.Image.new('RGB', size)
    load = pics8.load()

    for cr in arr_gray:
        x, y, gray = cr
        
        if userinput <= gray <= userinput2 :
            inslc = 255
        else :
            inslc = 0

        load[x, y] = (inslc, inslc, inslc)
            
    sizing = pics8.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 1, column= 3, pady= 2)
    
    text_area2.delete(1.0, END)
    pixel(pics8)
    text_area2.insert(tk.INSERT, arr_text)

def intensityslice2():
    size = w, h
    
    pixel(pics2)
    
    userinput = simpledialog.askinteger(title="Input", prompt="Interval Terkecil")
    userinput2 = simpledialog.askinteger(title="Input", prompt="Interval Terbesar")
    
    pics7 = PIL.Image.new('RGB', size)
    load = pics7.load()

    for cr in arr_gray:
        x, y, gray = cr
        
        if userinput <= gray <= userinput2 :
            inslc = 255 
        else :
            inslc = gray
        
        print(inslc)
        load[x, y] = (inslc, inslc, inslc)
            
    sizing = pics7.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 1, column= 3, pady= 2)
    
    text_area2.delete(1.0, END)
    pixel(pics7)
    text_area2.insert(tk.INSERT, arr_text)

def bitextraction():
    size = w, h
    
    pixel(pics2)
    
    userinput = simpledialog.askinteger(title="Input", prompt="Bit ke-")
    
    pics9 = PIL.Image.new('RGB', size)
    load = pics9.load()
    
    for cr in arr_gray:
        x, y, gray = cr
        biner = format(gray,'08b')
        reverse = biner[::-1]
        be = int(reverse[userinput])
        
        if be == 0:
            hasil = 0
        elif be == 1:
            hasil = 255
            
        load[x, y] = (hasil, hasil, hasil)
        
    sizing = pics9.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 1, column= 3, pady= 2)
    
    text_area2.delete(1.0, END)
    pixel(pics9)
    text_area2.insert(tk.INSERT, arr_text)
    
text()
frame()

text_area = st.ScrolledText(root, width = 40, height = 14, font = ("Times New Roman",10))
text_area.grid(row=1, column = 5, pady = 10, padx = 10)

text_area2 = st.ScrolledText(root, width = 40, height = 14, font = ("Times New Roman",10))
text_area2.grid(row=1, column = 6, pady = 10, padx = 10)

tombol1 = Button(root, text="Buka Gambar", command=open_file, height=1, width=20)
tombol1.grid(row=3, column=1, pady= 2)

tombol2 = Button(root, text="Grayscale", command=grayscale, height=1, width=20)
tombol2.grid(row=3, column=2, pady= 2)

tombol3 = Button(root, text="Brightness Adjustment", command=bradj, height=1, width=20)
tombol3.grid(row=3, column=3, pady= 2)

tombol4 = Button(root, text="Negation", command=negation, height=1, width=20)
tombol4.grid(row=4, column=3, pady= 2)

tombol5 = Button(root, text="Gamma Correction", command=gammacorrection, height=1, width=20)
tombol5.grid(row=5, column=3, pady= 2)

tombol6 = Button(root, text="Contrast Streching 1", command=contraststrech1, height=1, width=20)
tombol6.grid(row=6, column=3, pady= 2)

tombol7 = Button(root, text="Contrast Streching 2", command=contraststrech2, height=1, width=20)
tombol7.grid(row=8, column=3, pady= 2)

tombol8 = Button(root, text="Intensity Slicing 1", command=intensityslice1, height=1, width=20)
tombol8.grid(row=9, column=3, pady= 2)

tombol9 = Button(root, text="Intensity Slicing 2", command=intensityslice2, height=1, width=20)
tombol9.grid(row=10, column=3, pady= 2)

tombol10 = Button(root, text="Bit Extraction", command=bitextraction, height=1, width=20)
tombol10.grid(row=11, column=3, pady= 2)

root.mainloop()
