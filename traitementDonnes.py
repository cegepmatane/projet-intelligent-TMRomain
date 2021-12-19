import re
import math
#Recuperer les donnée de position du serpent de la pomme et de la grille en generale
def grilleDeDonneeExterne(oldgrille):
    # print(oldgrille)
    #Separer les differente ligne recuperer en innerHTML
    matches = re.findall(r'<br>.+?<br>',oldgrille) 
    grilleTraiter = []

    # print(len(matches))
    x=0
    y=0
    for submatch in matches:
        submatch = submatch.replace("<br>","")
        rematches = re.split(']',submatch) 
        cleanRematches = [s.replace("[", "") for s in rematches]
        del cleanRematches[-1]
        
        for ultraSubmatch in cleanRematches:
            grilleTraiter.append([x,y,ultraSubmatch])
            x += 1
        # for ultraSubmatch in rematches:
        #     grilleTraiter[x][y] = ultraSubmatch
        #     print("Position X"+ x)
        #     print("Position Y"+ y)
        #     print(grilleTraiter[x][y])
        #     x+=1
        x =0
        y +=1
    # print(grilleTraiter[0][0])
    return grilleTraiter


def trouverTete(grille):
    coordX= 0
    coordY= 0
    for y in range(624):
        coordY = y
        if(grille[coordY][2] == "H"):
            return(grille[coordY][1],grille[coordY][0])
            
def trouverPomme(grille):
    coordX= 0
    coordY= 0
    for y in range(624):
        coordY = y
        if(grille[coordY][2] == "A"):
            return(grille[coordY][1],grille[coordY][0])

def differenceTetePomme(grille):
    coordTete = trouverTete(grille)
    coordPomme = trouverPomme(grille)
    print(coordTete)
    differenceX = math.fabs(coordTete[1]-coordPomme[1])
    differenceY = math.fabs(coordTete[0]-coordPomme[0])
    return differenceX,differenceY
