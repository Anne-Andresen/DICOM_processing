import glob
import os.path
import numpy as np
import cv2 as cv
import re
# img = []
# templ = []
# path = ''
# path1 = ''
def get_numbers_from_filename(input):
    file = os.path.basename(input)
    print('File:', file)
    filename = os.path.splitext(file)[0]
    return re.search(r'\d+', filename).group(0)

# Missing need to exract specific part of file name

for f in glob.glob('path/*.png'):
    print('Loading new patch')
    img = cv.imread(f)
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    dir = os.path.dirname(os.path.dirname(f))
    # print('Directory path ', dir)
    dirname2 = os.path.split(dir)[1]
    # print('Directory name:', dirname2)
    numb = get_numbers_from_filename(f)
    # print('numb', numb)
    file = os.path.basename(f)
    # print('File:', file)
    y = os.path.splitext(file)[0]
   #  print('Y_ ', y)

    E = [int(x) for x in re.findall('\d+', file)]
    print('E', E)
    print('ZZ', E[4], 'RR', E[5])
    num = int(E[3])
    summation = num+1
    if summation == 66:
        summation = 65
    else:
        summation = summation
    print('Sum', num + 1)

    #patch_num = name[1]
    # s3 = s[]
    # print('S1: ', s1, 'S2: ', s2)
    if len(numb) == 1:
        # number_str.zfill(5)
        numb = numb.zfill(1)
        # print('Numb with 0', numb)
    else:
        numb = numb

    if cv.countNonZero(gray) == 0:
        print('patch is black')
    else:
        #hi= z[0]
        path1 = 'template path'+file
        patch = cv.imread(path1)
        print('patch', patch)
        path12 = 'image path'
        print('path12', path12)

        path = ''
        dir1 = os.path.dirname(os.path.dirname(path))
        print('Directory path1 ', dir1)
        dirname12 = os.path.split(dir1)[1]
        print('Directory name1:', dirname12)
        file1 = os.path.basename(dir1)
        print('File1:', file1)
        y = os.path.splitext(file1)[0]

        template = patch
        print(template)
        print('path', path12 + str(summation) + '.png')
        img = cv.imread(path12 + str(summation) + '.png')


        print('img', img)
        # Works for one lymph node with boundaries  not entirely sure how it will work for multiple.
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
        template_width = 64
        template_height = 64
        k = 10
        print('coordinate', E[4] -k, E[5] + template_width + k)

        #a = name[1]

        #b = [int(x) for x in re.findall('\d+', a)]
        #print('AAAA', name[1])
        y = int(E[4])

        x = int(E[5])
        y1 = y - k
        print('YYY', y1)
        y2 = y + 64 + k
        print('YYY', y2)
        x1 = x- k
        print('YYY', x1)
        x2 = x + 64 + k
        print('YYY', x2)
        roi = img_gray[ y1:y2, x1:x2]

        #roi = img_gray[E[1] -k: E[1] + template_height + k, E[2] - k : E[2] + template_width + k]

        cv.imshow('ROI', roi)
        print('ROI', roi)

        result = cv.matchTemplate(roi, template_gray, cv.TM_CCORR)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print('MAX', max_loc[0], max_val)
        #top_left = max_loc
        top_left = max_loc[0] + E[5], max_loc[1] + E[4]
        h, w = template_gray.shape

        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(img, top_left, bottom_right, (0, 0, 255), 4)
        cv.putText(img, str('LN') + str(E[3]), top_left, cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        print('DONE')

        cv.imwrite(path12 + str(summation) + '.png', img)

        #cv.imshow('Result', img)
        #cv.imshow('Template', template)

        # cv.moveWindow('Template', 10, 50);
        # cv.moveWindow('Result', 150, 50);

