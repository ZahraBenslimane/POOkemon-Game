#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from competences import Attaque, Defense

from pokemons import Pokemon
#from dresseurs import Dresseur
from Combats import JCJ, JCE,gameOver


class AI(Pokemon) : 
    def __init__(self, nom, pokemonDictionary,attaqueDictionary, defenseDictionary) : 
        super().__init__(nom, pokemonDictionary,attaqueDictionary, defenseDictionary)
    
            
    def jouerUneCompetence(self,dresseurAdversaire):   
        
        print("{}, a vous de jouer !\n".format(self.nom))
        print(self)
        self.ShowAllcompetences()
        
        while True:
            try:
                
                choix = self.aiDecision(dresseurAdversaire)
                
            except ValueError:
                print("Saisie invalide, veuillez reesayer.")
                #better try again... Return to the start of the loop
                continue
            if choix < 0 or choix > len(self.competences)-1: 
                print("Saisie invalide, veuillez reesayer.")
                continue
            else:
                break
         
        competenceChoisi = self.competences[choix]
            
        #Verifier que le pokemon n'est pas KO:
        if self.isKO() :
                print("\nVotre pokemon est KO ! Veillez changer de pokemon, si vous souhaiter continuer le jeu.\n")
                raise gameOver
                
        # retrancher le cout 
        self.retrancherCout(competenceChoisi)
        
        if  isinstance(competenceChoisi , Attaque) : 
                # verifier la réussite de l'attaque 
            if competenceChoisi.isSuccess() == True  : 
                # retrancher la vie  à l'adversaire 
                degatsInfilges = competenceChoisi.calculer_degatsInfilges(self, dresseurAdversaire.pokemonChoisi)
                dresseurAdversaire.pokemonChoisi.retrancherVie(degatsInfilges)
                print("Attaque reussite ({}) :{} degats ".format(competenceChoisi.nom,degatsInfilges ))
            else:
                print("Votre Attaque n'a pas affecté votre adversaire {}.".format(dresseurAdversaire.pokemonChoisi.nom))
            
        elif isinstance(competenceChoisi , Defense) : 
            self.regenererVieEnergie(competenceChoisi)
            #combat.swapTour()
        else:
            print("Competence choisi n'est ni Attaque ni Defense")
            
        if dresseurAdversaire.isDeckKO() : raise gameOver
    
    def aiDecision (self , dresseurAdversaire) : # elle choisit la competence du pokemon
        #joueur = dresseurAdversaire
        has_soin = False 
        has_energie = False
        energy_min = 1000000 
        #puissance_max = 0
        tab_puissance = []
        tab_indices =[]
        for i,competence_choisi in enumerate  (self.competences) : # On parcours d'abord les competences pour savoir si une competence de soin existe 
            if isinstance( competence_choisi, Defense) : 
                
                #print((competence_choisi.afficherCompetence()))
                
                if (competence_choisi.soin[1] > 0) : 
                    has_soin = True 
                    if self.vie <= (self.vie * 22)/100 and has_soin == True :   
                        return i
                elif competence_choisi.energie[1] > 0 : 
                    has_energie = True 
                    for j, c in enumerate (self.competences) : 
                        if isinstance(c, Defense) and ( energy_min > c.energie[1] ) :
                            energy_min = c.energie[1]
                    if self.energie <= energy_min and has_energie == True : 
                        return i
            if isinstance( competence_choisi, Attaque) :
                tab_puissance.append(competence_choisi.puissance)
                tab_indices.append(i)
        for i in range (len(tab_indices)) : 
            indice_puissance_max =  tab_puissance.index(max(tab_puissance))
            if (self.competences[tab_indices[indice_puissance_max]].cout <= self.energie) : 
                return tab_indices[indice_puissance_max]  
            else : 
                tab_puissance.pop(indice_puissance_max)
                tab_indices.pop(indice_puissance_max)
                
           
            
#tab_indices[indice_puissance_max]                        
            

            
                    
        
            
                
                    
                
            
            
        
        