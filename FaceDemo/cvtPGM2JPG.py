import os
import numpy as np
import cv2 as cv

pgmset_path = os.path.curdir + '/../' + 'att_faces/'
jpgset_path = os.path.curdir + '/' + 'att_faces_jpg/'
if False == os.path.exists(jpgset_path):
    os.mkdir(jpgset_path)

dirs = os.listdir(pgmset_path)
for item in dirs:
    filedir = os.path.abspath(pgmset_path + '/' + item)
    if item.startswith('s') and os.path.isdir(filedir):
        label = int(item[1:])
        savedir = os.path.abspath(jpgset_path + '/s' + '{0:0>2}'.format(label))
        if False == os.path.exists(savedir):
            os.mkdir(savedir)
        files = os.listdir(filedir)
        for file in files:
            absfile = os.path.join(filedir, file)
            if os.path.isfile(absfile) and '.pgm' in file:
                dotid = file.rfind('.')
                fileidstr = file[:dotid]
                if fileidstr.isnumeric():
                    fileid = int(fileidstr)
                    savefile = os.path.join(savedir, '{0:0>2}'.format(fileid) + '.jpg')
                    img = cv.imread(absfile, cv.IMREAD_COLOR)
                    cv.imwrite(savefile, img)
                    print(absfile + ' done...')
                else:
                    pass