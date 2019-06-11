import os
import cv2 as cv

'''
real time face predict demo
'''

# use opencv pre-trianed xml
facexml = 'D:/Program Files (x86)/Microsoft Visual Studio/Shared/Python36_64/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml'
face_cascade = cv.CascadeClassifier(facexml)
recognizer = cv.face_EigenFaceRecognizer.create()
recognizer.read('./facemodel.yml')

cv.namedWindow('demo')
cap = cv.VideoCapture(0)
while cap.isOpened():
    # show real-time video
    ret, frame = cap.read()
    if ret == False:
        print('open live video failed')
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) > 0:
        for (x,y,w,h) in faces:
            cv.rectangle(frame, (x,y), (x + w,y + h), (0,255,0), 2)
            face = gray[y:y + h, x:x + w]
            face = cv.resize(face, (92,112))    # resize same size with dataset
            label = recognizer.predict(face)
            labelstr = str(label[0])
            cv.putText(frame, 's' + labelstr, (x, y), cv.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 2)
            cv.imshow('demo', frame)

    # press 'ESC' to break
    key = cv.waitKey(200);
    if key == 0x1B:
        break;

# done
cap.release()
cv.destroyAllWindows()
print('done...')
