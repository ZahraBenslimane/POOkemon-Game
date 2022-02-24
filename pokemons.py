# -*- coding: utf-8 -*-


from competences import Attaque, Defense
import random
import getFiles 

from Combats import gameOver

nameIndex = 0
elementIndex = 3
niveauMinIndex = 4
niveauMaxIndex = 5
vieMinIndex = 6
vieMaxIndex = 7
energieMinIndex = 8
energieMaxIndex = 9
regenerationMinIndex = 10
regenerationMaxIndex = 11
resistanceMinIndex = 12
resistanceMaxIndex = 13
competencesIndex = 14

   
class Pokemon:
    def __init__(self, nom, pokemonDictionary,attaqueDictionary, defenseDictionary):
        self.nom = nom
        self.element = pokemonDictionary[nom][elementIndex]


        # Le niveau du pokemon est randomiser entre ça valeur de niveau MIN et MAX lu du fichier CSV
        self.niveau = random.randint( pokemonDictionary[nom][niveauMinIndex],  pokemonDictionary[nom][niveauMaxIndex]  )
        self.experience = self.niveau * 100 # pour le niveau 1 : le pokemon atteint le niveau suivant à experience = 200
        
        # L'algorithm nous permettant de generer une vie, energie, regeneration et une resistance par rapport au niveau donné
        if pokemonDictionary[nom][niveauMinIndex] == 1 or pokemonDictionary[nom][niveauMinIndex] == 6  :
            diviseur = 4
        else :
            diviseur = 5
        
        self.vieMax = pokemonDictionary[nom][vieMinIndex]  +  ( ( pokemonDictionary[nom][vieMaxIndex] - pokemonDictionary[nom][vieMinIndex] )/diviseur ) * (self.niveau - pokemonDictionary[nom][niveauMinIndex])
        self.vie = self.vieMax
        
        self.energieMax = pokemonDictionary[nom][energieMinIndex] +  ( ( pokemonDictionary[nom][energieMaxIndex] - pokemonDictionary[nom][energieMinIndex] )/diviseur ) * (self.niveau - pokemonDictionary[nom][niveauMinIndex])
        self.energie = self.energieMax
        
        self.regeneration = pokemonDictionary[nom][regenerationMinIndex] +  ( ( pokemonDictionary[nom][regenerationMaxIndex] - pokemonDictionary[nom][regenerationMinIndex] )/diviseur ) * (self.niveau - pokemonDictionary[nom][niveauMinIndex])
        self.resistance	= pokemonDictionary[nom][resistanceMinIndex]  +  ( ( pokemonDictionary[nom][resistanceMaxIndex] - pokemonDictionary[nom][resistanceMinIndex] )/diviseur ) * (self.niveau - pokemonDictionary[nom][niveauMinIndex])
        
        # On initialise la liste d'objet de type < Attaque > ou < Defense >
        self.competences = []
        # List des noms des competences 
        liste_competences = pokemonDictionary[nom][competencesIndex]
        # Extraire les noms (keys) du dictionnaire contenant les attaque ou defense
        List_noms_attaques = attaqueDictionary.keys()
        #print(List_noms_attaques)
        List_noms_defences = defenseDictionary.keys()
        #print()
        #print(List_noms_defences)
        
        # Pour chaque competence, on verifie si c'est une attaque ou defense en regardant si elle appartient à attaqueDictionary ou defenseDictionary        
        for myCompetenceName in liste_competences:
            # Si le nom indique que c'est une attaque, on instancie un objet de type < Attaque >
            # Lors de extraction des noms, des fois y a un espace avant ou apres le nom : ex; ' Feu Sacre' : ce qui induit des erreurs , on enleve les whitespace avec .strip()
            myCompetenceName = myCompetenceName.strip() 
            if myCompetenceName in List_noms_attaques:  
               (self.competences).append( Attaque(myCompetenceName,attaqueDictionary ) ) 
           # Si le nom indique que c'est une defense, on instancie un objet de type < Defense >
           
            elif myCompetenceName in List_noms_defences:
                (self.competences).append( Defense(myCompetenceName, defenseDictionary ) )
            else: 
                print("Competence non reconnue ! ")
                
                


    def __str__(self):
        res = "{} : (Lvl {}, {}/{}, {}) : Vie {}/{}, Energie {}/{} (+{}), Resistance  {} \n"\
                 .format(self.nom, self.niveau, self.experience, self.experience + 100, self.element, self.vie, self.vieMax, self.energie, self.energieMax, self.regeneration, self.resistance) 
        for competence in self.competences:
            # Si c'est la derniere competense dans la lists des competenses on mets un . 
            if competence.nom == self.competences[-1].nom: 
                res += "{}. ".format(competence.nom)
            else:
                res += "{}, ".format(competence.nom)
                
        return res
    

    def __eq__(self,other):
    
        if not isinstance(other,Pokemon): return False
        if self is other: return True
            
        if  self.nom != other.nom : return False
        if  self.element != other.element : return False
        if  self.vieMax != other.vieMax : return False
        if  self.energieMax != other.energieMax : return False
        if  self.niveau != other.niveau : return False
        if  self.experience != other.experience : return False
        if  self.vie != other.vie : return False
        if  self.energie != other.energie : return False
        if  self.regeneration != other.regeneration : return False
        if  self.resistance != other.resistance : return False 
        
        for i,competence in enumerate(self.competences):
            if competence != other.competences[i]:
                return False
        return True
        
    
    def ShowAllcompetences(self):
        for i, competence in enumerate(self.competences):
            print(i, "/",competence)
            

            
    def jouerUneCompetence(self,dresseurAdversaire):   
        
        print("{}, a vous de jouer !\n".format(self.nom))
        print(self)
        self.ShowAllcompetences()
        
        while True:
            try:
                choix = int(input("Que voulez vous faire? (0-{}) : ".format(len(self.competences)-1)))
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
        
        
    # def attaquer(self):
    #     ####
    #     print("lancer une attaque")
    #     pass
        
    # def defendre(self):
    #     ###
    #     print("defendre")
    #     pass
    
    
        
    # Fonction à appeler lorsque le joueur selectionne un pokemon pour jouer un tour:
    # Pour Vérifier qu'un pokémon peu toujours jouer sinon on le change:
    def isKO(self):
        if self.vie <= 0:
            return True
        else:
            #print("Oups ! votre pokemon est KO, vous ne pourriez plus l'utiliser dans cette partie.")
            #print("Veillez choisir un autre pokemon de votre deck.")
            return False

   
    # Fonction à appeler au début de chaque combat pour un reset de la vie et energie du pokémon
    def reset_VieEnergie(self):
        self.energie = self.energieMax
        self.vie = self.vieMax
        
    #Fonction à appeler à la fin de chaque tour(gain d'énergie à chaque tour de combat)    
    def regenererEnergie(self):
        if self.energie < self.energieMax:  
            if self.energie + self.regeneration >= self.energieMax:
                self.energie = self.energieMax
            else:
                self.energie += self.regeneration
                
    #Fonction à appeler apres chaque attaque ou défense
    def retrancherCout(self,competence):
        if self.energie > 0:
            if self.energie - competence.cout < 0:
                self.energie = 0
            else:
                self.energie -= competence.cout
                
    # Définition du tableau            
    def calculer_CoefMultiplicateur(self,adversaire):
        if self.element == adversaire.element:
            b = 1
            
        if self.element == "Air" and  adversaire.element =="Eau"  or  \
              self.element == "Eau" and adversaire.element == "Feu"  or  \
                self.element =="Feu" and adversaire.element =="Terre"  or  \
                    self.element =="Terre"  and adversaire.element =="Air":
           b = 1.5
        elif self.element == "Air"   and  adversaire.element =="Feu"  or  \
               self.element == "Eau"   and adversaire.element == "Terre"  or  \
                self.element =="Feu"    and adversaire.element =="Air"  or  \
                  self.element =="Terre"  and adversaire.element =="Eau":
            b = 0.5
        if self.element == "Air" and  adversaire.element =="Terre"  or  \
              self.element == "Eau" and adversaire.element == "Air"  or  \
                self.element =="Feu" and adversaire.element =="Eau"  or  \
                    self.element =="Terre"  and adversaire.element =="Feu":
           b = 1                        
        return b 
    
    def retrancherVie(self,degatsInfilges):
        #elf.vie -= degatsInfilges
        if self.vie > 0:
            if self.vie - degatsInfilges < 0: 
                self.vie = 0
            else:
                self.vie -= degatsInfilges
        
    def regenererVieEnergie(self,competenceChoisi ):
        # On choisit une valeure entre valmin et valmax  pour déterminer le taux de soin et d'energie a attribuer au pokemon
        vieRegeneree = random.randint(competenceChoisi.soin[0], competenceChoisi.soin[0])/100 * self.vieMax
        energieRegeneree = random.randint(competenceChoisi.energie[0], competenceChoisi.energie[0])/100 * self.energieMax
        if vieRegeneree != 0 :
            #self.vie += vieRegeneree 
            if self.vie < self.vieMax:  
                if self.vie + vieRegeneree >= self.vieMax:
                    self.vie = self.vieMax
                else:
                    self.energie += energieRegeneree
            print("{} a regenerer {}/{} de ça vie Max avec sa defense : {} : Vie actuelle = {}".format(self.nom,vieRegeneree,self.vieMax,competenceChoisi.nom, self.vie))
        if energieRegeneree != 0:
            #self.energie +=  energieRegeneree 
            if self.energie < self.energieMax:  
                if self.energie + energieRegeneree >= self.energieMax:
                    self.energie = self.energieMax
                else:
                    self.energie += energieRegeneree
            
            
            print("{} a regenerer {}/{} de son energie Max avec sa defense : {} : Energie actuelle = {}".format(self.nom,energieRegeneree,self.vieMax,competenceChoisi.nom, self.energie))


  

#Nidoqueen.ShowAllcompetences()

#print(Goupix.competences)

#print("b = ",Nidoqueen.calculer_CoefMultiplicateur(Goupix))

