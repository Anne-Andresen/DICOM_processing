import glob
import os.path
import numpy as np
import cv2 as cv
import matplotlib as plt
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
c = '18'
for f in glob.glob('E:\AAU\Patient_8\Dec 4, 2019\png/'+str(c)+'/patches2/LN/LN*.png'):
    print('Loading new patch:', f)
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
    '''
    z = file.split('2019')
    print('Z[0]', z[0], 'Z[1]')
    na = z[0]
    r = file.split('IMG00')[-1]
    s = str(y)
    s1 = r[0]
    s2 = r[1]
    print('S1',s1,'S2', s2)
    name = s.rpartition(s1 + s2)
    patch_number = name[2]
    slice_number = name[1]
    name1 = name[0]
    print('name', name[0])
    print('Name ', patch_number)
    print('Slice', slice_number)
    #pit = patch_number.split('_')
    #print('pit', pit[0])
    '''
    E = [int(x) for x in re.findall('\d+', file)]
    print('E', E)
    print('E[0]', E[0])
    print('ZZ', E[2], 'RR', E[1])
    '''
    num = int(E[])
    summation = num+1
    filanem = file.split('p')
    print('filanem', filanem[1])
    if summation == 66:
        summation = 65
    else:
        summation = summation
    print('Sum', num + 1)
    '''
    # patch_num = name[1]
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

        # hi= z[0]
        #path1 = 'E:\AAU\Patient_8\Dec 4, 2019\png/18/patches1/LN/' + file # patches
        t = file.split('gt_')
        print('t[0]', t[0], 't[1]', t[1])
        path1 = 'E:\AAU\Patient_8\Dec 4, 2019\png/'+str(c)+'/patches1/LN/' + t[0] + 'gt_' + t[1]
        patch = cv.imread(path1)
        print('patch', patch)
        path12 = 'E:\AAU\Patient_8\Dec 6, 2019\png\gt_gt_IMG00' + str(c) # img
        print('path12', path12)

        path = 'E:\AAU\Patient_8\Dec 6, 2019\png\gt_IMG00' + str(c) # predictions
        dir1 = os.path.dirname(os.path.dirname(path))
        print('Directory path1 ', dir1)
        dirname12 = os.path.split(dir1)[1]
        print('Directory name1:', dirname12)
        file1 = os.path.basename(dir1)
        print('File1:', file1)
        y = os.path.splitext(file1)[0]

        template = patch
        print(template)
        print('path', path12 + '.png')
        img1 = cv.imread(path12 + '.png')
        print('IMGIMG', img)

        print('img', img1)
        # Works for one lymph node with boundaries  not entirely sure how it will work for multiple.
        img_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        widt, height = img_gray.shape
        print('DIM: ', widt, height)
        template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
        width, heigt = template_gray.shape
        print('TEMPLATE, DIM:', width, heigt)
        template_width = 32
        template_height = 32
        k = 10
        print('coordinate', E[4], E[5])

        # a = name[1]

        # b = [int(x) for x in re.findall('\d+', a)]
        # print('AAAA', name[1])
        y = int(E[5])

        x = int(E[4])
        y1 = y - k
        print('YYY', y1)
        y2 = y + 32 + k
        print('YYY', y2)
        x1 = x - k
        print('YYY', x1)
        x2 = x + 32 + k
        print('YYY', x2)
        lymph_num = '18'
        img5 = cv.imread('E:\AAU\Patient_8\Dec 6, 2019\png/png/gt_IMG00' + str(c) + '.png')
        img_gray5 = cv.cvtColor(img5, cv.COLOR_BGR2GRAY)
        roi = img_gray[y1:y2, x1:x2]
        roi1 = img_gray5[y1:y2, x1:x2]
        print('ROI', roi.shape)



        # cv.imshow('ROI', roi)

        result = cv.matchTemplate(roi, template_gray, cv.TM_CCORR)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print('MAX', max_loc[0], max_loc[1])
        # top_left = max_loc
        top_left = max_loc[0] + E[5], max_loc[1] + E[4]
        print(top_left)
        h, w = template_gray.shape

        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(img1, top_left, bottom_right, (0, 0, 255), 2)

        cv.putText(img1, str('LN') + str(E[0]), top_left, cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        print('DONE')
        # lymph_num = str(E[4])
        lymph_num = '18'
        cv.imwrite(path12 + '.png', img1)
        # Extract and save template
        img3 = cv.imread('E:\AAU\Patient_8\Dec 6, 2019\png/png/gt_gt_IMG00' + str(c) + '.png') # img
        img4 = cv.imread('E:\AAU\Patient_8\Dec 6, 2019\png/png/gt_IMG00' + str(c) + '.png')
        #template1 = img3[max_loc[1] + E[5]:max_loc[1] + E[5] + 32, max_loc[0] + E[6]:max_loc[0] + E[6] + 32]
        #template2 = img4[max_loc[1] + E[5]:max_loc[1] + E[5] + 32, max_loc[0] + E[6]:max_loc[0] + E[6] + 32]
        template1 = img3[top_left[1]:top_left[1] + 32, top_left[0]:top_left[0]+32]
        template2 = img4[top_left[1]:top_left[1] + 32, top_left[0]:top_left[0]+32]


        print('template', template)
        path = 'E:\AAU\Patient_8\Dec 6, 2019\png/' + str(c)
        cv.imwrite(
            path + '/template/scans/LN_' + str(E[0]) + '_' + str(top_left[1]) + '_' + str(top_left[0]) + '.png',
            template1)
        cv.imwrite(
            path + '/template/pred/LN_' + str(E[0]) + '_' + str(top_left[1]) + '_' + str(top_left[0]) + '.png',
            template2)
        cv.imwrite(
            path + '/template/scans/ROI_' + str(E[0]) + '_' + str(x1) + '_' + str(y1) + '.png',
            roi)
        cv.imwrite(
            path + '/template/pred/ROI_' + str(E[0]) + '_' + str(x1) + '_' + str(y1) + '.png',
            roi1)
# cv.imshow('Result', img)
# cv.imshow('Template', template)

# cv.moveWindow('Template', 10, 50);
# cv.moveWindow('Result', 150, 50);
'''

print('Here')
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)
# img = os.path.join(path1, '00060.pnh')
'''

'''
text.rpartition('offset ')
Out[179]: ('March 1st 2013 ntp[22485] Time server ', 'offset ', '-.0070 sec')
In [169]: text.rpartition('offset ')[-1]
Out[169]: '-.0070 sec'
'''

'''
template = cv.imread('mergmerg_448_384.png')
img = cv.imread('merged1.png')
# Works for one lymph node with boundaries  not entirely sure how it will work for multiple.
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

result = cv.matchTemplate(img_gray, template_gray, cv.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
top_left = max_loc
h, w = template_gray.shape

bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img, top_left, bottom_right, (0, 0, 255), 4)
cv.putText(img, 'LN-1', top_left,cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
cv.imwrite('BB.png', img)
cv.imshow('Result', img)
cv.imshow('Template', template)
# cv.moveWindow('Template', 10, 50);
# cv.moveWindow('Result', 150, 50);

print('Here')
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)
# img = os.path.join(path1, '00060.pnh')
'''
