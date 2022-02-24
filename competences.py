# -*- coding: utf-8 -*-


import random
import getFiles

#%% Class Attaque
class Attaque():
    def __init__(self, nom,  attaqueDictionary):
        self.nom = nom 
        self.description = attaqueDictionary[nom][1]
        self.element     = attaqueDictionary[nom][2]
        self.puissance   = attaqueDictionary[nom][3] 
        self.precision   = attaqueDictionary[nom][4] 
        self.cout        = attaqueDictionary[nom][5]
        
        
    def __str__(self):
        res = self.nom + " (Attaque , {}, Cout : {}) : {} ".format(self.element, self.cout, self.description)
        return  res
    
    
    def __eq__(self,other):
        
        if not isinstance(other,Attaque):
            return False
        elif self is other:
            return True
        else :
            if self.nom != other.nom : return False
            if self.description != other.description : return False
            if self.element != other.element : return False
            if self.puissance != other.puissance : return False
            if self.precision != other.precision : return False
            if self.cout != other.cout : return False
            
            return True
        

    def afficherCompetence(self):
        res = "Attaque : " + self.nom +" ; "+ self.description +" \n"  + self.element
        res +=  " | puissance = " + str(self.puissance) + " | precision = " + str(self.precision)   + " | cout = " + str(self.cout) 
        return res
     
    #Déterminer si l'attaque est réussite : à utiliser sur les compétences de types attaque
    def isSuccess (self ):
        randomNum = random.uniform(1,100)
        if randomNum >  self.precision :
            #Attaque échoué
            return False
        else :
            #Attaque réussite
            return True
        
        
    #calculer les dégats infligés par un pokémon sur son adversaire SI L'ATTAQUE EST REUSSITE
    def calculer_degatsInfilges(self, pokemon, adversaire):
        puissance = self.puissance  # Puissance de la compétence utilisée
        eta = pokemon.niveau
        omega = adversaire.resistance 
        b = pokemon.calculer_CoefMultiplicateur(adversaire)
        cm = random.uniform(0.85, 1) * b  # !!!!!!
        return  round( cm * ( puissance * (4*eta+2)/omega + 2   ))
          
        
#%% Class Defense        
class Defense():
    def __init__(self, nom,  defenseDictionary):
        self.nom = nom 
        self.description = defenseDictionary[nom][1]
        self.element     = defenseDictionary[nom][2]        
        self.soin        = defenseDictionary[nom][3]  
        self.energie     = defenseDictionary[nom][4]         
        self.cout        = defenseDictionary[nom][5]    
    
    def __str__(self):
        res =  self.nom + " (Defense , {}, Cout : {}) ".format(self.element, self.cout) +": " + self.description
        return res
    
    
    def __eq__(self,other):
        
        if not isinstance(other,Defense):
            return False
        if self is other:
            return True
        
        if self.nom != other.nom : return False
        if self.description != other.description : return False
        if self.element != other.element : return False
        if self.soin != other.soin : return False
        if self.energie != other.energie : return False
        if self.cout != other.cout : return False
            
        return True

      
    def afficherCompetence(self):
        res = "Defense : " + self.nom +" ; "+ self.description +" \n"  + self.element 
        res +=   " | soin = " + str(self.soin) + " | energie = " + str(self.energie) + " | cout = " + str(self.cout)
        return res 
   
    