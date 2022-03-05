from wand.image import Image as WandImage
from PIL import Image
import numpy as np
import cv2
import os 
os.environ['KMP_DUPLICATE_LIB_OK']='True'

def read_image(path, crop=None, margin=55):
    with WandImage(filename=path) as img:
        if crop is not None:
            img.crop(*crop)
        img.virtual_pixel = 'black'
        img.distort('barrel', (0.2, 0.0, 0.0, 1.0))
        img.save(filename='unwarp_barrel.png')
        img_jjdf = np.array(img)
        cv2.imshow('image',img_jjdf)
        cv2.waitKey(0)
 
def main():
    return read_image('./image/unwarp.jpg')
    
if __name__ == '__main__':
    main()