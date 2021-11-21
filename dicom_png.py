import os
import pydicom as dicom
import os
import cv2
import numpy as np






# make it True if you want in PNG format
PNG = True
# Specify the folder path to DICOM imgs here
folder_path = " DCM path here"
# The output path of png /jpeg 
jpg_folder_path = "PNG/jpeg path here"
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
