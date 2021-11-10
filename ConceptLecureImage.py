import cv2
import numpy as np

image_jeu = cv2.imread("images/Test_Image_Base.jpg",cv2.IMREAD_GRAYSCALE)
image_ennemie = cv2.imread("images/Test_Gapper.png",cv2.IMREAD_GRAYSCALE)


#Affichage des images 
# cv2.imshow("Image Jeu",image_jeu)
# cv2.waitKey()
# cv2.destroyAllWindows()
#image_ennemie = cv2.resize(image_ennemie, (100, 100))
# cv2.imshow("Image Ennemie",image_ennemie)
# cv2.waitKey()
# cv2.destroyAllWindows()

#Comparaison des images
result = cv2.matchTemplate(image_jeu, image_ennemie, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
w = image_ennemie.shape[1]
h = image_ennemie.shape[0]


threshold = .40
yloc, xloc = np.where(result >= threshold)

for (x, y) in zip(xloc, yloc):
    cv2.rectangle(image_jeu, (x, y), (x + w, y + h), (0,255,255), 2)

    
# cv2.rectangle(image_jeu, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
cv2.imshow("Comparaison",image_jeu)
cv2.waitKey()
cv2.destroyAllWindows()