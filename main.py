import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

haystack_img = cv.imread("images/SnakeSimple2.png",cv.IMREAD_REDUCED_COLOR_2)
needle_img = cv.imread("images/objectif2.png",cv.IMREAD_REDUCED_COLOR_2)

needle_w = needle_img.shape[1]
needle_h = needle_img.shape[0]

result = cv.matchTemplate(haystack_img,needle_img,cv.TM_CCOEFF_NORMED)

treshold = 0.55

locations = np.where(result>= treshold)

locations = list(zip(*locations[::-1]))

rectangles = []
for loc in locations:
    rec=[int(loc[0]),int(loc[1]),needle_w,needle_h]
    rectangles.append(rec)

rectangles, weight = cv.groupRectangles(rectangles,1,0.91)


# cv.imshow("Result",result)
# cv.waitKey()


if len(rectangles):
    print("Needle trouver")


    line_color = (0,255,0)
    line_type = cv.LINE_4
    marker_color= (255,0,255)
    marker_type = cv.MARKER_CROSS


    for (x,y,w,h) in rectangles:
        # #Positionne les carré
        # top_left = (x,y)
        # bottom_right = (x+w,y+h)
        # cv.rectangle(haystack_img,top_left,bottom_right,line_color,line_type)
        
        center_x = x +int(w/2)
        center_y = y + int(h/2)
        cv.drawMarker(haystack_img,(center_x,center_y),marker_color,marker_type)

    cv.imshow("Resultas", haystack_img)
    cv.waitKey()





# min_val,max_val,min_loc,max_loc =cv.minMaxLoc(result)

# print("Best match top left position : %s " % str(max_loc))
# print ("Best match confidence : %s " % max_val)

# if(max_val >= treshold):
#     print("needle trouver")

#     needle_w = needle_img.shape[1]
#     needle_h = needle_img.shape[0]

#     top_left= max_loc
#     bottom_right = (top_left[0]+needle_w, top_left[1] + needle_h)


#     cv.rectangle(haystack_img,top_left,bottom_right,color=(0,255,0),thickness=2,lineType=cv.LINE_4)

#     cv.imshow("Result", haystack_img)
#     cv.waitKey()
# else:
#     print("needle non trouver")