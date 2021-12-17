from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyboard 
import re
import numpy as np
from traitementDonnes import differenceTetePomme, grilleDeDonneeExterne
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import numpy as np
from tensorflow.keras.utils import to_categorical

from random import randint

import matplotlib.pyplot as plt

driver = webdriver.Firefox()
driver.get("http://51.161.32.22/Snake/snake.html")


score = driver.find_element_by_id("scoreValue")
gameover = driver.find_element_by_id("gameoverValue")
jeu = driver.find_element_by_id("game")
grille = driver.find_element_by_id("grilleVisuel")
main_body = driver.find_element_by_xpath("//html")
boucle = True
oldgrille = grille.get_attribute('innerHTML')
grilleTraiter = []



#Neural network 
# Frequence d'entrainement
train_frequency = 10

# Le neural Network
model = Sequential()
model.add(Dense(1, input_dim=1, activation='sigmoid'))
model.add(Dense(2, activation='softmax'))
model.compile(Adam(lr=0.1), loss='categorical_crossentropy', metrics=['accuracy'])

#Distance entre pomme et tete
x_train = np.array([])
#Decision prise par NN
y_train = np.array([])

fig, _ = plt.subplots(ncols=1, nrows=3, figsize=(6, 6))
fig.tight_layout()

all_scores = []
average_scores = []
average_score_rate = 10
all_x, all_y = np.array([]), np.array([])

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



def bougerViaAction(action):
    if(action==0):
        mouvement("haut")
    if(action==1):
        mouvement("bas")
    if(action==2):
        mouvement("gauche")
    if(action==3):
        mouvement("droite")

oldScore = score.text

def visualiser():
    plt.subplot(3, 1, 1)
    x = np.linspace(1, len(all_scores), len(all_scores))
    plt.plot(x, all_scores, 'o-', color = 'r')
    plt.xlabel("Jeu Snake avec Python")
    plt.ylabel("Score")
    plt.title("Score par partie")

    plt.subplot(3, 1, 2)
    plt.scatter(x_train[y_train==0], y_train[y_train==0], color='r', label='Gauche')
    plt.scatter(x_train[y_train==1], y_train[y_train==0], color='r', label='Droite')
    plt.scatter(x_train[y_train==2], y_train[y_train==0], color='r', label='Haut')
    plt.scatter(x_train[y_train==3], y_train[y_train==0], color='r', label='Bas')
    plt.xlabel('Distance avec la pomme')
    plt.title('Données d entrainement')

    plt.subplot(3, 1, 3)
    x2 = np.linspace(1, len(average_scores), len(average_scores))
    plt.plot(x2, average_scores, 'o-', color = 'b')
    plt.xlabel("Jeu")
    plt.ylabel("Score")
    plt.title("Score moyen des 10 derniere partie")

    plt.pause(0.001)

    
#Boucle du jeu
while(boucle):
    if(oldgrille != grille.get_attribute('innerHTML')):
        oldgrille= grille.get_attribute('innerHTML')
        grilleTraiter = grilleDeDonneeExterne(oldgrille)
    action = 1

    if(oldScore !=score.text ):
        oldScore = score.text
        x_train = np.append(x_train, [differenceTetePomme(grilleTraiter)])
        y_train = np.append(y_train, [action])

        # Prediction du neural NN
    # prediction = model.predict_classes(np.array([[differenceTetePomme(grilleTraiter)]]))
    predict_x=model.predict(differenceTetePomme(grilleTraiter)) 
    classes_x=np.argmax(predict_x,axis=1)

    r = randint(0, 100)
    random_rate = 50*(1-int(gameover.text)/50)
    visualiser()
    # print(classes_x)
    # bougerViaAction(action)
    if int(gameover.text) is not 0 and int(gameover.text) % train_frequency is 0:
                # Before training, let's make the y_train array categorical
                all_x = np.append(all_x, x_train)
                all_y = np.append(all_y, y_train)

                all_scores.append(int( score.text))

                y_train_cat = to_categorical(y_train, num_classes = 2)

                # Let's train the network
                model.fit(x_train, y_train_cat, epochs = 50, verbose=1, shuffle=1)

                # Reset x_train and y_train
                x_train = np.array([])
                y_train = np.array([])
                if int(gameover.text) is not 0 and int(gameover.text) % average_score_rate is 0:
                    average_score = sum(all_scores)/len(all_scores)
                    average_scores.append(average_score)
    #Appuier sur q pour quitter la simulation
    if keyboard.is_pressed('q'): 
            driver.close()
            boucle = False
            break
    if keyboard.is_pressed('p'):
        #  grilleDeDonneeExterne(oldgrille)
        print(len(grilleTraiter))
    if keyboard.is_pressed('t'):
        # print(score.text)
         print(differenceTetePomme(grilleTraiter))
    
    #print(elem.text)


# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()