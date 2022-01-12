from PIL import Image, ImageChops
import glob
import os
import cv2 as cv


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


for f in glob.glob('E:/AAU/blob_detection/blob_templates/Slice*.png'):
    image = f
    im = Image.open(image)
    img = trim(im)
    # img.show()
    filename = f
    print(filename)
    file = os.path.basename(filename)
    y = os.path.splitext(file)[0]
    print('YY', y)
    img.save('E:/AAU/blob_detection/blob_templates/' + y + '.png')

print('Done')
