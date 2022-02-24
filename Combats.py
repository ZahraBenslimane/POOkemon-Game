# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
#%% Class Combat : abstraite        
class Combat(ABC): 
    
    def __init__(self):
        self.gameOver = False 
        
    @abstractmethod    
    def fuireCombat(self):   pass  #Dresseur qui déclare forfait contre un autre dresseur OU qui fuit un pokemon libre
       
    @abstractmethod
    def passerLeTour(self): pass

    @abstractmethod 
    def swapTour(self): pass

    @abstractmethod 
    def gagnerExperience(self,Vainqueur): pass
    @abstractmethod 
    def reset_VieEnergie_forAll(self): pass
        

#%% Class JCJ 
class JCJ(Combat):
    
    def __init__(self, dresseur1, dresseur2): 
        super().__init__()
        #self.gameOver = False
        self.dresseur1 = dresseur1
        self.dresseur2 = dresseur2
        
        self.dresseur1Turn = True
        self.dresseur2Turn = False
        
    def fuireCombat():   #Fuire le pokémon
        pass
    
    def passerLeTour(self):
         #Appel d'une methode de type (self.pokemonLibre).play()       
        pass
        
    
    def gagnerExperience(self, dresseurVainqueur):
        if dresseurVainqueur == self.dresseur1:
            niveauMoy_pokemonVaicus = ( (self.dresseur2.deck[0]).niveau + (self.dresseur2.deck[1]).niveau +(self.dresseur2.deck[2]).niveau )/3
            # Pour chaque pokémon du dek du dresseur vainqueur gagne de l'éxpérience
            for pokemon in (self.dresseur1).deck:
                pokemon.experience += 10 + niveauMoy_pokemonVaicus - pokemon.niveau
                if pokemon.experience >  pokemon.niveau * 100 + 100:
                   pokemon.niveau += 1 #On change de niveau du pokémon         
             
        elif dresseurVainqueur == self.dresseur2:   
            niveauMoy_pokemonVaicus = ( (self.dresseur1.deck[0]).niveau + (self.dresseur1.deck[1]).niveau +(self.dresseur1.deck[2]).niveau )/3
            # Pour chaque pokémon du dek du dresseur vainqueur gagne de l'éxpérience
            for pokemon in self.dresseur2.deck:
                pokemon.experience += 10 + niveauMoy_pokemonVaicus - pokemon.niveau
                if pokemon.experience >  pokemon.niveau * 100 + 100:
                   pokemon.niveau += 1 #if pokemon.experience   #On change de niveau du pokémon                        
        else:
            print("Ce dresseur n'est pas dans le combat")
            
    def reset_VieEnergie_forAll(self): 
    # Reinitialiser la vie et energie des 6 pokemon (3 de chaque deck d'un dresseur)
        
        # Dresseur2
        for pokemonD1 in self.dresseur1.pokemonListe:
            pokemonD1.reset_VieEnergie()
        for pokemonD1 in self.dresseur1.deck:
            pokemonD1.reset_VieEnergie()
        
        # Dresseur 2 
        for pokemonD2 in self.dresseur2.pokemonListe:
            pokemonD2.reset_VieEnergie()
        for pokemonD2 in self.dresseur2.deck:
            pokemonD2.reset_VieEnergie()
            
    def swapTour(self):
        self.dresseur1Turn = not(self.dresseur1Turn)
        self.dresseur2Turn = not(self.dresseur2Turn)
        
    def regenererEnergie_forALL(self):
        self.dresseur1.pokemonChoisi.regenererEnergie()
        self.dresseur2.pokemonChoisi.regenererEnergie()
        
        
    def combatJCJ(self):

        # RESET VIE ET ENERGIE FOR ALL
        self.reset_VieEnergie_forAll()
        
        joueur = self.dresseur1
        adversaire = self.dresseur2
        
        #print(moncombat.gameOver)
        print("\n\n ************* Combat JCJ entre {} et {} !  ***********".format(joueur.nom,adversaire.nom)) 
        print("\nC'est à {} de choisir son pokemon !\n".format(joueur.nom))
        joueur.choisirUnPokemon(adversaire.pokemonChoisi)
        print("\nC'est à {} de choisir son pokemon !\n".format(adversaire.nom))
        adversaire.choisirUnPokemon(joueur.pokemonChoisi)      
        
        i=1
        while(not(self.gameOver)):
            print("--------------------------------------")
            print("Tour  : {} \n".format(i))
            print("--------------------------------------")
            
            while (self.dresseur1Turn) :    
                try:
                    joueur.choisirUneAction( adversaire.pokemonChoisi , self)  
                except gameOver:
                    print("Game Over ! {} a gagne contre {}".format(joueur.nom,adversaire.nom)) 
                    self.gagnerExperience(joueur)
                    self.gameOver = True
                    break

                except quitGame :
                    print("Game Over ! {} a quitter le combat, {} a gagne !.".format(joueur.nom,adversaire.nom))
                    self.gagnerExperience(adversaire)
                    self.gameOver = True
                    break
            
                    
            print("\n--------------------------------------")        
            while(self.dresseur2Turn) :
                try:
                    adversaire.choisirUneAction(joueur.pokemonChoisi, self)
                    
                except gameOver:
                    print("Game Over ! {} a gagne contre {}".format(adversaire.nom,joueur.nom)) 
                    self.gagnerExperience(adversaire)
                    self.gameOver = True
                    break
                
                except quitGame :
                    print("Game Over ! {} a quitter le combat, {} a gagne !.".format(adversaire.nom,joueur.nom))
                    self.gagnerExperience(joueur)
                    self.gameOver = True
                    break
            # Regenerer l'energie for ALL 
            self.regenererEnergie_forALL()
            
            i +=1 
            

            
#%% Class JCE        
class JCE(Combat):   #Implemetation d'une IA
    
    def __init__(self,dresseur, pokemonLibre):
        super().__init__()
        self.dresseur = dresseur
        self.pokemonLibre = pokemonLibre #class pokemon
        
        self.dresseurTurn = True
        self.pokemonLibreTurn = False
        
    def fuireCombat():   #Fuire le pokémon
        pass
    
    def passerLeTour(self):
         #Appel d'une methode de type (self.pokemonLibre).play()       
        pass
    
    def swapTour(self):
        self.dresseurTurn = not(self.dresseurTurn)
        self.pokemonLibreTurn = not(self.pokemonLibreTurn)
    
    
    def gagnerExperience(self):         
        # Chaque pokémon du dek du dresseur vainqueur gagne de l'éxpérience
        for pokemon in self.dresseur.deck:
            pokemon.experience += (10 + self.pokemonLibre.niveau -  pokemon.niveau )/4        
            #if pokemon.experience > 100#On change de niveau du pokémon                  

            
    def capturerPokemon(self): # Une autre IA 
        seuil = 0.5  # ???  à discuter
        # Vérifier que le pokemon est de vie inferieur a 20%
        if (self.pokemonLibre).vie <= 20* (self.pokemonLibre).vieMax / 100 :
            # Calculer la probabilité de capture du pokemon
            probabiliteDeCapture = 4*(0.2 - (self.pokemonLibre).vie/(self.pokemonLibre).vieMax)
            # Comparer la probabilite a un certain seuil
            if probabiliteDeCapture >= seuil:
                # On ajoute ce pokemon à la liste du dresseur
                ((self.dresseur).pokemonListe).append(self.pokemonLibre) #l'ajout à la liste veut dire que le pokemo est capturé
                # Déclarer que le combat est fini 
                self.gameOver = True                     
        else:
            print("Vous ne pouvez pas capturer ce pokemon tant que ca vie n'est pas inferieur a 20%")

    # Fonction à appeler à l'initialisation de chaque combat
    def reset_VieEnergie_forAll(self):
        # Reinitialiser la vie et energie du pokemon libre avant le combat                est ce qu'on doit reseter ça ? à discuter
        self.pokemonLibre.reset_VieEnergie()
        
        # Meme chose pour chaque pokemon du deck du dresseur
        for pokemon in self.dresseur.pokemonListe:
            pokemon.reset_VieEnergie()
        for pokemon in self.dresseur.deck:
            pokemon.reset_VieEnergie()
            
    def regenererEnergie_forALL(self):
        
        self.dresseur.pokemonChoisi.regenererEnergie()
        self.pokemonLibre.regenererEnergie()
    
   
   
        
        
    def combatJCE(self): #la deuxieme implementaion de l'IA 

        # RESET VIE ET ENERGIE FOR ALL
        self.reset_VieEnergie_forAll()
        
        joueur = self.dresseur
        pokemonLibre = self.pokemonLibre
        
        #print(moncombat.gameOver)
        print("\n\n ************* Combat JCE entre {} et {} !  ***********".format(joueur.nom,pokemonLibre.nom)) 
        print("\nC'est à {} de choisir son pokemon !\n".format(joueur.nom))
        joueur.choisirUnPokemon(pokemonLibre)
    
        i=1
        while(not(self.gameOver)):
            print("--------------------------------------")
            print("Tour  : {} \n".format(i))
            print("--------------------------------------")
            
            while (self.dresseurTurn) :    
                try:
                    joueur.choisirUneAction(pokemonLibre, self)  
                    
                except gameOver:
                    print("Game Over ! {} a gagne contre {}".format(joueur.nom,pokemonLibre.nom)) 
                    self.gagnerExperience()
                    self.gameOver = True
                    break

                except quitGame :
                    print("Game Over ! {} a quitter le combat, {} a gagne !.".format(joueur.nom,pokemonLibre.nom))
                    self.gameOver = True
                    break
                
                except pokemonCapture :
                    print("Bravo ! Vous venez de capturer {}".format(pokemonLibre.nom))
                    self.gameOver = True
                    break
            
                    
            print("--------------------------------------")        
            while(self.pokemonLibreTurn) :
                try:
                    pokemonLibre.jouerUneCompetence(joueur)
                    self.swapTour()
                    
                except gameOver:
                    print("Game Over ! {} a gagne contre {}".format(pokemonLibre.nom,joueur.nom)) 
                    # gagner experience
                    self.gameOver = True
                    break
                
            # Regenerer l'energie for ALL        
            self.regenererEnergie_forALL()
            i +=1 
            

class gameOver(Exception): pass                 
class quitGame(Exception): pass
class pokemonCapture(Exception):pass