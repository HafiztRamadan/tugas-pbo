import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

# Fungsi untuk membuka gambar, menampilkan, dan mengekstrak teks
def extract_text():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        # Menampilkan gambar yang dipilih sebelum mengekstrak teks
        display_image(image)
        
        text = pytesseract.image_to_string(image)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, text)

# Fungsi untuk menampilkan gambar di GUI
def display_image(img):
    img.thumbnail((250, 250))  # Mengatur ukuran gambar yang ditampilkan
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

# Membuat GUI
root = tk.Tk()
root.title("Extraksi Teks dari Gambar")

# Tombol untuk memilih gambar
browse_button = tk.Button(root, text="Pilih Gambar", command=extract_text)
browse_button.pack()

# Menampilkan gambar yang dipilih
image_label = tk.Label(root)
image_label.pack()

# Output teks yang diekstrak
text_output = tk.Text(root, height=10, width=50)
text_output.pack()

root.mainloop()
