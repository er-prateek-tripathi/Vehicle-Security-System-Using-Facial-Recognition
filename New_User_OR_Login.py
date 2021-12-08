import tkinter
from tkinter import *
import os
import pyttsx3


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


window = Tk()
text_to_speech('Welcome.')
window.title('Welcome User')
window.geometry("720x540")
window.attributes('-fullscreen', True)
window.configure(background='Black')

HeadLabel = Label(window, text='$ Vehicle Security System $', fg="black", relief=tkinter.RAISED, borderwidth=6)
HeadLabel.config(font=('algerian', 48))
HeadLabel.place(x=280, y=30)


# ---------------------------------------------------------

# ----------------Open file : Adding New USer---------------------------
def NextUser():
    text_to_speech('Adding new User...Please follow the instructions.')
    os.system('1_Facial_Recognition_Dataset_Building.py')
    window.destroy()


NextStepButton = Button(window, text='Add new User', command=NextUser)
NextStepButton.config(font=('algerian', 25))
NextStepButton.place(x=300, y=350)


# ----------------Open file : Facial Recognition---------------------------
def Login():
    text_to_speech('Recognising...')
    os.system('3_Facial_Recognition.py')
    window.destroy()


NextStepButton = Button(window, text='Continue to Facial Recognition', command=Login)
NextStepButton.config(font=('algerian', 25))
NextStepButton.place(x=655, y=350)

# -------------------Exit----------------------------------------------------

exitButton = Button(window, text="Quit", bg='red', command=quit)
exitButton.place(x=700, y=650)
exitButton.config(font=('algerian', 20))
window.mainloop()
