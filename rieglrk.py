import numpy as np
import glob
import cv2 as cv
import math
import re
import os

filenames = []
interest = []
file_name_x = []
file_name_y = []
j = 1
for f in glob.glob('E:/AAU/blob_detection/blob_templates/18/Slice*.png'):
    file = f
    template = cv.imread(f)
    file = os.path.basename(file)
    y = os.path.splitext(file)[0]
    slice = str(y)
    temp1 = re.findall(r'\d+', slice)
    print('Numbers in name: ', temp1)
    X = temp1[1]
    Y = temp1[2]
    print('x', X, 'y', Y)
    x1 = int(X) + 1
    x2 = int(X) + 2
    x3 = int(X) + 3

    x5 = int(X) - 3
    x6 = int(X) - 1
    x7 = int(X) - 2
    x8 = int(X) - 3
    x9 = int(X) - 4
    print('Xs', X, x1, x2, x3, x5, x6, x7, x8, x9)
    y1 = int(int(Y) +1)
    y2 = int(Y) + 2

    y3 = int(Y) + 3
    y4 = int(Y) + 4
    y5 = int(Y) - 1
    y6 = int(Y) - 2
    y7 = int(Y) - 3
    y8 = int(Y) - 4

    print('Ys', Y, y1, y2, y3, y4, y5, y6, y7, y8)
    # Cehcj is part of name in folder
    for i in glob.glob('E:/AAU/blob_detection/blob_templates/Slice*.png'):
        file1 = i

        # template = cv.imread(f)
        file12 = os.path.basename(file1)
        y1 = os.path.splitext(file12)[0]
        filenames.append(y1)
        #print('done')
    '''
    for i in range(len(filenames)):
        if X or x1 or x2 or x3 or x4 or x5 or x6 or x7 or x8 or x9 == filenames[i]:
            print("\nElement found at Position:", i + 1)
    for i in range(len(filenames)):
        if any(s.endswith(Y or y1 or y2 or y3 or y4 or y5 or y6 or y7 or y8 or y9) for s in filenames):
            print("\nElement found at Position:", i + 1)
            print('Element' [i])

    '''


    def get_file_names_with_strings(str_list, path):
        full_list = os.listdir(path)
        final_list = [nm for ps in str_list for nm in full_list if ps in nm]

        return final_list


    x_coord = [X, x1, x2, x3, x5, x6, x7, x8, x9]
    print('xcood',X)
   # files_x = get_file_names_with_strings(['_' + str(X)  + '_' + str(Y) or str(y1) or str(y2) or str(y3) or str(y4), '_' + str(x1) + '_', '_' + str(x2) + '_', '_' + str(x3) + '_', '_' + str(x4) + '_', '_' + str(x5) + '_', '_' + str(x6) + '_', '_' + str(x7) + '_', '_' + str(x8) + '_', '_' + str(x9) + '_'])
    '''
    files_x = get_file_names_with_strings(
        ['_' + str(X) + '_' + str(Y) , '_' + str(X) + '_' + str(y1),
         '_' + str(x2) + '_', '_' + str(x3) + '_', '_' + str(x4) + '_', '_' + str(x5) + '_', '_' + str(x6) + '_',
         '_' + str(x7) + '_', '_' + str(x8) + '_', '_' + str(x9) + '_'])
    '''
    #files_x1 = get_file_names_with_strings(['_' + str(X) + '_', '_' + str(x1) + '_', '_' + str(x2) + '_', '_' + str(x3) + '_', '_' + str(x5) + '_', '_' + str(x6) + '_', '_' + str(x7) + '_', '_' + str(x8) + '_', '_' + str(x9) + '_'] and ['_' + str(Y) + '.png', '_' + str(y1) + '.png', '_' + str(y2) + '.png', '_' + str(y3) + '.png', '_' + str(y4) + '.png'])
    files_x1 = get_file_names_with_strings(
        ['_' + str(X) + '_', '_' + str(x1) + '_', '_' + str(x2) + '_', '_' + str(x3) + '_', '_' + str(x5) + '_',
         '_' + str(x6) + '_', '_' + str(x7) + '_', '_' + str(x8) + '_', '_' + str(x9) + '_'] , path='E:/AAU/blob_detection/blob_templates/18/')

    #files_x = get_file_names_with_strings(['_' + X + '_' + y1])
    LN_numb = j
    for i in range(len(files_x1)):
        print('i', i)
        #os.rename(r'E:/AAU/blob_detection/blob_templates/'+files_x1[i-1], r'E:/AAU/blob_detection/LN/LN_' + str(j) + '_' + files_x1[i-1])
        #tempel = cv.imread('E:/AAU/blob_detection/blob_templates/' + files_x1[i-1])
        #cv.imwrite('E:/AAU/blob_detection/LN/LN_' + str(j) + files_x1[i-1], tempel)
        #os.remove('E:/AAU/blob_detection/blob_templates/' + files_x1[i-1])
    j = j + 1
    print('files_x', files_x1, 'len', len(files_x1))

    #print('tab', '_' + str(X)  + '_' + str(y1))
    '''
    files_y = get_file_names_with_strings(['_' + str(Y) + '.png', '_' + str(y1) + '.png', '_' + str(y2) + '.png', '_' + str(y3) + '.png', '_' + str(y4) + '.png', '_' + str(y5) + '.png', '_' + str(y6) + '.png', '_' + str(y7) + '.png', '_' + str(y8) + '.png', '_' + str(y9) + '.png'])
    print('Files_y', files_y)
    '''




    '''
    is_found = X or x1 or x2 or x3 or x4 or x5 or x6 or x7 or x8 or x9 in filenames
    is_found1 = Y or y1 or y2 or y3 or y4 or y5 or y6 or y7 or y8 or y9 in filenames

    if is_found:
        print("Its in X!")
    elif is_found1:
        print("its in Y")

    else:
        print('New lymph node')

    '''

print('program done')
