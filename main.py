from doctest import master

import customtkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import CTkImage
from time import sleep

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()

TITRE = customtkinter.CTkFont(family="Poppins", size=60, weight="bold")
OPTIONS = customtkinter.CTkFont(family="Poppins", size=20,  weight="bold")
LOGO = customtkinter.CTkImage(light_image=Image.open("images/chasseLogo.png"),
                                   dark_image=Image.open("images/chasseLogo.png"),
                                   size=(111, 144))

app.title("Connexion")
app.geometry("450x550")


def setup():
    app.title("Chasse au trésor")
    app.geometry("1500x1100")
    # Column configure
    app.grid_columnconfigure(0)
    app.grid_columnconfigure(1, weight=1)
    # Row configure
    app.rowconfigure(0)
    app.rowconfigure(1, weight=1)


def clear():
    for wid in app.winfo_children():
        wid.destroy()


def frame_top():
    # Frame top ******************************************************************************************
    frame_top = customtkinter.CTkFrame(master=app, height=40, bg_color="gray13")
    frame_top.grid(column=0, row=0, sticky="nsew", columnspan=3)
    frame_top.columnconfigure(0)
    frame_top.columnconfigure(1, weight=1)
    frame_top.columnconfigure(2)
    image_logo = customtkinter.CTkLabel(frame_top, text="", image=LOGO, compound="left")
    image_logo.grid(column=0, row=0, pady=40, padx=70, sticky="nsew")
    titre = customtkinter.CTkLabel(master=frame_top, text="Chasse ô Coco", font=TITRE, text_color="#A8E3FF", anchor="w")
    titre.grid(column=1, row=0, padx=10, sticky="w")
    bonjour = customtkinter.CTkLabel(master=frame_top, text="Bonjour, RabbidRabbit69", font=customtkinter.CTkFont(family="Roboto", size=20), text_color="#A8E3FF", anchor="e")
    bonjour.grid(column=2, row=0,pady=40, padx=30, sticky="nw")

def frame_left():
    # Frame left ******************************************************************************************
    frame_left = customtkinter.CTkFrame(master=app, width=100, bg_color="gray13")
    frame_left.grid(column=0, row=1, sticky="nsw", rowspan=2)
    menu_bouton = customtkinter.CTkButton(master=frame_left, text="Tableau de bord", font=OPTIONS, text_color="#FF9191", fg_color="#FFF278", hover_color="#FFEA90", width=200, height=50)
    menu_bouton.pack(padx=20, pady=8, anchor="w")
    cuisine_bouton = customtkinter.CTkButton(master=frame_left, text="Cuisine", font=OPTIONS, text_color="#FF9191", fg_color="#A8E3FF", hover_color="#93D9FA", width=200, height=50)
    cuisine_bouton.pack(padx=20, pady=8, anchor="w")

def frame_lieux():
    # Frame lieux ******************************************************************************************
    frame_lieux = customtkinter.CTkFrame(master=app, fg_color="gray10")
    frame_lieux.grid(column=1, row=1, padx=20, pady=20, sticky="nsew")
    # Column configure
    frame_lieux.columnconfigure(0, weight=1)
    frame_lieux.columnconfigure(1, weight=1)
    frame_lieux.columnconfigure(2, weight=1)
    # Row configure
    frame_lieux.rowconfigure(0, weight=1)
    frame_lieux.rowconfigure(1, weight=1)

auth = False
def login_checkbox():
    global auth
    auth = check_var.get()

def login_button():
    if auth and username.get() == "vide" and password.get() == "vide":
        etat = customtkinter.CTkLabel(master=frame, text="Succès", font=customtkinter.CTkFont(family="Roboto", size=15), text_color="green", anchor="n")
        etat.pack(fill="both")
        clear()
        setup()
        frame_top()
        frame_left()
        frame_lieux()
    else:
        etat = customtkinter.CTkLabel(master=frame, text="Erreur", font=customtkinter.CTkFont(family="Roboto", size=15), text_color="red", anchor="n")
        etat.pack(fill="both")


frame = customtkinter.CTkFrame(master=app)
frame.pack(fill="both", expand=True, padx=30, pady=30)
connexion = customtkinter.CTkLabel(master=frame, text="Connexion", font=TITRE, text_color="#A8E3FF", anchor="n")
connexion.pack(fill="y", pady=60)
username = customtkinter.CTkEntry(frame, placeholder_text="Nom d'utilisateur")
username.pack(fill="x", padx=55)
password = customtkinter.CTkEntry(frame, placeholder_text="Mot de passe")
password.pack(fill="x", padx=55, pady=15)
check_var = customtkinter.StringVar(value="off")
checkbox = customtkinter.CTkCheckBox(frame, text="Je suis vraiment cet utilisateur", command=login_checkbox, variable=check_var, onvalue="on", offvalue="off")
checkbox.pack(fill="x", padx=55, pady=15)
button = customtkinter.CTkButton(frame, text="Se connecter", command=login_button)
button.pack(fill="x", padx=55, pady=15)

setup()
frame_top()
frame_left()
frame_lieux()
app.mainloop()