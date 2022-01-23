import cv2 as cv
import os
import glob
import re
def bb_intersection_over_union(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = abs(max((xB - xA, 0)) * max((yB - yA), 0))
    if interArea == 0:
        return 0
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = abs((boxA[2] - boxA[0]) * (boxA[3] - boxA[1]))
    boxBArea = abs((boxB[2] - boxB[0]) * (boxB[3] - boxB[1]))

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)

    # return the intersection over union value
    return iou

'''-----------------------------------------DEFINITIONS---------------------------------------------------'''
import glob
import os
import cv2 as cv
import numpy as np
import re
from math import sqrt
ed = []

def get_file_names_with_strings(str_list, path):
    full_list = os.listdir(path)
    final_list = [nm for ps in str_list for nm in full_list if ps in nm]

    return final_list
def get_file_names_with_strings_depth_constraint(str_list, y_list):
    full_list = y_list
    final_list2 = [nm for ps in str_list for nm in full_list if ps in nm]

    return final_list2




for i in range(15, 66):
    file1 = open('LN.txt', 'a')
    # pris = ' Mean of slice Euclidean distance: ' + str(temp1[0]) + ' ' + str(Dec46)
    file1.write('NEW SLICE ' + str(i))
    file1.write('\n')
    file1.write('\n')
    file1.close()

    for f in glob.glob('E:/AAU/blob/LN/LN*Slice_00'+str(i)+'*.png'):
        img = cv.imread(f)
        file = os.path.basename(f)
        y = os.path.splitext(file)[0]
        dimensions = img.shape
        slice = str(y)
        temp1 = re.findall(r'\d+', slice)
        print('Numbers in name: ', temp1)
        temp1 = re.findall(r'\d+', slice)
        print('Numbers in name: ', temp1)
        slice_numb = str(temp1[1])
        slice = str(slice_numb[2] + slice_numb[3])
        lymph_numb = str(temp1[0])
        print('Slice number', slice)
        print('lymph number', lymph_numb)
        print('euihf', 'LN_' + lymph_numb + '_' + 'Slice' + slice_numb + '_')
        Dec4 = get_file_names_with_strings([str('LN_' + lymph_numb + '_Slice_00' + slice + '_')], 'E:/AAU/blob/LN/')
        print('Dec 4 list', Dec4)
        Dec6 = get_file_names_with_strings([str('LN_' + lymph_numb + '_' + 'Slice' + '_' + slice + '_')],
                                           'E:/AAU/blob/Dec 6, 2019/png/templates/')
        print('Dec 6 list', Dec6)
        Dec13 = get_file_names_with_strings([str('LN_' + lymph_numb + '_' + 'Slice' + '_' + slice + '_')],
                                            'E:/AAU/blob/Dec 13, 2019/png/templates/')
        print('Dec 13 list', Dec13)
        Dec20 = get_file_names_with_strings([str('LN_' + lymph_numb + '_' + 'Slice' + '_' + slice + '_')],
                                            'E:/AAU/blob/Dec 20, 2019/png/templates/')
        print('Dec 20 list', Dec20)
        Jan3 = get_file_names_with_strings([str('LN_' + lymph_numb + '_' + 'Slice' + '_' + slice + '_')],
                                           'E:/AAU/blob/Jan 3, 2020/png/templates/')
        print('Jan 3 list', Jan3)
        # file1 = os.path.basename()
        y1 = os.path.splitext(Dec4[0])[0]
        print(y1)
        # file2 = os.path.basename(f)
        y2 = os.path.splitext(Dec6[0])[0]
        # file3 = os.path.basename(f)
        y3 = os.path.splitext(Dec13[0])[0]
        # file4 = os.path.basename(f)
        y4 = os.path.splitext(Dec20[0])[0]
        #
        y5 = os.path.splitext(Jan3[0])[0]
        tempdec4 = re.findall(r'\d+', y1)
        tempdec6 = re.findall(r'\d+', y2)
        tempdec13 = re.findall(r'\d+', y3)
        tempdec20 = re.findall(r'\d+', y4)
        tempjan3 = re.findall(r'\d+', y5)
        print(tempdec4)
        print(tempdec6)
        print(tempdec13)
        print(tempdec20)
        # print(tempjan3)
        boxA46 = [int(tempdec4[2]) - int(dimensions[1]), int(tempdec4[3]) - int(dimensions[1]), int(tempdec4[2]) + int(dimensions[1]), int(tempdec4[3]) + int(dimensions[1])]
        boxB46 = [int(tempdec6[3]) - int(dimensions[1]), int(tempdec6[2]) - int(dimensions[1]), int(tempdec6[3]) + int(dimensions[1]), int(tempdec6[2]) + int(dimensions[1])]
        boxA613 = [int(tempdec6[2]) - int(dimensions[1]), int(tempdec6[3]) - int(dimensions[1]), int(tempdec6[2]) + int(dimensions[1]), int(tempdec6[3]) + int(dimensions[1])]
        boxB613 = [int(tempdec13[2]) - int(dimensions[1]), int(tempdec13[3]) - int(dimensions[1]), int(tempdec13[2]) + int(dimensions[1]), int(tempdec13[3]) + int(dimensions[1])]
        boxA1320 = [int(tempdec13[2]) - int(dimensions[1]), int(tempdec13[3]) - int(dimensions[1]), int(tempdec13[2]) + int(dimensions[1]), int(tempdec13[3]) + int(dimensions[1])]
        boxB1320 = [int(tempdec20[2]) - int(dimensions[1]), int(tempdec20[3]) - int(dimensions[1]), int(tempdec20[2]) + int(dimensions[1]), int(tempdec20[3]) + int(dimensions[1])]
        boxA203 = [int(tempdec20[2]) - int(dimensions[1]), int(tempdec20[3]) - int(dimensions[1]), int(tempdec20[2]) + int(dimensions[1]), int(tempdec20[3]) + int(dimensions[1])]
        boxB203 = [int(tempjan3[2]) - int(dimensions[1]), int(tempjan3[3]) - int(dimensions[1]), int(tempjan3[2]) + int(dimensions[1]), int(tempjan3[3]) + int(dimensions[1])]
        correct46 = bb_intersection_over_union(boxA46, boxB46)
        print('Correct solution - also analytical: {0}\n'
              .format(correct46))

        print('Normalizing coordinates in a 100x100 coordinate system')
        boxA46 = [a / 100. for a in boxA46]
        boxB46 = [b / 100. for b in boxB46]

        correct613 = bb_intersection_over_union(boxA613, boxB613)
        print('Correct solution - also analytical: {0}\n'
              .format(correct613))

        print('Normalizing coordinates in a 100x100 coordinate system')
        boxA613 = [a / 100. for a in boxA613]
        boxB613 = [b / 100. for b in boxB613]


        correct1320 = bb_intersection_over_union(boxA1320, boxB1320)
        print('Correct solution - also analytical: {0}\n'
              .format(correct1320))

        print('Normalizing coordinates in a 100x100 coordinate system')
        boxA1320 = [a / 100. for a in boxA1320]
        boxB1320 = [b / 100. for b in boxB1320]

        correct203 = bb_intersection_over_union(boxA203, boxB203)
        print('Correct solution - also analytical: {0}\n'
              .format(correct203))

        print('Normalizing coordinates in a 100x100 coordinate system')
        boxA203 = [a / 100. for a in boxA203]
        boxB203 = [b / 100. for b in boxB203]
        '''
        Dec46 = sqrt(((int(tempdec6[3]) - int(tempdec4[2])) ** 2) + (
                    (int(tempdec6[2]) - int(tempdec4[3])) ** 2))  # Top left corner
        Dec613 = sqrt(((int(tempdec13[2]) - int(tempdec6[2])) ** 2) + ((int(tempdec13[3]) - int(tempdec6[3])) ** 2))
        Dec1320 = sqrt(((int(tempdec20[2]) - int(tempdec13[2])) ** 2) + ((int(tempdec20[3]) - int(tempdec13[3])) ** 2))
        # Dec203 = sqrt(((int(tempjan3[2]) - int(tempdec20[2])) ** 2) + ((int(tempjan3[3]) - int(tempdec20[3])) ** 2))

        print('euclidean', Dec46)
        print('euclidean', Dec613)
        print('euclidean', Dec1320)
        # print('euclidean', Dec20)
        '''
        # print('euclidean', Euclidean_distance2)
        # print('euclidean', Euclidean_distance3
        # print('euclidean', Euclidean_distance4)
        #        mean = (Euclidean_distance1 + Euclidean_distance2 + Euclidean_distance3 + Euclidean_distance4)/4
        #        print('Mean for slice', mean)
        #ed.append(Dec46)
        file1 = open('IoU.txt', 'a')
        # pris = ' Mean of slice Euclidean distance: ' + str(temp1[0]) + ' ' + str(Dec46)
        file1.write('Central distance 4 to 6: ' + str(temp1[0]) + ' Slice_' + str(temp1[1]) + ' ' + str(correct46))
        file1.write('\n')
        file1.write('Central distance 6 to 13: ' + str(temp1[0]) + ' Slice_' + str(temp1[1]) + ' ' + str(correct613))
        file1.write('\n')
        file1.write('Central distance 13 to 20: ' + str(temp1[0]) + ' Slice_' + str(temp1[1]) + ' ' + str(correct1320))
        file1.write('\n')
        file1.write('Central distance 20 to 3: ' + str(temp1[0]) + ' Slice_' + str(temp1[1]) +' ' + str(correct203))
        file1.write('\n')
        file1.close()

    i = i + 1

        # Euclidean_distance1 = sqrt(((Y - Y_temp) ** 2) + ((X - X_temp) ** 2))  # Top left corner









    '''
if __name__ == '__main__':
    path1 = 'E:/AAU/blob/IoU/LN_1_Slice_0054_579_413.png'
    path2 = 'E:/AAU/blob/IoU/6/LN_1_Slice_54_395_587.png'
    img = cv.imread(path1)
    dimensions = img.shape
    file = os.path.basename(path1)
    # print('File:', file)
    y = os.path.splitext(file)[0]
    E = [int(x) for x in re.findall('\d+', file)]
    print('E', E)
    file1 = os.path.basename(path2)
    # print('File:', file)
    y1 = os.path.splitext(file1)[0]
    E1 = [int(x) for x in re.findall('\d+', file1)]
    print('E', E1)
    '''
    '''
    boxA = [0., 0., 10., 10.]
    boxB = [1., 1., 11., 11.]
    
    boxA = [E[2]-dimensions[1], E[3]-dimensions[1], E[2] + dimensions[1], E[3] + dimensions[1]]
    boxB = [E1[3]-dimensions[1], E1[2]-dimensions[1], E1[3] + dimensions[1], E1[2] + dimensions[1]]
    # find corners of template
    correct = bb_intersection_over_union(boxA, boxB)
    print('Correct solution - also analytical: {0}\n'
          .format(correct))

    print('Normalizing coordinates in a 100x100 coordinate system')
    boxA = [a / 100. for a in boxA]
    boxB = [b / 100. for b in boxB]

    correct = bb_intersection_over_union(boxA, boxB)

    print('Correct solution - also analytical: {0}\n'
          .format(correct))
    '''
'''
    print('Two boxes with no overlap')
    boxA = [0., 0., 10., 10.]
    boxB = [12., 12., 22., 22.]
    correct = bb_intersection_over_union(boxA, boxB)

    print('Correct solution - also analytical: {0}\n'
          'Solution by published function: {1}\n'
          'Solution by correction (ptyshevs): {2}'.format(correct, '0.0', '0.0204081632653'))

    print('Example in the comments from ptyshevs')
    boxA = [0., 0., 2., 2.]
    boxB = [1., 1., 3., 3.]
    correct = bb_intersection_over_union(boxA, boxB)

    print('Correct solution - also analytical: {0}\n'
          'Solution by published function: {1}\n'
          'Solution by correction (ptyshevs): {2}'.format(correct, '0.285714285714', '0.142857142857'))
    
'''