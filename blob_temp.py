import cv2 as cv
import numpy as np


path = 'E:/AAU/blob_detection/gt_IMG0018.png'
path1 = 'E:/AAU/blob_detection/gt_gt_IMG0018.png'
blob_img = cv.imread(path, cv.IMREAD_GRAYSCALE)
blob_img = cv.resize(blob_img,(768, 768))

real_img = cv.imread(path1, cv.IMREAD_GRAYSCALE)
real_img = cv.resize(real_img,(768, 768))


from math import sqrt
from skimage import data
from skimage import io
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
import re
import matplotlib.pyplot as plt

img2 = io.imread(path1)
print('IMG2', img2)
#plt.imshow(blob_img)
#plt.show()
#image = data.hubble_deep_field()[0:500, 0:500]
image_gray = rgb2gray(blob_img)
real_image_gray = rgb2gray(img2)
blobs_log = blob_log(image_gray, max_sigma=30, num_sigma=10, threshold=.1)

# Compute radii in the 3rd column.
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

blobs_dog = blob_dog(image_gray, max_sigma=30, threshold=.1)
blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)

blobs_doh = blob_doh(image_gray, max_sigma=30, threshold=.01)
print('coordinates', blobs_doh)
#blobs_list = [blobs_log, blobs_dog, blobs_doh]
'''
colors = ['yellow', 'lime', 'red']
titles = ['Laplacian of Gaussian', 'Difference of Gaussian',
          'Determinant of Hessian']
sequence = zip(blobs_list, colors, titles)

fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharex=True, sharey=True)
ax = axes.ravel()

for idx, (blobs, color, title) in enumerate(sequence):
    ax[idx].set_title(title)
    ax[idx].imshow(image)
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
        ax[idx].add_patch(c)
    ax[idx].set_axis_off()
'''
blobs_list = [blobs_doh]
colors = [ 'red']
titles = [
          'Determinant of Hessian']
sequence = zip(blobs_list, colors)

fig, ax = plt.subplots(1, 1, figsize=(3, 3), sharex=True, sharey=True)
#ax = axes.ravel()

for idx, (blobs, color) in enumerate(sequence):
    #ax.set_title(title)
    ax.imshow(real_img)
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=0.4, fill=False)
        ax.add_patch(c)
        coord = str(c)
        temp = re.findall(r'\d+', coord)
        #crop_img = real_img[y:(y + 2 * r+ 5), x:(x + 2 * r+5)]
        res = list(map(int, temp))

        # print result
        print("The numbers list is : " + str(res))
        print("The numbers list is : "  + ' x ' + str(int(res[0])) + ' y ' + str(int(res[1])))
        x = res[0]
        y = res[1]
        r = str(res[2] +1) + '.' + str(res[3])
        print('r', r)
        r = int(res[2] + 1)

        #crop_img = real_img[y:(y + 2 * r+ 5), x:(x + 2 * r+5)]
        #cv.imwrite('E:/LN_region' + '.png', crop_img)
        print(coord)
    ax.set_axis_off()
plt.tight_layout()
plt.show()
#print(c)


'''
cv.imshow('Image', blob_img)
cv.waitKey(0)
img = cv.bitwise_not(blob_img)

params = cv.SimpleBlobDetector_Params()
detector = cv.SimpleBlobDetector_create(params)

keypoints = detector.detect(img)
print('KEY_points', keypoints)
img = cv.bitwise_not(img)
im_with_keypoints = cv.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow('Detections', im_with_keypoints)
cv.waitKey(0)
'''

'''

params = cv2.SimpleBlobDetector_Params()
# Change thresholds
params.minThreshold = 10;    # the graylevel of images
params.maxThreshold = 200;

params.filterByColor = True
params.blobColor = 255

# Filter by Area
params.filterByArea = True
params.minArea = 300

detector = cv2.SimpleBlobDetector(params)

# Detect blobs.
keypoints = detector.detect(im)

print (keypoints)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
'''