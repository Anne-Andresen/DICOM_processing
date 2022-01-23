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
    boxA = [0., 0., 10., 10.]
    boxB = [1., 1., 11., 11.]
    '''
    boxA = [E[3]-dimensions[1], E[2]-dimensions[1], E[3] + dimensions[1], E[2] + dimensions[1]]
    boxB = [E1[2]-dimensions[1], E1[3]-dimensions[1], E1[2] + dimensions[1], E1[3] + dimensions[1]]
    # find corners of template
    correct = bb_intersection_over_union(boxA, boxB)
    print('Correct solution - also analytical: {0}\n'
          'Solution by published function: {1}\n'
          'Solution by correction (ptyshevs): {2}'.format(correct, '0.704225352113', '0.680672268908'))

    print('Normalizing coordinates in a 100x100 coordinate system')
    boxA = [a / 100. for a in boxA]
    boxB = [b / 100. for b in boxB]

    correct = bb_intersection_over_union(boxA, boxB)

    print('Correct solution - also analytical: {0}\n'
          'Solution by published function: {1}\n'
          'Solution by correction: {2}'.format(correct, '0.964445166004', '0.680672268908'))
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