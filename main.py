from doctest import master

import customtkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL.ImageOps import expand
from click import command
from customtkinter import CTkImage
from time import sleep

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()

TITRE = customtkinter.CTkFont(family="Poppins", size=60, weight="bold")
TITRE2 = customtkinter.CTkFont(family="Poppins", size=40, weight="bold")
INDICE = customtkinter.CTkFont(family="Poppins", size=24, weight="bold")
OPTIONS = customtkinter.CTkFont(family="Poppins", size=20,  weight="bold")
LOGO = customtkinter.CTkImage(light_image=Image.open("images/chasseLogo.png"),
                                   dark_image=Image.open("images/chasseLogo.png"),
                                   size=(111, 144))
CHAT = customtkinter.CTkImage(light_image=Image.open("images/image.png"),
                                   dark_image=Image.open("images/image.png"),
                                   size=(135, 169))

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

def bravo():
    frame_lieux = customtkinter.CTkFrame(master=app, fg_color="gray13")
    frame_lieux.grid(column=1, row=1, pady=20, padx=20, sticky="nsew")
    # Column configure
    frame_lieux.columnconfigure(0, weight=1)
    frame_lieux.columnconfigure(1, weight=1)
    frame_lieux.columnconfigure(2, weight=1)
    frame_lieux.columnconfigure(3, weight=1)
    frame_lieux.columnconfigure(4, weight=1)
    # Row configure
    frame_lieux.rowconfigure(0, weight=1)
    frame_lieux.rowconfigure(1, weight=1)
    frame_lieux.rowconfigure(2, weight=1)
    frame_lieux.rowconfigure(3, weight=1)
    frame_lieux.rowconfigure(4, weight=1)

    titre = customtkinter.CTkLabel(master=frame_lieux, text="Bravoooo", font=TITRE, text_color="#58B655",
                                   anchor="w")
    titre.grid(column=0, row=3, columnspan=5, padx=20, pady=20)

    sleep(2)

    frame_lieux.destroy()




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
    bonjour.grid(column=2, row=0, pady=40, padx=30, sticky="nw")


def etape1():
    frame_lieux = customtkinter.CTkFrame(master=app, fg_color="gray13")
    frame_lieux.grid(column=1, row=1, pady=20, padx=20, sticky="nsew")
    # Column configure
    frame_lieux.columnconfigure(0, weight=1)
    frame_lieux.columnconfigure(1, weight=1)
    frame_lieux.columnconfigure(2, weight=1)
    frame_lieux.columnconfigure(3, weight=1)
    frame_lieux.columnconfigure(4, weight=1)
    # Row configure
    frame_lieux.rowconfigure(0, weight=1)
    frame_lieux.rowconfigure(1, weight=1)
    frame_lieux.rowconfigure(2, weight=1)
    frame_lieux.rowconfigure(3, weight=1)
    frame_lieux.rowconfigure(4, weight=1)

    def bon():
        if mot.get() == "caboulot":
            frame_lieux.destroy()
            bravo()
            etape2()

    titre = customtkinter.CTkLabel(master=frame_lieux, text="Mais oussé kessé ça?", font=TITRE2, text_color="#A8E3FF",anchor="w")
    titre.grid(column=0, row=0, columnspan=5, padx=20, pady=20)

    image_logo = customtkinter.CTkLabel(frame_lieux, text="", image=CHAT, compound="left")
    image_logo.grid(column=0, row=1, padx=20)
    image_logo1 = customtkinter.CTkLabel(frame_lieux, text="", image=CHAT, compound="left")
    image_logo1.grid(column=1, row=1, padx=20)
    image_logo2 = customtkinter.CTkLabel(frame_lieux, text="", image=CHAT, compound="left")
    image_logo2.grid(column=2, row=1, padx=20)
    image_logo3 = customtkinter.CTkLabel(frame_lieux, text="", image=CHAT, compound="left")
    image_logo3.grid(column=3, row=1, padx=20)
    image_logo4 = customtkinter.CTkLabel(frame_lieux, text="", image=CHAT, compound="left")
    image_logo4.grid(column=4, row=1, padx=20)

    label = customtkinter.CTkLabel(frame_lieux, text="C -------------> T", font=INDICE)
    label.grid(column=0, row=2, columnspan=5, padx=20, pady=20)

    frame_reponse = customtkinter.CTkFrame(master=frame_lieux)
    frame_reponse.grid(column=0, row=3, columnspan=5, padx=20)
    mot = customtkinter.CTkEntry(frame_reponse, placeholder_text="Mot secret", width=375)
    mot.grid(column=0, row=0, sticky="e", padx=5, pady=20)
    button = customtkinter.CTkButton(frame_reponse, text="Enter", command=bon, width=100)
    button.grid(column=1, row=0, sticky="w", padx=5, pady=20)


def etape2():
    frame_lieux = customtkinter.CTkFrame(master=app, fg_color="gray13")
    frame_lieux.grid(column=1, row=1, pady=20, padx=20, sticky="nsew")
    # Column configure
    frame_lieux.columnconfigure(0, weight=1)
    frame_lieux.columnconfigure(1, weight=1)
    frame_lieux.columnconfigure(2, weight=1)
    frame_lieux.columnconfigure(3, weight=1)
    frame_lieux.columnconfigure(4, weight=1)
    # Row configure
    frame_lieux.rowconfigure(0, weight=1)
    frame_lieux.rowconfigure(1, weight=1)
    frame_lieux.rowconfigure(2, weight=1)
    frame_lieux.rowconfigure(3, weight=1)
    frame_lieux.rowconfigure(4, weight=1)

    titre = customtkinter.CTkLabel(master=frame_lieux, text="Bin là... Braille pas?", font=TITRE2, text_color="#A8E3FF",
                                   anchor="w")
    titre.grid(column=0, row=0, columnspan=5, padx=20, pady=20)


auth = False
def login_checkbox():
    global auth
    auth = check_var.get()

def login_button():
    if auth and username.get() == "RabbidRabbit69" and password.get() == "easter":
        clear()
        setup()
        frame_top()
        etape1()
    else:
        etat = customtkinter.CTkLabel(master=frame, text="Erreur", font=customtkinter.CTkFont(family="Roboto", size=15), text_color="red", anchor="n")
        etat.pack(fill="both")


frame = customtkinter.CTkFrame(master=app)
frame.pack(expand=True, padx=30, pady=30)
connexion = customtkinter.CTkLabel(master=frame, text="Connexion", font=TITRE, text_color="#A8E3FF", anchor="n")
connexion.pack(fill="y", pady=60)
username = customtkinter.CTkEntry(frame, placeholder_text="Nom d'utilisateur", width=375)
username.pack(padx=55)
password = customtkinter.CTkEntry(frame, placeholder_text="Mot de passe", width=375)
password.pack(padx=55, pady=15)
check_var = customtkinter.StringVar(value="off")
checkbox = customtkinter.CTkCheckBox(frame, text="Je suis vraiment le lapin de pâques promis juré craché!", command=login_checkbox, variable=check_var, onvalue="on", offvalue="off", width=375)
checkbox.pack(padx=55, pady=15)
button = customtkinter.CTkButton(frame, text="Se connecter", command=login_button, width=375)
button.pack(padx=55, pady=60)



setup()
#frame_top()
#etape1()
app.mainloop()