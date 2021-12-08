import cv2
import os
import pyttsx3


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
recognizer.read('trainer/trainer.yml')  # load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach

font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to remove warning
cam.set(3, 640)  # set video FrameWidth
cam.set(4, 480)  # set video FrameHeight

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

# flag = True

while True:

    ret, img = cam.read()  # read the frames using the above created object

    converted_image = cv2.cvtColor(img,
                                   cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        converted_image,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)  # used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])  # to predict on every single image

        # Check if accuracy is less them 100 ==> "0" is perfect match
        if accuracy < 100:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            accuracy = "  {0}%".format(round(100 - accuracy))
            text_to_speech('Authentication Successful!')
            text_to_speech('Welcome!')
            text_to_speech('Steering Wheel and other functions are now Online.')
            cam.release()

        else:
            id = "unknown"
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            accuracy = "  {0}%".format(round(100 - accuracy))
            # mbox.showinfo('INFO', 'Authentication was not successful. \n Please provide your credentials.')
            text_to_speech('Authentication was not Successful!')
            text_to_speech('Please provide your credentials.')
            os.system('Non_Recognition.py')
            cam.release()

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break

print("Happy Driving")
cam.release()
cv2.destroyAllWindows()
