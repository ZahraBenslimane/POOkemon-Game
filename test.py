# -*- coding: utf-8 -*-


            
"""        
def dresseurVSdresseur(self):
    print("\n----- Dresseur Vs Dresseur -----")
    print("0/ Combatre un dresseur deja existant")
    print("1/ Creer puis combatre un nouveau dresseur ")
    print("2/ Revenir au menu principal")
    while True:
        try:
            select = int(input("Que voulez vous faire? (0-2)"))
        except ValueError:
            print("Saisie invalide, veuillez reesayer.")
            #better try again... Return to the start of the loop
            continue
        if select < 0 or select > 2: 
            print("Saisie invalide, veuillez reesayer.")
            continue
        else:
            break
        
    if select == 0:
        self.utilisateur.combatreDresseurExistant(self)
    elif select == 1:
        self.utilisateur.combatreNouveauDresseur(self)
    elif select == 2:
        self.main()
"""
    
 
"""        
def combatreDresseurExistant(self):
    #nbEssaies = 0
    adversaire = ""
    nomAdversaire = input("Veuillez saisir le nom de l'adversaire que vous souhaitez combatre : ")
    
    for dresseur in self.listDresseurs:
        if dresseur.nom == nomAdversaire:
            adversaire = dresseur
    # Si le dresseur n'existe pas
    if adversaire == "":
        print("\nLe dresseur que vous cherchez n'existe pas.\n")
        print("Voulez vous chercher un autre dresseur ?")
        print("0/ Oui")
        print("1/ Non, je souhaite revenir en arriere")
        print("2/ Non, je souhaite revenir au menu principal")
        
        select = int(input("\nQue voulez vous faire? (0-2) : ")) 
        # Ckeck if valid ????????????????????????????????
        
        if select == 0:
            self.combatreDresseurExistant()
        elif select == 1:
            self.dresseurVSdresseur()
        elif select == 2:
            self.main()
                
    # Si le dresseur existe
    # Creer un combat JCJ
    ################################# BOUCLE DE JEU ####################################       
    self.combatJCJ(self.utilisateur, adversaire)
    #####################################################################################
"""
"""
def combatreNouveauDresseur(self):
    nom_adversaire = input("Veuillez saisir le nom du nouveau dresseur : ")
    for dresseur in self.listDresseurs:
        if dresseur.nom == nom_adversaire :
            print("Ce nom existe deja, veuillez choisir un autre.")
            self.combatreNouveauDresseur(self.utilisateur)
            
    adversaire = Dresseur(nom_adversaire, self.pokemonDictionary, self.attaqueDictionary, self.defenseDictionary)
    # Append nouveau dresseur à la liste des dresseurs
    self.listDresseurs.append(adversaire)
    # Affichier ces pokemon
    print("\nVoici le deck de {}".format(adversaire.nom))
    adversaire.afficherDeck()
    ################################# BOUCLE DE JEU #################################### 
    self.combatJCJ(self.utilisateur, adversaire)
    #####################################################################################
 """ 
 
 

"""    def combatrePokemonLibre(self,game):
        print("\n----- Dresseur Vs Pokemon -----")
        print("0/ Combatre un dresseur deja existant")
        print("1/ Creer puis combatre un nouveau dresseur ")
        print("2/ Revenir au menu principal")
        while True:
            try:
                select = int(input("Que voulez vous faire? (0-2)"))
            except ValueError:
                print("Saisie invalide, veuillez reesayer.")
                #better try again... Return to the start of the loop
                continue
            if select < 0 or select > 2: 
                print("Saisie invalide, veuillez reesayer.")
                continue
            else:
                break
            
        if select == 0:
            self.combatreDresseurExistant(game.listDresseurs)
        elif select == 1:
            self.combatreNouveauDresseur(game)"""