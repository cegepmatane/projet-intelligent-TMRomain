from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyboard 
import re
from traitementDonnes import grilleDeDonneeExterne, trouverTete
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


#Boucle du jeu
while(boucle):
    if(oldgrille != grille.get_attribute('innerHTML')):
        oldgrille= grille.get_attribute('innerHTML')
        grilleTraiter = grilleDeDonneeExterne(oldgrille)
    #Appuier sur q pour quitter la simulation
    if keyboard.is_pressed('q'): 
            driver.close()
            boucle = False
            break
    if keyboard.is_pressed('p'):
        #  grilleDeDonneeExterne(oldgrille)
        print(len(grilleTraiter))
    if keyboard.is_pressed('t'):
         print(trouverTete(grilleTraiter))
    
    #print(elem.text)



# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()