import numpy as np
import cv2
from mss import mss
from PIL import Image

mon = {'left': 1000, 'top': 300, 'width': 700, 'height': 700}

needle_img = cv2.imread("images/objectif2.png",cv2.IMREAD_REDUCED_COLOR_2)

needle_w = needle_img.shape[1]
needle_h = needle_img.shape[0]


with mss() as sct:
    while True:
        screenShot = sct.grab(mon)
        img = Image.frombytes(
            'RGB', 
            (screenShot.width, screenShot.height), 
            screenShot.rgb, 
        )
        # test = cv2.imread(img,cv2.IMREAD_REDUCED_COLOR_2)

        image = np.array(img)

        result = cv2.matchTemplate(image,needle_img,cv2.TM_CCOEFF_NORMED)

        treshold = 0.4

        locations = np.where(result>= treshold)

        locations = list(zip(*locations[::-1]))

        rectangles = []
        for loc in locations:
            rec=[int(loc[0]),int(loc[1]),needle_w,needle_h]
            rectangles.append(rec)

        rectangles, weight = cv2.groupRectangles(rectangles,1,0.91)
        if len(rectangles):
            # print("Needle trouver")


            line_color = (0,255,0)
            line_type = cv2.LINE_4
            marker_color= (255,0,255)
            marker_type = cv2.MARKER_CROSS


            for (x,y,w,h) in rectangles:
                # #Positionne les carré
                # top_left = (x,y)
                # bottom_right = (x+w,y+h)
                # cv.rectangle(haystack_img,top_left,bottom_right,line_color,line_type)
                
                center_x = x +int(w/2)
                center_y = y + int(h/2)
                cv2.drawMarker(image,(center_x,center_y),marker_color,marker_type)
            x = 0
            xPosition = 0
            yPosition = 0
            for x in range(256):
                if xPosition >= 26 : 
                    yPosition +=1
                    xPosition = 0
                x += 1
                xPosition+=1
                # print(xPosition)
                cv2.drawMarker(image,(100+(xPosition*16),15+(yPosition*16)),marker_color,marker_type)
        #Afficher les images
        cv2.imshow('Computer Vision', image)
        if cv2.waitKey(33) & 0xFF in (
            ord('q'), 
            27, 
        ):
            break