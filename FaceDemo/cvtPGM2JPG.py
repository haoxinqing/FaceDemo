import os
import numpy as np
import cv2 as cv
import urllib.request
import zipfile as zip
import hashlib as hash

def Download_Data():
    pgmset_path = os.path.curdir + '/../' + 'att_faces/'
    jpgset_path = os.path.curdir + '/' + 'att_faces_jpg/'
    if False == os.path.exists(jpgset_path):
        os.mkdir(jpgset_path)

    # Download ORL face database from web
    if False == os.path.exists(pgmset_path):
        os.mkdir(pgmset_path)

        temp_path = os.path.curdir + '/../' + 'temp/'
        zip_file = temp_path + 'att_faces.zip'
        if True == os.path.exists(zip_file):
            # check file hash correct code is 'ea6281c63bb2e68a64c046957a749086'
            hashcode = 'ea6281c63bb2e68a64c046957a749086'
            try:
                f = open(zip_file, 'rb')
                bytes = f.read()
            finally:
                if f:
                    f.close()
            code = hash.md5()
            code.update(bytes)
            hex = code.hexdigest()
            print(hex)
            if hex != hashcode:
                # not match, delete it
                os.remove(zip_file);

        if False == os.path.exists(zip_file):
            if False == os.path.exists(temp_path):
                os.mkdir(temp_path)
            # download ORL
            download_url = 'http://www.cl.cam.ac.uk/Research/DTG/attarchive/pub/data/att_faces.zip'
            zip_file = temp_path + 'att_faces.zip'
            urllib.request.urlretrieve(download_url, zip_file);
        # extract zip file
        f = zip.ZipFile(zip_file, 'r')
        for file in f.namelist():
            f.extract(file, pgmset_path)
        f.close()


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
# function Download_Data end