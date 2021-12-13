import numpy as np
import cv2
from mss import mss
from PIL import Image

mon = {'left': 600, 'top': 300, 'width': 700, 'height': 700}

with mss() as sct:
    while True:
        screenShot = sct.grab(mon)
        img = Image.frombytes(
            'RGB', 
            (screenShot.width, screenShot.height), 
            screenShot.rgb, 
        )



        
        #Afficher les images
        cv2.imshow('Computer Vision', np.array(img))
        if cv2.waitKey(33) & 0xFF in (
            ord('q'), 
            27, 
        ):
            break