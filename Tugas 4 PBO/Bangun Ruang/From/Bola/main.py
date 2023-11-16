import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
from fungsi import hitung_luas, hitung_volume

def hitung():
    r = float(txtjarijari.get())
    
    luas_result = hitung_luas(r)
    volume_result = hitung_volume(r)

    txtluas.delete(0, END)
    txtluas.insert(END, luas_result)

    txtvolume.delete(0, END)
    txtvolume.insert(END, volume_result)

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Bola")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Jari - Jari
jarijari = Label(frame, text="Jari - Jari:")
jarijari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari - Jari
txtjarijari = Entry(frame)
txtjarijari.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=1, column=1, sticky=W, padx=5, pady=5)

# Output Luas
luas = Label(frame, text="Luas:")
luas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox Luas
txtluas = Entry(frame)
txtluas.grid(row=2, column=1)

# Output Volume
volume = Label(frame, text="Volume:")
volume.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=3, column=1)

app.mainloop()