from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Images")

image_original = Image.open("images/Cat03.jpg")
image_tk = ImageTk.PhotoImage(image_original)

label = ttk.Label(window, image=image_tk, text="Images")
label.pack()

window.mainloop()
