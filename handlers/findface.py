import cv2
import cv2.cv2 as cv2

def find_face(name):
    face_cascade = cv2.CascadeClassifier(r'D:\face&audio_bot\handlers\haarcascade_frontalface_default.xml') # path to haarcascade_frontalface_default.xml
    path = r'D:\face&audio_bot\/' # path to Photo
    name = r'{0}'.format(name)
    img = cv2.imread(path+str(name))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    return faces

