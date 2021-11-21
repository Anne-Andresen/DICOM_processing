import os
# dcm_folder= 'D:\Patient-1\Patient_1\Dec 9, 2020/registered/'
# PNG_folder= '/Users/riaroque/Desktop/PNG folder'
import pydicom as dicom
import os
import cv2
import numpy as np
import PIL # optional
from pydicom.pixel_data_handlers.util import apply_voi_lut
from skimage import exposure




# make it True if you want in PNG format
PNG = True
# Specify the .dcm folder path
folder_path = "D:\Patient-1\Patient_1\Dec 9, 2020/registered/"
# Specify the output jpg/png folder path
jpg_folder_path = "D:\Patient-1\Patient_1\Dec 9, 2020/png/"
images_path = os.listdir(folder_path)
for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    pixel_array_numpy = ds.pixel_array
    img = pixel_array_numpy - np.min(pixel_array_numpy)
    img = (img / np.max(img)) * 255

    if PNG == False:
        image = image.replace('.dcm', '.jpg')
    else:
        image = image.replace('.dcm', '.png')
    # cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    cv2.imwrite(os.path.join(jpg_folder_path, image), img)
    if n % 50 == 0:
        print('{} image converted'.format(n))