from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyboard 
import re
import numpy as np
from traitementDonnes import differenceTetePomme, grilleDeDonneeExterne,trouverTete,trouverPomme
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from random import randrange

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
firstTime= True
firstTimeAppend= True
oldgrille = ""
grilleTraiter = []

positionSerpent = []
actionPriseSerpent = []
customScore = []
positionPomme = []
distanceTetePomme = []
nombreMouvementArray = []
xDataset = []
yDataset = []

#Neural network 
# Frequence d'entrainement
train_frequency = 2

# Le neural Network
# model = Sequential()
# model.add(Dense(1, input_dim=1, activation='sigmoid'))
# model.add(Dense(2, activation='softmax'))
# model.compile(Adam(lr=0.1), loss='categorical_crossentropy', metrics=['accuracy'])
model = Sequential()
model.add(Dense(12, input_dim=3, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

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
oldPartie = score.text
nombreMouvement = 0

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
positionActuel = []
oldPositionSnake = []
def choixAction():
    return randrange(4)
#Boucle du jeu
while(boucle):
    if(oldgrille != grille.get_attribute('innerHTML')):
        oldgrille= grille.get_attribute('innerHTML')
    if(firstTime == True):
        if(oldgrille != ""):
            grilleTraiter = grilleDeDonneeExterne(oldgrille)
            oldPositionSnake = trouverTete(grilleTraiter)
            dernierePositionPomme = trouverPomme(grilleTraiter)
            positionActuel = oldPositionSnake
            firstTime = False
    action = 1
    
    if(oldScore !=score.text ):
        oldScore = score.text
        positionPomme.append(dernierePositionPomme[0])
        positionPomme.append(dernierePositionPomme[1])
        dernierePositionPomme = trouverPomme(grilleTraiter)
        # x_train = np.append(x_train, [differenceTetePomme(grilleTraiter)])
        # y_train = np.append(y_train, [action])
    if(oldPartie != int(gameover.text) ):
        oldPartie = int(gameover.text)
        if(oldPartie >= train_frequency):
            customScore.append(int(score.text))
            positionPomme.append(dernierePositionPomme)
            nombreMouvementArray.append(nombreMouvement)
            xDataset = [positionSerpent] + [actionPriseSerpent] + [positionPomme]
            # xDataset = positionSerpent
            yDataset = customScore + nombreMouvementArray
            print(xDataset)
            print(yDataset)
            model.fit(xDataset, yDataset, epochs=150, batch_size=10)
            # make class predictions with the model
            predictions = (model.predict(xDataset) > 0.5).astype(int)
            # summarize the first 5 cases
            for i in range(5):
                print('%s => %d (expected %d)' % (xDataset[i].tolist(), predictions[i], yDataset[i]))


            positionSerpent = []
            actionPriseSerpent = []
            customScore =  []
            positionPomme=[]
            distanceTetePomme =[]
            nombreMouvement= 0
            train_frequency += 2
    else :
        if(oldgrille != ""):
            grilleTraiter = grilleDeDonneeExterne(oldgrille)
            positionActuel = trouverTete(grilleTraiter)
        if(oldPositionSnake != positionActuel):
            nombreMouvement +=1
            action = choixAction()
            bougerViaAction(action)
            # distance = differenceTetePomme(grilleTraiter)

            if(oldPositionSnake == None):
                positionSerpent.append(positionSerpent[-1])
            else:
                positionSerpent.append(oldPositionSnake[0])
                positionSerpent.append(oldPositionSnake[1])
                # distanceTetePomme.append(distance[0])
                # distanceTetePomme.append(distance[1])
            actionPriseSerpent.append(action)
            oldPositionSnake = positionActuel
    # visualiser()
    # print(classes_x)
    # bougerViaAction(action)
    # if int(gameover.text) is not 0 and int(gameover.text) % train_frequency is 0:
    #             # Before training, let's make the y_train array categorical
    #             all_x = np.append(all_x, x_train)
    #             all_y = np.append(all_y, y_train)

    #             all_scores.append(int( score.text))

    #             y_train_cat = to_categorical(y_train, num_classes = 2)

    #             # Let's train the network
    #             model.fit(x_train, y_train_cat, epochs = 50, verbose=1, shuffle=1)

    #             # Reset x_train and y_train
    #             x_train = np.array([])
    #             y_train = np.array([])
    #             if int(gameover.text) is not 0 and int(gameover.text) % average_score_rate is 0:
    #                 average_score = sum(all_scores)/len(all_scores)
    #                 average_scores.append(average_score)
    #Appuier sur q pour quitter la simulation
    if keyboard.is_pressed('q'): 
            driver.close()
            boucle = False
            break
    if keyboard.is_pressed('p'):
        #  grilleDeDonneeExterne(oldgrille)
        print(len(grilleTraiter))
        # evaluate the keras model
        _, accuracy = model.evaluate(xDataset, yDataset)
        print('Accuracy: %.2f' % (accuracy*100))
    if keyboard.is_pressed('t'):
        # print(score.text)
         print(differenceTetePomme(grilleTraiter))
    
    #print(elem.text)


# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()