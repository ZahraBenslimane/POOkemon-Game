# -*- coding: utf-8 -*-

from AI import AI
from pokemons import Pokemon
import random
from competences import Attaque, Defense
from Combats import JCJ,JCE, gameOver, quitGame,pokemonCapture

class Dresseur: 
    
    def __init__(self, nom, pokemonDictionary, attaqueDictionary, defenseDictionary):  #liste_pokemon
        self.nom = nom
        self.pokemonListe = []
        self.deck = []
        self.pokemonChoisi = None
        
        nb_pokemon = random.randint(4,6)
        
        randomPokemonList = random.sample( list(pokemonDictionary.keys()) , nb_pokemon)    #List de 3 pokémons
        
        for pokemonName in randomPokemonList[0:3]:
            self.deck.append(Pokemon(pokemonName,pokemonDictionary, attaqueDictionary, defenseDictionary))
        for pokemonName in randomPokemonList[3:nb_pokemon]:
            self.pokemonListe.append(Pokemon(pokemonName,pokemonDictionary, attaqueDictionary, defenseDictionary))
 
    def __eq__(self,other):
        
        if not isinstance(other,Dresseur): return False
        if self is other: return True
            
        if self.nom != other.nom : return False
        if self.pokemonChoisi != other.pokemonChoisi : return False
        for i,pokemonInBench in  enumerate(self.pokemonListe):
            if  pokemonInBench != other.pokemonListe[i] : return False
            
        for i,pokemonInDeck in enumerate(self.deck):
            if pokemonInDeck != other.deck[i] : return False 
            
        return True
            
    
    # Affiche les pokemons du deck  : VALIDE  
    def afficherDeck(self):           #methode privée
        for i,pokemon in enumerate(self.deck):
            print("{}/ {} ".format(i, pokemon))
    
    # Affiche les pokemons sur le bench : VALIDE
    def afficherPokemonListe(self):   #methode privée
        for i,pokemon in enumerate(self.pokemonListe):
            print("{}/ {} ".format(i+3, pokemon)) 

           
    def afficherTousLesPokemons(self):
        print("\nVoici votre deck : ")
        self.afficherDeck()
        print("\nVoici le reste de vos pokemons sur le bench : ")
        self.afficherPokemonListe()
        

    # Changer de deck en dehors d'un combat : VALIDE    
    def changerDeck (self):        
        print("Changement de deck ...\nVoici votre deck : ")
        self.afficherDeck()
        print("\nVoici vos pokemons de bench :")
        self.afficherPokemonListe()

        while True:
            try:
                index_A_Remplacer = int(input("\nQuel pokemon voullez vous changer ? (0,2) "))
            except ValueError:
                print("Saisie invalide, veuillez reesayer.")
                #better try again... Return to the start of the loop
                continue
            if  not( 0 <= index_A_Remplacer < 3) : 
                print("Saisie invalide, veuillez reesayer.")
                continue
            else:
                break
            
        if len(self.pokemonListe) > 1:
            while True:
                try:
                    index_Remplacant = int(input("Quel pokemon voullez vous ajouter ? (3,{}) ".format(len(self.pokemonListe)+2 )))
                    index_Remplacant = index_Remplacant - 3
                except ValueError:
                    print("Saisie invalide, veuillez reesayer.")
                    #better try again... Return to the start of the loop
                    continue
                if  not (0 <= index_Remplacant <= len(self.pokemonListe)): 
                    print("Saisie invalide, veuillez reesayer.")
                    continue
                else:
                    break
        elif  len(self.pokemonListe) == 1: 
            index_Remplacant = 0
        else :
            print("Vous ne pouvez pas changer de deck ! Essayer de capturer des pokemons d'abord.")
                
        (self.pokemonListe).append(self.deck[index_A_Remplacer] )
        self.deck[index_A_Remplacer] = self.pokemonListe[index_Remplacant]
        (self.pokemonListe).remove(self.pokemonListe[index_Remplacant])
        print("\nVotre deck mis à jour :")
        self.afficherDeck()
        
        # Demander si l'utilisateur veut procéder par un autre changement de pokemon
        print("\nVoulez vous procéder par un autre changement de Pokemon ? ")  
        print("0/ Oui.")
        print("1/ Non, revenir au menu principal.")
        
        while True:
            try:
                select = int(input("Que voulez vous faire? (0-1) : "))
            except ValueError:
                print("Saisie invalide, veuillez reesayer.")
                #better try again... Return to the start of the loop
                continue
            if select != 0 and select != 1: 
                print("Saisie invalide, veuillez reesayer.")
                continue
            else:
                break
        
        if(select == 0):
            self.changerDeck()
            
    def combatreDresseur(self,game):
        print("\n----- Dresseur Vs Dresseur -----")
        print("0/ Combatre un dresseur deja existant")
        print("1/ Creer puis combatre un nouveau dresseur ")
        print("2/ Combatre ULTRON ")
        print("3/ Revenir au menu principal")
        while True:
            try:
                select = int(input("Que voulez vous faire? (0-2) : "))
            except ValueError:
                print("Saisie invalide, veuillez reesayer.")
                #better try again... Return to the start of the loop
                continue
            if select < 0 or select > 3: 
                print("Saisie invalide, veuillez reesayer.")
                continue
            else:
                break
            
        if select == 0:
            self.combatreDresseurExistant(game)
        elif select == 1:
            self.combatreNouveauDresseur(game)
        
        elif select == 2:
            self.combatreUltron(game)
        
        
    def combatrePokemonLibre(self,game):
        # On lui cree un pokemon à combatre
        randomNom = random.choice(list(game.pokemonDictionary.keys())) 
        pokemonLibre = AI(randomNom, game.pokemonDictionary, game.attaqueDictionary, game.defenseDictionary)
        
        #print("\n----- {} Vs {} -----".format(game.utilisateur.nom , pokemonLibre.nom))
        
        print("\nVoici les competences de {}.\n".format(pokemonLibre.nom))
        pokemonLibre.ShowAllcompetences()
        print()
        
        ################################# BOUCLE DE JEU ####################################  
        monCombat = JCE(game.utilisateur, pokemonLibre)
        monCombat.combatJCE()
        #####################################################################################

            
            
    def combatreDresseurExistant(self,game):
        #nbEssaies = 0
        adversaire = ""
        nomAdversaire = input("Veuillez saisir le nom de l'adversaire que vous souhaitez combatre : ")
        revenirMenuPrincipal = False

        for dresseur in game.listDresseurs:
            if dresseur.nom == nomAdversaire:
                adversaire = dresseur
        # Si le dresseur n'existe pas
        if adversaire == "":
            print("\nLe dresseur que vous cherchez n'existe pas.Voulez vous chercher un autre dresseur ?")
            print("0/ Oui")
            #print("1/ Non, je souhaite revenir en arriere")
            print("1/ Non, je souhaite revenir au menu principal")

            while True:
                try:
                    select = int(input("\nQue voulez vous faire? (0-1) : ")) 
                except ValueError:
                    print("Saisie invalide, veuillez reesayer.")
                    continue
                if not( 0  <= select < 2) : 
                    print("Saisie invalide, veuillez reesayer.")
                    continue
                else:
                    break

            if select == 0:
                self.combatreDresseurExistant(game)
            if select != 1:
                revenirMenuPrincipal = True


        elif revenirMenuPrincipal != True and adversaire !="": 
            # Si le dresseur existe, Creer un combat JCJ
            ################################# BOUCLE DE JEU ####################################
            monCombat = JCJ(game.utilisateur, adversaire)
            monCombat.combatJCJ()
            #####################################################################################
        
    def combatreNouveauDresseur(self,game):
        nom_adversaire = input("Veuillez saisir le nom du nouveau dresseur : ")
        for dresseur in game.listDresseurs:
            if dresseur.nom == nom_adversaire :
                print("Ce nom existe deja, veuillez choisir un autre.")
                self.combatreNouveauDresseur(self,game)
                
        adversaire = Dresseur(nom_adversaire, game.pokemonDictionary, game.attaqueDictionary, game.defenseDictionary)
        # Append nouveau dresseur à la liste des dresseurs
        game.listDresseurs.append(adversaire)
        # Affichier ces pokemon
        print("\nVoici le deck de {}".format(adversaire.nom))
        adversaire.afficherDeck()
        
        ################################# BOUCLE DE JEU #################################### 
        monCombat = JCJ(game.utilisateur, adversaire)
        monCombat.combatJCJ()
        #####################################################################################
        
        
    def combatreUltron(self,game):
        adversaireAI = IA_dresseur(game.pokemonDictionary, game.attaqueDictionary, game.defenseDictionary)
        print("combatreUltron:Adversaire IA", type(adversaireAI))
        # Affichier ces pokemon
        print("\nVoici le deck de Ultron")
        adversaireAI.afficherDeck()
        ################################# BOUCLE DE JEU #################################### 
        monCombat = JCJ(game.utilisateur, adversaireAI)
        monCombat.combatJCJ()
        #####################################################################################
        
        
    # Vérifier à chaque fois si au moins un pokemon n'est pas KO               
    def isDeckKO(self):
        res = True
        for pokemon in self.deck:
            res = res and pokemon.isKO()
        if res == True:
            return True
        else:
            return False
        
        
    def choisirUnPokemon(self, pokemon_adversaire): 
        #print("\nC'est à {} de choisir son pokemon !\n".format(self.nom))
        self.afficherDeck()
        choix = int(input("\nQuel pokemon voulez vous utiliser, {} ? : ".format(self.nom) ))
        print()
        self.pokemonChoisi = self.deck[choix]
        
    
    def choisirUneAction(self, pokemonAdversaire, combat) :
        
        if isinstance(combat, JCJ):
            
            print("{}, a vous de jouer !\n".format(self.nom))
            print(self.pokemonChoisi)
            print()
            self.pokemonChoisi.ShowAllcompetences()
            print("{} / Changer de pokemon".format(len(self.pokemonChoisi.competences) ))
            print("{} / Passer votre tour".format(len(self.pokemonChoisi.competences) + 1))
            print("{} / Fuir le combat".format(len(self.pokemonChoisi.competences) + 2))
            
            #choix = int(input("Que voulez vous faire ? (0,{}) ? : ".format(len(self.pokemonChoisi.competences) + 2)))
            
            while True:
                try:
                    choix = int(input("Que voulez vous faire ? (0,{}) ? : ".format(len(self.pokemonChoisi.competences) + 2)))
                except ValueError:
                    print("Saisie invalide, veuillez reesayer.")
                    continue
                if not( 0  <= choix < len(self.pokemonChoisi.competences) + 3) : 
                    print("Saisie invalide, veuillez reesayer.")
                    continue
                else:
                    break
            
        
            if (0 <= choix < len(self.pokemonChoisi.competences)) :
                
                competenceChoisi_joueur = self.pokemonChoisi.competences[choix]
                self.jouerUneCompetence( competenceChoisi_joueur, combat)
                combat.swapTour()
                
            if (choix == len(self.pokemonChoisi.competences)) : 
                self.choisirUnPokemon(pokemonAdversaire)
                combat.swapTour()
            
            elif choix == len(self.pokemonChoisi.competences) + 1: 
                combat.swapTour()
                
            elif choix ==  len(self.pokemonChoisi.competences) +2 :
                raise quitGame
                

        elif isinstance(combat,JCE) :
            
            print("{}, a vous de jouer !\n".format(self.nom))
            print(self.pokemonChoisi)
            print()
            
            self.pokemonChoisi.ShowAllcompetences()
            print("{} / Changer de pokemon".format(len(self.pokemonChoisi.competences) ))
            print("{} / Capturer le pokemon adversaire".format(len(self.pokemonChoisi.competences) + 1))
            print("{} / Passer votre tour".format(len(self.pokemonChoisi.competences) + 2))
            print("{} / Fuir le combat".format(len(self.pokemonChoisi.competences) + 3))
            
            #choix = int(input("Que voulez vous faire ? (0,{}) ? : ".format(len(self.pokemonChoisi.competences) + 3)))

            while True:
                try:
                    choix = int(input("Que voulez vous faire ? (0,{}) ? : ".format(len(self.pokemonChoisi.competences) + 3)))
                except ValueError:
                    print("Saisie invalide, veuillez reesayer.")
                    continue
                if not( 0  <= choix <= len(self.pokemonChoisi.competences) + 3) : 
                    print("Saisie invalide, veuillez reesayer.")
                    continue
                else:
                    break
            
            
            
            if (0 <= choix < len(self.pokemonChoisi.competences)) :
                competenceChoisi_joueur = self.pokemonChoisi.competences[choix]
                self.jouerUneCompetence( competenceChoisi_joueur, combat)
                combat.swapTour()
          

            if (choix == len(self.pokemonChoisi.competences)) : 
                self.choisirUnPokemon(self.pokemonChoisi)
                combat.swapTour()
                
            elif choix == len(self.pokemonChoisi.competences) + 1:
                self.capturerPokemon(pokemonAdversaire)
            
            elif choix == len(self.pokemonChoisi.competences) +2 : 
                combat.swapTour()
                
            elif choix == len(self.pokemonChoisi.competences) +3:
                raise quitGame
                                
                
    def capturerPokemon(self,pokemonLibre):
        seuil = 0.3  # ???  à discuter
        # Vérifier que le pokemon est de vie inferieur a 20%
        if pokemonLibre.vie <= 20* pokemonLibre.vieMax / 100 :
            # Calculer la probabilité de capture du pokemon
            probabiliteDeCapture = 4*(0.2 - pokemonLibre.vie/(pokemonLibre.vieMax))
            print("probabilité de capture =   Vs seuil de probabilité de capture",probabiliteDeCapture,seuil)
            # Comparer la probabilite a un certain seuil
            if probabiliteDeCapture >= seuil :
                # On ajoute ce pokemon à la liste du dresseur
                self.pokemonListe.append(pokemonLibre)
                
                # Déclarer que le combat est fini 
                raise pokemonCapture                    
        else:
            print("Vous ne pouvez pas capturer ce pokemon tant que ca vie n'est pas inferieur a 20%")

            
    def jouerUneCompetence(self, competenceChoisi , combat): 
        
        if isinstance(combat, JCE):
            pokemonAdversaire = combat.pokemonLibre
            
            #Verifier que le pokemon n'est pas KO:
            if self.pokemonChoisi.isKO() :
                    print("\nVotre pokemon est KO ! Veillez changer de pokemon, si vous souhaiter continuer le jeu.\n")
                    self.choisirUnPokemon()
                    
            else : 
                
                # retrancher le cout 
                self.pokemonChoisi.retrancherCout(competenceChoisi)

                if  isinstance(competenceChoisi , Attaque) : 
                    # verifier la réussite de l'attaque 
                    if competenceChoisi.isSuccess() == True  : 
                        # Calculer les degats infliges sur le pokemon adversaire
                        degatsInfilges = competenceChoisi.calculer_degatsInfilges(self.pokemonChoisi, pokemonAdversaire)
                        # retrancher la vie  à l'adversaire 
                        pokemonAdversaire.retrancherVie(degatsInfilges)
                        print("Attaque reussite ({}) : {} degats".format(competenceChoisi.nom, degatsInfilges))
                        
                    else:
                        print("Votre Attaque n'a pas affecté votre adversaire {}.".format(pokemonAdversaire.nom))
                    
 
                elif isinstance(competenceChoisi , Defense) : 
                    self.pokemonChoisi.regenererVieEnergie(competenceChoisi)

                else:
                    print("Competence choisi n'est ni Attaque ni Defense")
                
                if pokemonAdversaire.isKO() : raise gameOver
                     
            
        elif isinstance(combat, JCJ):
            
            if self == combat.dresseur1:
                pokemonAdversaire = combat.dresseur2.pokemonChoisi
            else:
                pokemonAdversaire = combat.dresseur1.pokemonChoisi
            
            #Verifier que le pokemon n'est pas KO:
            if self.pokemonChoisi.isKO() :
                    print("\nVotre pokemon est KO ! Veillez changer de pokemon, si vous souhaiter continuer le jeu.\n")
                    self.choisirUnPokemon(pokemonAdversaire)
            else : 
                
                # retrancher le cout 
                self.pokemonChoisi.retrancherCout(competenceChoisi)
                
                if  isinstance(competenceChoisi , Attaque) : 
                    # verifier la réussite de l'attaque 
                    if competenceChoisi.isSuccess() == True  : 
                        # retrancher la vie  à l'adversaire 
                        degatsInfilges = competenceChoisi.calculer_degatsInfilges(self.pokemonChoisi, pokemonAdversaire)
                        pokemonAdversaire.retrancherVie(degatsInfilges)
                        print("Attaque reussite ({}) : {} degats".format(competenceChoisi.nom, degatsInfilges))
                        
                    else:
                        print("\nVotre Attaque n'a pas affecté votre adversaire {}.".format(pokemonAdversaire.nom))
                        
                elif isinstance(competenceChoisi , Defense) : 
                    self.pokemonChoisi.regenererVieEnergie(competenceChoisi)
                    
                else:
                    print("Competence choisi n'est ni Attaque ni Defense")
            
            if self == combat.dresseur1:
                if combat.dresseur2.isDeckKO() : raise gameOver
            else:
                if combat.dresseur1.isDeckKO() : raise gameOver


class IA_dresseur(Dresseur) : 
    def __init__(self,pokemonDictionary, attaqueDictionary, defenseDictionary)  :
        super().__init__("Ultron", pokemonDictionary,attaqueDictionary, defenseDictionary)
    
    def choisirUnPokemon(self, pokemon_adversaire): 
        self.afficherDeck()
        coeficient_b = []
        #indice_pokemon = []
        indice_pokemon_alfa = 7
        for i, pokemon in enumerate(self.deck):
            coeficient_b.append(self.calculer_CoefMultiplicateur(pokemon,pokemon_adversaire))
        indice_pokemon_alfa =  coeficient_b.index(max(coeficient_b))
        choix = indice_pokemon_alfa
        if not(self.deck[choix].isKO()) :
            self.pokemonChoisi = self.deck[choix]
        else : 
            for i , p in enumerate (self.deck ): 
                if not(p.isKO()) : 
                    self.pokemonChoisi = self.deck[i]
        print ("Ultron a décider de vous tabassser avec {}".format(self.pokemonChoisi.nom))

        

                    
                    
        
    
    def changerPokemon(self, pokemon_adversaire): 
        #self.afficherDeck()
        coeficient_b = []
        #indice_pokemon = []
        indice_pokemon_alfa = 7
        for i, pokemon in enumerate (self.deck):
            coeficient_b.append(self.calculer_CoefMultiplicateur(pokemon,pokemon_adversaire))
            
        indice_pokemon_alfa =  coeficient_b.index(max(coeficient_b))
            
        #print ("Ultron a décider de vous tabassser avec {}".format(self.deck[indice_pokemon_alfa].nom))
        choix = indice_pokemon_alfa
        return choix

    
    def calculer_CoefMultiplicateur(self,pokemon,adversaire):
        if pokemon.element == adversaire.element:
            b = 1
            
        if pokemon.element == "Air" and  adversaire.element =="Eau"  or  \
              pokemon.element == "Eau" and adversaire.element == "Feu"  or  \
                pokemon.element =="Feu" and adversaire.element =="Terre"  or  \
                    pokemon.element =="Terre"  and adversaire.element =="Air":
           b = 1.5
        elif pokemon.element == "Air"   and  adversaire.element =="Feu"  or  \
               pokemon.element == "Eau"   and adversaire.element == "Terre"  or  \
                pokemon.element =="Feu"    and adversaire.element =="Air"  or  \
                  pokemon.element =="Terre"  and adversaire.element =="Eau":
            b = 0.5
        if pokemon.element == "Air" and  adversaire.element =="Terre"  or  \
              pokemon.element == "Eau" and adversaire.element == "Air"  or  \
                pokemon.element =="Feu" and adversaire.element =="Eau"  or  \
                    pokemon.element =="Terre"  and adversaire.element =="Feu":
           b = 1                        
        return b 
    
    
    
    
    def choisirUneAction(self, pokemonAdversaire, combat) :
        
        if isinstance(combat, JCJ):
            
            print("{} se prépare pour jouer! ..\n".format(self.nom))
            choix = self.ai_Ultron_decision(pokemonAdversaire)       
            
            if (0 <= choix < len(self.pokemonChoisi.competences)) :
                
                competenceChoisi_joueur = self.pokemonChoisi.competences[choix]
                self.jouerUneCompetence( competenceChoisi_joueur, combat)
                combat.swapTour()
                
            if (choix == len(self.pokemonChoisi.competences)) : 
                self.choisirUnPokemon(pokemonAdversaire)
                combat.swapTour()
                
        else:
            print("La fonctionnalité AI-dresseur contre AI-Environement n'est pas implémentée")
                
                 
    def jouerUneCompetence(self, competenceChoisi , combat):  
        
        if isinstance(combat, JCJ):
            
            if self == combat.dresseur1:
                pokemonAdversaire = combat.dresseur2.pokemonChoisi
            else:
                pokemonAdversaire = combat.dresseur1.pokemonChoisi
            
            #Verifier que le pokemon n'est pas KO:
            if self.pokemonChoisi.isKO() :
                    print("\nVotre pokemon est KO ! Veillez changer de pokemon, si vous souhaiter continuer le jeu.\n")
                    self.choisirUnPokemon()
            else : 
                
                # retrancher le cout 
                self.pokemonChoisi.retrancherCout(competenceChoisi)
                
                if  isinstance(competenceChoisi , Attaque) : 
                    # verifier la réussite de l'attaque 
                    if competenceChoisi.isSuccess() == True  : 
                        # retrancher la vie  à l'adversaire 
                        degatsInfilges = competenceChoisi.calculer_degatsInfilges(self.pokemonChoisi, pokemonAdversaire)
                        pokemonAdversaire.retrancherVie(degatsInfilges)
                        print("Attaque reussite ({}) : {} degats".format(competenceChoisi.nom, degatsInfilges))
                        
                    else:
                        print("\nVotre Attaque n'a pas affecté votre adversaire {}.".format(pokemonAdversaire.nom))
                        
                elif isinstance(competenceChoisi , Defense) : 
                    self.pokemonChoisi.regenererVieEnergie(competenceChoisi)
                    
                else:
                    print("Competence choisi n'est ni Attaque ni Defense")
            
            if self == combat.dresseur1:
                if combat.dresseur2.isDeckKO() : raise gameOver
            else:
                if combat.dresseur1.isDeckKO() : raise gameOver
                
                
                     

    def ai_Ultron_decision(self, pokemondversaire) : 
        #joueur = dresseurAdversaire
        has_soin = False 
        has_energie = False
        energy_min = 1000000 
        #puissance_max = 0
        tab_puissance = []
        tab_indices =[]
        #change_pokemon = False 
        
        
        if self.changerPokemon(pokemondversaire) != self.deck.index(self.pokemonChoisi) or self.pokemonChoisi.vie <=0: 
            return len(self.pokemonChoisi.competences)
            
        elif self.changerPokemon(pokemondversaire) == self.deck.index(self.pokemonChoisi) : 
            for i,competence_choisi in enumerate  (self.pokemonChoisi.competences) : # On parcours d'abord les competences pour savoir si une competence de soin existe 
                if isinstance( competence_choisi, Defense) : 
                    ##print((competence_choisi.afficherCompetence()))
                    
                    if (competence_choisi.soin[1] > 0) : 
                        has_soin = True 
                        if self.pokemonChoisi.vie <= (self.pokemonChoisi.vie * 22)/100 and has_soin == True :   
                            return i
                    elif competence_choisi.energie[1] > 0 : 
                        has_energie = True 
                        for j, c in enumerate (self.pokemonChoisi.competences) : 
                            if isinstance(c, Defense) and ( energy_min > c.energie[1] ) :
                                energy_min = c.energie[1]
                        if self.pokemonChoisi.energie <= energy_min and has_energie == True : 
                            return i
                if isinstance( competence_choisi, Attaque) :
                    tab_puissance.append(competence_choisi.puissance)
                    tab_indices.append(i)
            for i in range (len(tab_indices)) : 
                indice_puissance_max =  tab_puissance.index(max(tab_puissance))
                if (self.pokemonChoisi.competences[tab_indices[indice_puissance_max]].cout <= self.pokemonChoisi.energie) : 
                    return tab_indices[indice_puissance_max]  
                else : 
                    tab_puissance.pop(indice_puissance_max)
                    tab_indices.pop(indice_puissance_max)
             