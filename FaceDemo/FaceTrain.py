import os
import cv2 as cv
import numpy as np

# read image-label map from label file
def Load_csv(filepath, images = [], labels = []):
    # load image-label map
    if filepath != '' and os.path.isfile(filepath) and os.path.exists(filepath):
        # clear images and labels
        images.clear()
        labels.clear()

        try:
            f = open(filepath, 'r')

            for newline in f.readlines():
                items = newline.strip('\n').split(',')
                imagepath = items[0];
                label = int(items[1].strip())
                images.append(imagepath)
                labels.append(label)
                # print(imagepath + ' - ' + str(label))
        finally:
            f.close()
    else:
        print('invalid csv file')

def Face_Train():
    # function call
    labfile = os.path.abspath(os.path.join(os.path.curdir, 'at.txt'))
    if False == os.path.exists(labfile):
        pass
        # create label file

    # label files
    images = []
    labels = []
    Load_csv(labfile, images, labels)

    # convert into numpy arrays
    faces = []
    for item in images:
        face = cv.imread(item, cv.IMREAD_GRAYSCALE)   # convert into gray image
        faces.append(face)

    if len(images) < 1:
        print('Train dataset is not enough...')
    else:
        trainsfaces = faces[0:len(faces) - 10]
        trainlabels = labels[0:len(labels) - 10]
        testfaces = faces[-10:]
        testlabels = labels[-10:]

        # train face recognizer
        recognizer = cv.face_EigenFaceRecognizer.create()
        recognizer.train(faces, np.array(labels))
        #recognizer.train(trainsfaces, np.array(trainlabels))
        recognizer.save('facemodel.yml')
    
        # test face recognizer
        cv.namedWindow('Test')
        for faceitem in testfaces:
            pre_label = recognizer.predict(faceitem)
            img = faceitem.copy()
            cv.putText(img, 's' + str(pre_label[0]), (50, 50), cv.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
            cv.imshow('Test', img)
            cv.waitKey(0)
    
        cv.destroyAllWindows()
# function Face_Train end