import cv2
import numpy as np
from PIL import Image
import os
import pyttsx3


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


text_to_speech('Welcome. Here we will train the machine for the samples taken from the previous program.')
# Path for face image database
path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");


# function to get the images and label data
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
        img_numpy = np.array(PIL_img, 'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)

    return faceSamples, ids


text_to_speech('Training model for the face samples. It will take a few seconds. Wait ...')
faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.write('trainer/trainer.yml')  # recognizer.save() worked on Mac, but not on Pi

# Print the number of faces trained and end program
# print("\n {0} faces trained. Exiting Program".format(len(np.unique(ids))))

text_to_speech('Model Trained. Go back to the Welcome Interface.')
print('\n Either proceed to the next file or \n')
print('\n Go back to the Welcome Interface.')