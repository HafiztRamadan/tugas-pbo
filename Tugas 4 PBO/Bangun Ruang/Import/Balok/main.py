import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
import fungsi

def hitung_luas():
    p = float(txtpanjang.get())
    l = float(txtlebar.get())
    t = float(txttinggi.get()) 

    L = fungsi.hitung_luas(p,l,t)
    txtluas.delete(0,END)
    txtluas.insert(END, L)

def hitung_volume(): 
    p = float(txtpanjang.get())  
    l = float(txtlebar.get()) 
    t = float(txttinggi.get())

    V = fungsi.hitung_volume(p,l,t)
    txtvolume.delete(0,END,)
    txtvolume.insert(END, V)

def hitung():
    hitung_luas()
    hitung_volume()  

# Create tkinter object
app = tk.Tk() 

# Tambahkan judul 
app.title("Kalkulator Luas dan Volume Balok")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label panjang
panjang = Label(frame, text="panjang:")
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=0, column=1)

# Label Lebar
lebar = Label(frame, text="Lebar:")
lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Lebar
txtlebar = Entry(frame)
txtlebar.grid(row=1, column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Output Textbox Luas
txtluas = Entry(frame)
txtluas.grid(row=4, column=1)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)
# Output Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=5, column=1, )

app.mainloop()
