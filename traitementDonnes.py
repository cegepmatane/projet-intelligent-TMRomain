import re

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
            grilleTraiter.append([x,ultraSubmatch])
            x += 1
        # for ultraSubmatch in rematches:
        #     grilleTraiter[x][y] = ultraSubmatch
        #     print("Position X"+ x)
        #     print("Position Y"+ y)
        #     print(grilleTraiter[x][y])
        #     x+=1
        y +=1
    print(grilleTraiter[0][0])
    return grilleTraiter

