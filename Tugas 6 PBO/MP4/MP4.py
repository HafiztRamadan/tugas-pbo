import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

def play_video():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        video = VideoFileClip(file_path)
        video.preview()

root = tk.Tk()
root.minsize(width=400, height=300)
root.title("MP4 Player")

play_button = tk.Button(root, text="Play Video", command=play_video)
play_button.pack(pady=20)

root.mainloop()
