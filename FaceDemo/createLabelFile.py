import os
import sys

dataset_path = os.path.abspath(os.path.curdir + '/' + 'att_faces_jpg/')
labfile = os.path.abspath(os.path.join(os.path.curdir, 'at.txt'))
if os.path.exists(labfile):
    os.remove(labfile)

try:
    f = open(labfile, 'w')
    # create dataset path-label file
    items = os.listdir(dataset_path)
    items.sort()
    for item in items:
        if item.startswith('s'):
            nNum = item[1:]
            if nNum.isnumeric():
                nLabel = int(nNum) - 1;
                files = os.listdir(os.path.join(dataset_path, item))
                files.sort()
                for file in files:
                    if os.path.isfile(os.path.join(dataset_path, item, file)):
                        filepath = os.path.abspath(os.path.join(dataset_path, item, file))
                        # write a new line
                        f.write(filepath + ', ' + str(nLabel) + '\n');
except OSError as err:
    print('OS error: {0}'.format(err))
except:
    print("Unexpected error:", sys.exc_info()[0])
finally:
    if f:
        f.close()