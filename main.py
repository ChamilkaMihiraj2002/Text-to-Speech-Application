import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from PIL import ImageTk, Image

root = Tk()
root.title("TEXT TO SPEECH APP")
root.geometry("500x700+50+50")
root.resizable(False, False)
root.configure(bg="#305065")

engine = pyttsx3.init()


def setvoice(gender, text, speed):
    voices = engine.getProperty('voices')
    if gender == 'Male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    if speed == 'Fast':
        engine.setProperty('rate', 250)
    elif speed == 'Normal':
        engine.setProperty('rate', 150)
    else:
        engine.setProperty('rate', 60)

    engine.say(text)
    engine.runAndWait()


def speaknow():
    text = text_area.get(1.0, END).strip()
    if text:
        gender = gender_combo.get()
        speed = speed_combo.get()
        setvoice(gender, text, speed)


def download():
    text = text_area.get(1.0, END).strip()
    if text:
        gender = gender_combo.get()
        speed = speed_combo.get()
        file_path = filedialog.asksaveasfilename(defaultextension='.mp3', filetypes=[("MP3 files", '*.mp3')])
        if file_path:
            voices = engine.getProperty('voices')
            if gender == 'Male':
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)

            if speed == 'Fast':
                engine.setProperty('rate', 250)
            elif speed == 'Normal':
                engine.setProperty('rate', 150)
            else:
                engine.setProperty('rate', 60)

            engine.save_to_file(text, file_path)
            engine.runAndWait()


# ICON
image_icon = ImageTk.PhotoImage(file="./Assets/speaker.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_Frame = Frame(root, bg="white", height=110, width=500)
Top_Frame.place(x=0, y=0)

Logo = ImageTk.PhotoImage(file="./Assets/speaker.png")
label = Label(Top_Frame, image=Logo, bg="white").place(x=10, y=5)

Label(Top_Frame, text="TEXT TO SPEECH", font="arial 30 bold", bg="white", fg="black").place(x=120, y=30)

# Text Area
text_area = Text(root, font="Roboto 15", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=480, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg="#305065", fg="white").place(x=75, y=460)
Label(root, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(x=75, y=560)

gender_combo = Combobox(root, values=['Male', 'Female'], font="arial 14", state='readonly', width=10)
gender_combo.place(x=75, y=500)
gender_combo.set('Male')

speed_combo = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='readonly', width=10)
speed_combo.place(x=75, y=600)
speed_combo.set('Normal')

imageicon = ImageTk.PhotoImage(file="./Assets/speak logo.png")
btn = Button(root, text="Speak", compound=LEFT, image=imageicon, width=150, font="arial 14 bold", bg="#39c790",
             command=speaknow)
btn.place(x=270, y=480)

imageicon2 = ImageTk.PhotoImage(file="./Assets/download.png")
save = Button(root, text="Save", compound=LEFT, image=imageicon2, width=150, font="arial 14 bold", bg="#00ccff",
              command=download)
save.place(x=270, y=580)

root.mainloop()
