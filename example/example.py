# @Time    : 2019/4/18 0:54
# @Author  : Noah
# @File    : face_recognition.py
# @Software: PyCharm
# @description: use OpenCV get number of face
import cv2

image_path = r'./5903040bf4146.jpg'

face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(

    gray,

    scaleFactor=1.15,

    minNeighbors=5,

    minSize=(5, 5),

    flags=cv2.CASCADE_SCALE_IMAGE

)

print("{0} faces were found".format(len(faces)))

for (x, y, w, h) in faces:

    cv2.circle(image, ((x + x + w) // 2, (y + y + h) // 2), w // 2, (0, 255, 0), 2)

cv2.imshow("The find faces!", image)

cv2.waitKey(0)
