from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyboard 
import re
driver = webdriver.Firefox()
driver.get("http://51.161.32.22/Snake/snake.html")


elem = driver.find_element_by_id("score")
jeu = driver.find_element_by_id("game")
grille = driver.find_element_by_id("grilleVisuel")
main_body = driver.find_element_by_xpath("//html")
boucle = True
oldgrille = grille.get_attribute('innerHTML')
grilleTraiter = []

#Fonction qui envoie le mouvement
def mouvement(leMouvement):
    if(leMouvement =="haut"):
        driver.execute_script("versLeHaut();")
    if(leMouvement =="bas"):
        driver.execute_script("versLeBas();")
    if(leMouvement =="gauche"):
        driver.execute_script("versLeGauche();")
    if(leMouvement =="droite"):
        driver.execute_script("versLeDroite();")


#Recuperer les donnée de position du serpent de la pomme et de la grille en generale
def grilleDeDonnee():
    # print(oldgrille)
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
    return


#Boucle du jeu
while(boucle):
    if(oldgrille != grille.get_attribute('innerHTML')):
        oldgrille= grille.get_attribute('innerHTML')
        # grilleDeDonnee()
    #Appuier sur q pour quitter la simulation
    if keyboard.is_pressed('q'): 
            driver.close()
            boucle = False
            break
    if keyboard.is_pressed('p'):
         grilleDeDonnee()
    
    #print(elem.text)



# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()