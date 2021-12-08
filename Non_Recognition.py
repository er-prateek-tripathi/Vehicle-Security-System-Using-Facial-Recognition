import tkinter
from tkinter import *
import pyttsx3
import playsound
from playsound import *


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


def dialogBox():
    username = UsernameInput.get()
    password = PasswordInput.get()

    if username == '' or password == '':
        text_to_speech('Please complete the required fields.')

    elif username == 'MASTERADMIN' and password == 'MASTER@101':
        text_to_speech('Authentication Successful!')
        text_to_speech('Sorry for Inconvenience.')
        text_to_speech('Welcome!')
        text_to_speech('Steering Wheel and other functions are now Online.')
        window.destroy()
    else:
        text_to_speech('Authentication was not Successful!')
        text_to_speech('Please, Step outside the vehicle.')
        text_to_speech('Security protocol is now online.')
        text_to_speech('The Owner is now being informed about the Security Breach.')
        text_to_speech('Steering Wheel and other functions are now Offline.')
        playsound('D:/Programming/Python Repo/Vehicle Security System/Alarm/Alert2.mp3')
        window.destroy()


def toggle_password():
    if PasswordInput.cget('show') == '':
        PasswordInput.config(show='*')
        ToggleButton.config(text='Show Password')
    else:
        PasswordInput.config(show='')
        ToggleButton.config(text='Hide Password')


window = Tk()
window.title('User Authentication')
window.geometry("640x640")
window.attributes('-fullscreen', True)
window.configure(background='Black')

HeadLabel = Label(window, text='$ User Authentication $', fg="black", relief=tkinter.RAISED, borderwidth=6)
HeadLabel.config(font=('algerian', 48))
HeadLabel.place(x=360, y=30)

UsernameLabel = Label(window, text='Username:', relief=tkinter.RAISED, borderwidth=6)
UsernameLabel.config(font=('algerian', 18))
UsernameLabel.place(x=500, y=200)

UsernameInput = Entry(window, bd=3)
UsernameInput.place(x=790, y=200)
UsernameInput.config(font=('times new roman', 25))

PasswordLabel = Label(window, text='Password: ', relief=tkinter.RAISED, borderwidth=6)
PasswordLabel.config(font=('algerian', 18))
PasswordLabel.place(x=500, y=350)

PasswordInput = Entry(window, bd=3, show='*')
PasswordInput.place(x=790, y=350)
PasswordInput.config(font=('times new roman', 25))

LoginButton = Button(window, text='Check Login', bg='lime', command=dialogBox)
LoginButton.config(font=('algerian', 18))
LoginButton.place(x=640, y=490)

exitButton = Button(window, text="Quit", bg='red', command=quit)
exitButton.config(font=('times new roman', 18))
exitButton.place(x=690, y=600)

ToggleButton = Button(window, text='Show Password', width=15, command=toggle_password)
ToggleButton.place(x=1220, y=355)

window.mainloop()
