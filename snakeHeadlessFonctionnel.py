from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyboard 
driver = webdriver.Firefox()
driver.get("http://51.161.32.22/Snake/snake.html")


elem = driver.find_element_by_id("score")
jeu = driver.find_element_by_id("game")
main_body = driver.find_element_by_xpath("//html")
boucle = True

#Fonction qui envoie le mouvement
def mouvement(leMouvement):
    print(leMouvement)
    if(leMouvement =="haut"):
        main_body.send_keys("w")


#Boucle du jeu
while(boucle):

    #Appuier sur q pour quitter la simulation
    if keyboard.is_pressed('q'): 
            driver.close()
            boucle = False
            break
    if keyboard.is_pressed('p'):
         mouvement("haut")
    
    #print(elem.text)



# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()