from ctypes.wintypes import RGB
from tkinter import *
from PIL import Image
import PIL.Image
from PIL import ImageTk
import tkinter.filedialog
from array import *
from tkinter import simpledialog
from matplotlib.pyplot import gray

root = Tk()
root.title("IMAGE ENHANCEMENT APPLICATION (Grayscale, Brightness Adjustment, Negation)")
root.wm_iconbitmap("C:/Users/Wahyu/Downloads/logo.ico")
root.geometry("1000x300")

label1 = Label(root, text = "Gambar Asli")
label1.grid(row= 0, column= 1)
label2 = Label(root, text = "Grayscale")
label2.grid(row = 0, column= 2)
label3 = Label(root, text = "Brightness Adjustment")
label3.grid(row = 0, column=3)
label4 = Label(root, text = "Negation")
label4.grid(row = 0, column=4)


frame1 = Frame(root, width=206, height=206, background="#242424")
frame1.grid(row= 1, column= 1, padx= 20, pady= 2)
frame2 = Frame(root, width=206, height=206, background="#242424")
frame2.grid(row= 1, column= 2, padx= 20, pady= 2)
frame3 = Frame(root, width=206, height=206, background="#242424")
frame3.grid(row= 1, column= 3, padx= 20, pady= 2)
frame4 = Frame(root, width=206, height=206, background="#242424")
frame4.grid(row= 1, column= 4, padx= 20, pady= 2)
    
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
                r_gray = pics2.getpixel((x,y))[0]
                g_gray = pics2.getpixel((x,y))[1]
                b_gray = pics2.getpixel((x,y))[2]
                arr_gray.append([x, y, r_gray, g_gray, b_gray])

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
    my_label.grid(row= 1, column= 1, padx= 2, pady= 2)
    
    w, h = pics.size
    
    pixel(pics, 1)
    
def grayscale ():
    global rvalue, gvalue, bvalue, gray_b, gray_g, gray_r, pics2, arr_gray 
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
    my_label2.grid(row= 1, column= 2, padx= 2, pady= 2)
    
    pixel(pics, 2)
    
def bradj():
    global gray
    
    size = w, h
    
    userinput = simpledialog.askinteger(title="Input", prompt="input")
        
    pics3 = PIL.Image.new('RGB', size)
    load = pics3.load()
    
    for cr in arr_gray:
        x, y, gray, gray, gray = cr   
        adj = gray + userinput
        load[x,y] = (adj, adj, adj)
    
    sizing3 = pics3.resize((204,204))
    photo3 = PIL.ImageTk.PhotoImage(sizing3)
    my_label3 = Label(image=photo3)
    my_label3.image = photo3
    my_label3.grid(row= 1, column= 3)
    
def negation():
    size = w, h
        
    pics4 = PIL.Image.new('RGB', size)
    load = pics4.load()

    for cr in arr_gray:
        x, y, gray, gray, gray = cr   
        ngtn = 255 - gray
        load[x,y] = (ngtn, ngtn, ngtn)
    
    sizing4 = pics4.resize((204,204))
    photo4 = PIL.ImageTk.PhotoImage(sizing4)
    my_label4 = Label(image=photo4)
    my_label4.image = photo4
    my_label4.grid(row= 1, column= 4, padx= 2, pady= 2)

tombol = Button(root, text="Buka Gambar", command=open_file, height=1, width=15)
tombol.grid(row=3, column=1)

tombol = Button(root, text="Grayscale", command=grayscale, height=1, width=10)
tombol.grid(row=3, column=2)

tombol = Button(root, text="Brightness Adjustment", command=bradj, height=1, width=20)
tombol.grid(row=3, column=3)

tombol = Button(root, text="Negation", command=negation, height=1, width=10)
tombol.grid(row=3, column=4)

# tombol = Button(root, text="Reset", command=reset, height=1, width=10)
# tombol.grid(row=5, column=2)

root.mainloop()
