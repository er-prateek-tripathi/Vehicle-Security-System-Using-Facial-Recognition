import cv2
import os
import pyttsx3


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


text_to_speech('Please sit straight and  face towards the camera')

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
print('Enter your name nad then Press ENTER KEY.')
face_id = input(text_to_speech('Enter your Name :   '))


text_to_speech('Initializing face capture. Look at the camera and wait ...')
count = 0

while True:

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/Name_" + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 100:
        break

cam.release()
cv2.destroyAllWindows()
text_to_speech('Samples Taken. Now moving to next step.')
os.system('2_Facial_Recognition_Dataset_Training.py')
