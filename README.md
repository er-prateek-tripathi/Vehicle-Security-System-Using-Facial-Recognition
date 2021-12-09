# Vehicle-Security-System-Using-Facial-Recognition.
A Vehicle Security System which will recognise the Face of the user before bringing the vehicle system online.
Modules Used : 
  1. [OpenCV](https://opencv.org/)
  2. [Tkinter](https://docs.python.org/3/library/tkinter.html)
  3. [OS](https://docs.python.org/3/library/os.html)
  4. [MessageBox](https://docs.python.org/3/library/tkinter.messagebox.html)
  5. [Python Text to Speech (PYTTSX3)](https://pypi.org/project/pyttsx3/)
  6. [Pillow (PIL)](https://pypi.org/project/Pillow/)
  7. [Numpy](https://numpy.org/doc/stable/)
  8. [Playsound](https://pypi.org/project/playsound/)

>Pyhton Version : 3.7.0

>OpenCV Version : 4.5.4.60

>Numpy Version : 1.21.4

>PlaySound Version : 1.3.0

>PYTTSX3 Version : 2.90

CasCade Classifier : [Haar Cascade Frontaface Classifier](https://www.pyimagesearch.com/2021/04/12/opencv-haar-cascades/), [Tutorial](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)

Face Recognizer: [Local Binary Patterns Histograms Face Recognizer](https://docs.opencv.org/3.4/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html)

Adaboost Algorithm : [Adaboost Algorithm](https://www.mygreatlearning.com/blog/adaboost-algorithm/)

How to Use :                          
>         1. Pre Registered User :                
                    a. On the welcome interface click on login button.                
                    b. It will lead to new window User Authentication.
                    c. Input the Credentials provided in the Manual.
                      = If the credentials are correct then okay,
                      = If not then you are in trouble.
                    Contact to the CUSTOMER CARE.
                    d. After this, two options will appear.
                    e. Add New User and Facial Recognition.
                    f. Click on Facial Recognition.
                    g. It will start Recognising your face.
                      = if validation is done, steering wheel will come out
                          of the dashboard and the other function of the
                          vehicle will come online.
                      = If the camera will not be able to recognise you,
                          then it will ask for the master password.
                      = If that password is correct, steering wheel will come out
                          of the dashboard and the other function of the
                            vehicle will come online.
                      = Else You will be locked out of the system and Security protocol will come online.
>         2. New User :
                    a. On the welcome interface click on login button.
                    b. It will lead to new window User Authentication.
                    c. Input the Credentials provided in the Manual.
                      = if the credentials are correct the n okay,
                      = If not then you are in trouble.
                    Contact to the CUSTOMER CARE.
                    d. After this, two options will appear.
                    e. Add New User and Facial Recognition.
                    f. Click on New User.
                    g. New interface will open.
                      :- It will ask you to face towards the camera and it will take 100 pictures of you.
                      :- It will take few time. So BE PATIENT.
                      :- After this Trainer interface will open.
                      :- It will train the machine to recognise the face fed to the machine via the samples.
>         After that Restart the vehicle and Proceed.
                  
## Order of Execution of files
                         
                     a. For Pre - Registered User :-
                          1. Welcome Interface
                          2. User Authentication
                          3. New User Or Login(Continue to facial recognition)
                          4. Facial Recognition
                          5. Non Recognition (On Non detection of face)
                     b. For New User :- 
                          1. Welcome Interface
                          2. User Authentication
                          3. New User Or Login(New User)
                          4. Facial recognition Dataset Building (Take face Samples)
                          5. Facial REcognition Dataset Training.(Training Model)
                          6. Go back to Welcome Interfae

 
 ## If you are facing any type of problem in understanding the codes and data in the project,
 ## SOLVE IT YOURSELF
 ## Be INDEPENDENT.
 ## Good Bye.
