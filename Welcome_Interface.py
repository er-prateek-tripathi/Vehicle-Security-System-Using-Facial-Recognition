import tkinter
from tkinter import *
import messagebox as mbox
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

text_to_speech('Please browse through your options displayed on the screen.')


# -----------------------------developer info------------------------------------

def CreatorInfo():
    text_to_speech('Developers Info')
    mbox.showinfo("Information", "Project Group : 1 \n"
                                 "Developers : \n"
                                 "1.Name :- Prateek Tripathi \n"
                                 "\t Roll No. :- RKM024A21 \n"
                                 "\t Regd. No. :- 11908181 \n \n"
                                 "2.Name :- Sahyogvir Singh \n"
                                 "\t Roll No. :- RKM024A13 \n"
                                 "\t Regd. No. :- 11904949 \n \n"
                                 "3.Name :- Rishikesh Chouksey \n"
                                 "\t Roll No. :- RKM024A06 \n"
                                 "\t Regd. No. :- 11904832 \n \n"
                                 "\nClick OK!!")


CreatorsButton = Button(window, text='Developers', command=CreatorInfo)
CreatorsButton.config(font=('algerian', 20))
CreatorsButton.place(x=440, y=250)


# ----------------------------How to use-----------------------------------
def UsageInfo():
    text_to_speech('User Manual')
    mbox.showinfo("User Manual : .",
                  "1. Pre Registered User : \n"
                  "\ta. On the welcome interface click on login button. \n"
                  "\tb. It will lead to new window User Authentication. \n"
                  "\tc. Input the Credentials provided in the Manual. \n"
                  "= If the credentials are correct then okay, \n"
                  "= If not then you are in trouble. \n"
                  "Contact to the CUSTOMER CARE. \n"
                  "\td. After this, two options will appear. \n"
                  "\te. Add New User and Facial Recognition. \n"
                  "\tf. Click on Facial Recognition. \n"
                  "\tg. It will start Recognising your face. \n"
                  "= if validation is done, steering wheel will come out \n"
                  "of the dashboard and the other function of the \n"
                  "vehicle will come online. \n"
                  "= If the camera will not be able to recognise you, \n"
                  "then it will ask for the master password. \n"
                  "= If that password is correct, steering wheel will come out \n"
                  "of the dashboard and the other function of the \n"
                  "vehicle will come online. \n"
                  "= Else You will be locked out of the system and Security protocol will come online. \n \n"
                  "2. New User : \n"
                  "\ta. On the welcome interface click on login button. \n"
                  "\tb. It will lead to new window User Authentication. \n"
                  "\tc. Input the Credentials provided in the Manual. \n"
                  "= if the credentials are correct the n okay, \n"
                  "= If not then you are in trouble. \n"
                  "Contact to the CUSTOMER CARE. \n"
                  "\td. After this, two options will appear. \n"
                  "\te. Add New User and Facial Recognition. \n"
                  "\tf. Click on New User. \n"
                  "\tg. New interface will open. \n"
                  ":- It will ask you to face towards the camera and it will take 100 pictures of you. \n"
                  ":- It will take few time. So BE PATIENT. \n"
                  ":- After this Trainer interface will open. \n"
                  ":- It will train the machine to recognise the face fed to the machine via the samples. \n"
                  "After that Restart the vehicle and Proceed. \n \n"
                  "Click on OK after reading this.")


UsageButton = Button(window, text='How to Use!', command=UsageInfo)
UsageButton.config(font=('algerian', 20))
UsageButton.place(x=840, y=250)


# ----------------Open file : User Authentication---------------------------
def NextStep():
    text_to_speech('moving forward to User Authentication')
    os.system('User_Authentication.py')
    window.destroy()


NextStepButton = Button(window, text='User Authentication', command=NextStep)
NextStepButton.config(font=('algerian', 25))
NextStepButton.place(x=555, y=450)

# -------------------Exit----------------------------------------------------

exitButton = Button(window, text="Quit", bg='red', command=quit)
exitButton.place(x=700, y=650)
exitButton.config(font=('algerian', 20))
window.mainloop()
