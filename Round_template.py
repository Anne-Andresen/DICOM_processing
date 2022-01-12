import glob
import os
from PIL import Image, ImageDraw
from math import sqrt
from skimage import data
import cv2 as cv
from skimage import io
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
import re
import matplotlib.pyplot as plt
import numpy as np
i = 1
for f in glob.glob('E:/AAU/blob_detection/gt_*.png'):
    image = f
    image = cv.imread(f)
    filename = f
    print(filename)
    file = os.path.basename(filename)
    y = os.path.splitext(file)[0]
    slice = str(y)
    temp1 = re.findall(r'\d+', slice)

    print('YY', temp1)
    slicenumber = temp1[0]
    path1 = 'E:/AAU/blob_detection/gt_gt_IMG' + slicenumber + '.png'
    img2 = io.imread(path1)
    print('IMG2', img2)
    # plt.imshow(blob_img)
    # plt.show()
    # image = data.hubble_deep_field()[0:500, 0:500]
    image_gray = rgb2gray(image)
    real_image_gray = rgb2gray(img2)
    blobs_log = blob_log(image_gray, max_sigma=30, num_sigma=10, threshold=.1)

    # Compute radii in the 3rd column.
    blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

    blobs_dog = blob_dog(image_gray, max_sigma=30, threshold=.1)
    blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)

    blobs_doh = blob_doh(image_gray, max_sigma=30, threshold=.01)
    print('coordinates', blobs_doh)
    # blobs_list = [blobs_log, blobs_dog, blobs_doh]
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
    colors = ['red']
    titles = [
        'Determinant of Hessian']
    sequence = zip(blobs_list, colors)

    fig, ax = plt.subplots(1, 1, figsize=(3, 3), sharex=True, sharey=True)
    # ax = axes.ravel()

    for idx, (blobs, color) in enumerate(sequence):
        # ax.set_title(title)
        ax.imshow(real_image_gray)
        for blob in blobs:
            y, x, r = blob
            c = plt.Circle((x, y), r, color=color, linewidth=0.4, fill=False)
            ax.add_patch(c)
            coord = str(c)
            temp = re.findall(r'\d+', coord)
            print("The numbers list is : ", temp)


            # crop_img = real_img[y:(y + 2 * r+ 5), x:(x + 2 * r+5)]
            res = list(map(int, temp))
            radius_whole = int(temp[2])
            #remainder = int(temp[3])
            print("The numbers list is : " + ' x ' + str(int(res[0])) + ' y ' + str(int(res[1])))

            r = str(radius_whole+ 1) #+ '.' + str(remainder)
            print('r', r)
            r = int(res[2] + 8)
            x = res[0]
            y = res[1]
            img = Image.open(path1).convert("RGB")
            npImage = np.array(img)
            # h, w = img.size
            h = y + r + 8
            w = x + r + 8
            # Create same size alpha layer with circle
            alpha = Image.new('L', img.size, 0)
            draw = ImageDraw.Draw(alpha)
            draw.pieslice([y, x, h, w], 0, 360, fill=255)

            # Convert alpha Image to numpy array
            npAlpha = np.array(alpha)

            # Add alpha layer to RGB
            npImage = np.dstack((npImage, npAlpha))

            # Save with alpha
            Image.fromarray(npImage).save(
                'E:/AAU/blob_detection/blob_templates/Slice_' + str(slicenumber) + '_' + str(res[0]) + '_' + str(res[1]) + '.png')

            # print result


            # crop_img = real_img[y:(y + 2 * r+ 5), x:(x + 2 * r+5)]
            # cv.imwrite('E:/LN_region' + '.png', crop_img)
            print(coord)

        ax.set_axis_off()




print('Done')