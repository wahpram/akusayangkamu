from cProfile import label
from tkinter import *
from PIL import Image
import PIL.Image
from PIL import ImageTk
import tkinter.filedialog
from array import *

root = Tk()
root.title("JANJI GA NYESEL MASUK TEKNIK!")

root.geometry("400x400")

def koordinat():
    global arr, w, h, rvalue, gvalue, bvalue,x, y
    
    x = 0
    y = 0
    arr = []
    
    file_path = tkinter.filedialog.askopenfilename()
    pics = (PIL.Image.open(file_path))

    photo = PIL.ImageTk.PhotoImage(PIL.Image.open(file_path))
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row=2, column=2)
    
    # pics1 = PIL.ImageTk.PhotoImage(PIL.Image.OPEN(file_path))
    w, h = pics.size
    
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
    
def hasil_copy():
    print(arr)
    size = w, h
    #new image
    pics2 = PIL.Image.new('RGB', size)

    load = pics2.load()

    for cr in arr:
        x, y, rvalue, gvalue, bvalue = cr
        
        load[x,y] = (rvalue, gvalue, bvalue)
    
    photo2 = PIL.ImageTk.PhotoImage(pics2)
    my_label2 = Label(image=photo2)
    my_label2.image = photo2
    my_label2.grid(row=2, column=5)

def sel(x):
    size = w, h
    
    match x:
        case 1:
            pics3 = PIL.Image.new('RGB', size)

            load2 = pics3.load()

            for cr in arr:
                x, y, rvalue, gvalue, bvalue = cr
                
                load2[x,y] = (rvalue, 0, 0)
            
            photo3 = PIL.ImageTk.PhotoImage(pics3)
            my_label2 = Label(image=photo3)
            my_label2.image = photo3
            my_label2.grid(row=2, column=6)
            
        case 2:
            pics4 = PIL.Image.new('RGB', size)

            load3 = pics4.load()

            for cr in arr:
                x, y, rvalue, gvalue, bvalue = cr
                
                load3[x,y] = (0, gvalue, 0)
            
            photo3 = PIL.ImageTk.PhotoImage(pics4)
            my_label2 = Label(image=photo3)
            my_label2.image = photo3
            my_label2.grid(row=2, column=6) 
           
        case 3:
            pics5 = PIL.Image.new('RGB', size)

            load4 = pics5.load()

            for cr in arr:
                x, y, rvalue, gvalue, bvalue = cr
                
                load4[x,y] = (0, 0, bvalue)
            
            photo5 = PIL.ImageTk.PhotoImage(pics5)
            my_label2 = Label(image=photo5)
            my_label2.image = photo5
            my_label2.grid(row=2, column=6)
        
        case 4:
            pics6 = PIL.Image.new('RGB', size)

            load5 = pics6.load()

            for cr in arr:
                x, y, rvalue, gvalue, bvalue = cr
                
                load5[x,y] = (rvalue, gvalue, 0)
            
            photo6 = PIL.ImageTk.PhotoImage(pics6)
            my_label2 = Label(image=photo6)
            my_label2.image = photo6
            my_label2.grid(row=2, column=6)

        case 5:
            pics7 = PIL.Image.new('RGB', size)

            load6 = pics7.load()

            for cr in arr:
                x, y, rvalue, gvalue, bvalue = cr
                
                load6[x,y] = (0,gvalue, bvalue)
            
            photo7 = PIL.ImageTk.PhotoImage(pics7)
            my_label2 = Label(image=photo7)
            my_label2.image = photo7
            my_label2.grid(row=2, column=6)

        case 6:
            pics8 = PIL.Image.new('RGB', size)

            load7 = pics8.load()

            for cr in arr:
                x, y, rvalue, gvalue, bvalue = cr
                
                load7[x,y] = (rvalue,0, bvalue)
            
            photo8 = PIL.ImageTk.PhotoImage(pics8)
            my_label2 = Label(image=photo8)
            my_label2.image = photo8
            my_label2.grid(row=2, column=6)
            

var = IntVar()
R1 = Radiobutton(root, text="MERAH", variable=var, value=1,
                command= lambda: sel(1))
R1.grid(row=4, column=6)

R2 = Radiobutton(root, text="HIJAU", variable=var, value=2,
                command= lambda: sel(2))
R2.grid(row=4, column=7)

R3 = Radiobutton(root, text="BIRU", variable=var, value=3,
                command= lambda: sel(3))
R3.grid(row=4, column=8)

R4 = Radiobutton(root, text="YELLOW", variable=var, value=4,
                command= lambda: sel(4))
R4.grid(row=5, column=6)

R5 = Radiobutton(root, text="CYAN", variable=var, value=5,
                command= lambda: sel(5))
R5.grid(row=5, column=7)

R6 = Radiobutton(root, text="MAGENTA", variable=var, value=6,
                command= lambda: sel(6))
R6.grid(row=5, column=8)



label = Label(root)
label.grid(row=3, column=7)    

tombol = Button(root, text='HAI CANTIK', command=koordinat)

tombol.grid(row=3, column=2)

tombol2 = Button(root, text="pecik gen", command=hasil_copy)

tombol2.grid(row=3, column=5)

root.geometry('1300x400+33+100')

root.mainloop()
#radiobox