import pygame
import tkinter as tk
from tkinter import filedialog

def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def main():
    root = tk.Tk()
    root.title("MP3 Player")
    root.minsize(width=400, height=300)

    label = tk.Label(root, text="MP3 Player", font=("Helvetica", 20))
    label.pack(pady=10)

    play_button = tk.Button(root, text="Play", command=play_music)
    play_button.pack(pady=20)

    stop_button = tk.Button(root, text="Stop", command=stop_music)
    stop_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
