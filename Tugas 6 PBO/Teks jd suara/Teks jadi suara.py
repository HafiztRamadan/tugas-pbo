from gtts import gTTS
import tkinter as tk
from tkinter import messagebox

def convert_to_speech():
    text = entry.get()  # Mendapatkan teks dari kotak teks
    if text:
        try:
            tts = gTTS(text=text, lang='id')  # Ubah teks menjadi suara dengan bahasa Indonesia
            tts.save("output.mp3")  # Simpan sebagai file output.mp3
            messagebox.showinfo("Success", "Text converted to speech successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter text to convert!")

# Membuat window
root = tk.Tk()
root.title("Text to Speech Converter")

# Membuat label dan kotak teks untuk input
label = tk.Label(root, text="Enter text:")
label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

# Tombol untuk mengonversi teks ke suara
convert_button = tk.Button(root, text="Convert", command=convert_to_speech)
convert_button.pack()

# Fungsi untuk menutup aplikasi
def close_app():
    root.destroy()

# Tombol untuk keluar
exit_button = tk.Button(root, text="Exit", command=close_app)
exit_button.pack()

# Menjalankan aplikasi
root.mainloop()
