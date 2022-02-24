# -*- coding: utf-8 -*-



import sys
#import pokemons
import getFiles
#from Combats import JCJ
from dresseurs import Dresseur


class Game:
    def __init__(self):
        self.pokemonDictionary = getFiles.creer_mesPokemons()
        self.attaqueDictionary = getFiles.creer_mesAttaques()
        self.defenseDictionary = getFiles.creer_mesDefenses()
        self.listDresseurs = []
        self.utilisateur = None

    
    def afficherBienvenue(self):
        print("#-------------------------------------------#")
        print("#         Bienvenue dans POOkemon!          #")
        print("#   Le jeu de Pokemon Oriente Objet  :D     #")
        print("#-------------------------------------------#")
        
    def getNomUtilisateur(self):
        self.utilisateur = Dresseur(input("Quel est votre nom? "),self.pokemonDictionary, self.attaqueDictionary, self.defenseDictionary)
        self.listDresseurs.append(self.utilisateur)
        print ("Voila votre dresseur : {}: {} Pokemon.".format(self.utilisateur.nom, len(self.utilisateur.deck) + len(self.utilisateur.pokemonListe) ))
    
             
    def afficherMenuPrincipal(self):
        print("\n----  Menu Principal  ----")
        print("0/ Voir vos pokemon")
        print("1/ Changer le deck")
        print("2/ Combattre / Capturer un pokemon")
        print("3/ Combattre un dresseur") 
        print("4/ Creer un nouveau dresseur") 
        print("5/ Quitter le jeu ")
        
    def initialiserGame(self):
        self.afficherBienvenue()
        self.getNomUtilisateur()
        self.utilisateur.afficherDeck()
        
        
    def main(self):
        
        self.afficherMenuPrincipal()
        # Verifier si la saisie est valide               
        while True:
            try:
                choix = int (input("Que voulez vous faire? (0-5) : "))
            except ValueError:
                print("Saisie invalide, veuillez reesayer.")
                #better try again... Return to the start of the loop
                continue
            if choix < 0 or choix > 5: 
                print("Saisie invalide, veuillez reesayer.")
                continue
            else:
                break
        
        if choix == 0 : 
            self.utilisateur.afficherTousLesPokemons()
        elif choix == 1:
            self.utilisateur.changerDeck()      
        elif choix == 2:     
            self.utilisateur.combatrePokemonLibre(self)
        elif choix == 3:
            self.utilisateur.combatreDresseur(self)
        elif choix==4 : 
            self.creerNouveauDresseur()
        
        elif choix== 5:
            sys.exit()
            
    # Lorsque le joueur principal souhaite creer un nouveu dresseur 
    def creerNouveauDresseur(self):
        print("\n-- Creation d'un nouveau dresseur --")
        nom_nouveau_dresseur = input("Veuillez saisir le nom du nouveau dresseur : ")
        
        for dresseur in self.listDresseurs:
            if dresseur.nom == nom_nouveau_dresseur :
                print("Ce nom existe deja, veuillez choisir un autre.")
                self.creerNouveauDresseur()
                
        nouveau_dresseur = Dresseur(nom_nouveau_dresseur, self.pokemonDictionary, self.attaqueDictionary, self.defenseDictionary)
        # Append nouveau dresseur à la liste des dresseurs
        self.listDresseurs.append(nouveau_dresseur)
        
        print("\nVoici le deck de {} : ".format(nouveau_dresseur.nom))
        nouveau_dresseur.afficherDeck()
        print("\nLe rest des pokemons : ")
        nouveau_dresseur.afficherPokemonListe()
        print()

       

#%%mh
myGame = Game()

myGame.initialiserGame()

while(True):
    myGame.main()    
            