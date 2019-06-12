import os
import numpy as np
import cv2 as cv

def Take_Photo():
    dataset_path = os.path.curdir + '/' + 'att_faces_jpg/'
    if False == os.path.exists(dataset_path):
        os.mkdir(dataset_path)

    print('Do you want take your photo into face database? (Y or N)')
    choice = input();
    if choice.upper() == 'N':
        return;

    # find existing person number
    nPerson = 1
    for item in os.listdir(dataset_path):
        itempath = os.path.join(dataset_path, item)
        if os.path.isdir(itempath):
            nPerson += 1

    save_dir = os.path.join(dataset_path, 's' + '{0:0>2}'.format(nPerson))
    if False == os.path.exists(save_dir):
        os.mkdir(save_dir)

    # Take my photos
    cap = cv.VideoCapture(0)
    cv.namedWindow('My Face')
    # use opencv pre-trianed xml
    facexml = 'D:/Program Files (x86)/Microsoft Visual Studio/Shared/Python36_64/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml'
    eyexml = 'D:/Program Files (x86)/Microsoft Visual Studio/Shared/Python36_64/Lib/site-packages/cv2/data/haarcascade_eye.xml'
    face_cascade = cv.CascadeClassifier(facexml)
    eye_cascade = cv.CascadeClassifier(eyexml)

    nNum = 10   # 10 photos for each person
    i = 1
    while True:
        ret, frame = cap.read()
        cv.imshow('My Face', frame)

        key = cv.waitKey(200)
        if key == 0x0D:
            # get my face ROI
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            gray = cv.equalizeHist(gray)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            frame_tp = np.zeros(frame.shape, np.uint8)
            frame_tp = frame.copy()
            for (x,y,w,h) in faces:
                cv.rectangle(frame_tp, (x,y), (x + w,y + h), (0,255,0), 2)
                roiGray = gray[y:y + h, x:x + w]
                roiColor = frame[y:y + h, x:x + w]
            cv.imshow('My Face', frame_tp)
            # save face to local file
            if len(faces) > 0:
                (x,y,w,h) = faces[0]
                face = frame[y:y + h,x:x + w]
                cv.imshow('My Face', face)
                face = cv.resize(face, (92,112))    # resize same size with dataset
                savefile = save_dir + '/' + '{0:0>2}'.format(i) + '.jpg'
                if os.path.exists(savefile):
                    os.remove(savefile)
                cv.imwrite(savefile, face)
                i += 1
            else:
                print('no face detected...')
            if nNum < i:
                print('Take photo done...')
                break
    
        # Esc to break
        elif key == 0x1B:
            print('quit take photo')
            break;

    cap.release()
    cv.destroyAllWindows()
# function Take_Photo end
