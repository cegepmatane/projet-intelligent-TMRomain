import numpy as np
import cv2
from mss import mss
from PIL import Image

mon = {'left': 0, 'top': 0, 'width': 800, 'height': 800}

image_ennemie = cv2.imread("images/pomme.png",cv2.IMREAD_ANYCOLOR)
with mss() as sct:
    while True:
        screenShot = sct.grab(mon)
        img = Image.frombytes(
            'RGB', 
            (screenShot.width, screenShot.height), 
            screenShot.rgb, 
        )
        image = cv2.cvtColor(np.array(img), cv2.IMREAD_ANYCOLOR)
        result = cv2.matchTemplate(image, image_ennemie, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = image_ennemie.shape[1]
        h = image_ennemie.shape[0]
        threshold = .30
        yloc, xloc = np.where(result >= threshold)

        # print(len(xloc))

        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,255), 2)
        cv2.imshow('Comparaison', image)
        if cv2.waitKey(33) & 0xFF in (
            ord('q'), 
            27, 
        ):
            break