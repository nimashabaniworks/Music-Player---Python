import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer for audio playback
pygame.mixer.init()

def play_music():
    song = filedialog.askopenfilename(title="Choose a song", filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
    if song:
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0, start=0.0)
        song_name.set(f"Now Playing: {song.split('/')[-1]}")
        play_button.config(state=tk.DISABLED)
        pause_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.NORMAL)

def stop_music():
    pygame.mixer.music.stop()
    song_name.set("No song playing")
    play_button.config(state=tk.NORMAL)
    pause_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.DISABLED)

def pause_music():
    pygame.mixer.music.pause()
    play_button.config(state=tk.NORMAL)
    pause_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

def unpause_music():
    pygame.mixer.music.unpause()
    play_button.config(state=tk.DISABLED)
    pause_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
root.title("Stylish Music Player")
root.geometry("500x300")
root.config(bg="#2e3d49")  # Background color

# Add a custom font for the text
font_style = ("Helvetica", 14, "bold")

# Create a label to show the song name
song_name = tk.StringVar()
song_label = tk.Label(root, textvariable=song_name, font=("Helvetica", 16, "italic"), bg="#2e3d49", fg="#f1f1f1")
song_label.pack(pady=20)

# Function to create custom buttons (accepts state argument)
def create_button(text, command, state=tk.NORMAL, width=15, height=2):
    return tk.Button(root, text=text, command=command, font=font_style, bg="#1c1c1c", fg="#ffffff", activebackground="#4CAF50", activeforeground="#ffffff", relief="solid", bd=2, width=width, height=height, state=state)

# Create buttons for play, pause, and stop
play_button = create_button("Play", play_music)
play_button.pack(side=tk.LEFT, padx=20, pady=10)

pause_button = create_button("Pause", pause_music, state=tk.DISABLED)
pause_button.pack(side=tk.LEFT, padx=20, pady=10)

stop_button = create_button("Stop", stop_music, state=tk.DISABLED)
stop_button.pack(side=tk.LEFT, padx=20, pady=10)

unpause_button = create_button("Unpause", unpause_music, state=tk.DISABLED)
unpause_button.pack(side=tk.LEFT, padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()
