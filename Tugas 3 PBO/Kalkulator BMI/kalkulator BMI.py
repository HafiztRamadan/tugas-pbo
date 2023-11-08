import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def hitung_bmi():
    berat = float(berat_entry.get())
    tinggi = float(tinggi_entry.get())
    usia = float(usia_entry.get())
    jenis_kelamin = jenis_kelamin_var.get()  

    satuan = satuan_var.get()
    if satuan == "Metric":
        bmi = berat / ((tinggi / 100) ** 2)
    else:
        bmi = (berat / (tinggi ** 2)) * 703

    if usia <= 20:
        if jenis_kelamin == "Laki-Laki":
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        else:
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        kategori = ["Kurus", "Berat Normal", "Kegemukan", "Obesitas"]
    else:
        if jenis_kelamin == "Laki-Laki":
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        else:
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        kategori = ["Kurus", "Berat Normal", "Kegemukan", "Obesitas"]

    label_hasil.config(text=f"BMI: {bmi:.2f} ({kategori[0]})")
    perbarui_grafik_bmi(bmi, nilai_bmi, kategori)

def perbarui_grafik_bmi(bmi, nilai_bmi, kategori):
    plt.clf()

    # Tambahkan warna yang berbeda untuk setiap kategori
    colors = ['green', 'yellow', 'orange', 'red']

    # Hitung sudut berdasarkan BMI
    angles = np.linspace(0, 2*np.pi, len(kategori), endpoint=False)

    # Plot pie chart untuk menyerupai gauge
    plt.pie([1]*len(kategori), labels=kategori, colors=colors, startangle=90, counterclock=False, wedgeprops=dict(width=0.4), autopct='%1.1f%%')

    # Tambahkan jarum atau titik
    angle = (bmi - 18.5) / (29.9 - 18.5) * 180  # Hitung sudut berdasarkan BMI

    # Hitung koordinat jarum di tengah lingkaran
    x = 0.5 + 0.35 * np.cos(np.radians(angle))
    y = 0.5 + 0.35 * np.sin(np.radians(angle))

    plt.scatter(x, y, marker='o', color='black', s=100, zorder=5)  # Gunakan marker 'o' untuk menambahkan titik pada posisi jarum

    # Tambahkan label untuk BMI pengguna
    plt.text(x, y, f'{bmi:.2f}', color='r', fontsize=12, ha='center', va='center', zorder=10)

    # Tambahkan label dan legenda
    plt.title("Kategori BMI")
    plt.legend()

    canvas.draw()

def perbarui_label_tinggi(event):
    satuan = satuan_var.get()
    if satuan == "Metric":
        label_tinggi.config(text="Tinggi (cm):")
    else:
        label_tinggi.config(text="Tinggi (inci):")

app = tk.Tk()
app.title("Kalkulator BMI")
app.geometry("800x500")

frame_satuan_jk = ttk.LabelFrame(app, text="Satuan dan Jenis Kelamin")
frame_satuan_jk.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

label_satuan = ttk.Label(frame_satuan_jk, text="Satuan:")
label_satuan.grid(row=0, column=0)
satuan_var = tk.StringVar()
satuan_dropdown = ttk.Combobox(frame_satuan_jk, textvariable=satuan_var, values=["Metric", "US"])
satuan_dropdown.grid(row=0, column=1)
satuan_dropdown.set("Metric")
satuan_dropdown.bind("<<ComboboxSelected>>", perbarui_label_tinggi)

label_jk = ttk.Label(frame_satuan_jk, text="Jenis Kelamin:")
label_jk.grid(row=1, column=0)
jenis_kelamin_var = tk.StringVar()
radio_laki = ttk.Radiobutton(frame_satuan_jk, text="Laki-Laki", variable=jenis_kelamin_var, value="Laki-Laki")
radio_perempuan = ttk.Radiobutton(frame_satuan_jk, text="Perempuan", variable=jenis_kelamin_var, value="Perempuan")
radio_laki.grid(row=1, column=1)
radio_perempuan.grid(row=1, column=2)
jenis_kelamin_var.set("Laki-Laki")

frame_personal = ttk.LabelFrame(app, text="Informasi Pribadi")
frame_personal.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

label_usia = ttk.Label(frame_personal, text="Usia:")
label_usia.grid(row=0, column=0)
usia_entry = ttk.Entry(frame_personal)
usia_entry.grid(row=0, column=1)

label_berat = ttk.Label(frame_personal, text="Berat (kg):")
label_berat.grid(row=1, column=0)
berat_entry = ttk.Entry(frame_personal)
berat_entry.grid(row=1, column=1)

label_tinggi = ttk.Label(frame_personal, text="Tinggi (cm):")
label_tinggi.grid(row=2, column=0)
tinggi_entry = ttk.Entry(frame_personal)
tinggi_entry.grid(row=2, column=1)

tombol_hitung = ttk.Button(app, text="Hitung BMI", command=hitung_bmi)
tombol_hitung.grid(row=3, column=0, pady=10, sticky="ew")

label_hasil = ttk.Label(app, text="")
label_hasil.grid(row=4, column=0, pady=5, sticky="ew")

figure = plt.figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(figure, master=app)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=1, rowspan=5, padx=10, pady=10, sticky="nsew")

app.mainloop()
