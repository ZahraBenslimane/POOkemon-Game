#-*- coding: utf-8 -*-



# ***************************   Fonction qui lit les compétences d'attaques    *********************************************
      
# get_myAttaque_Atributes(): renvois les composants d'une seule ligne(compétence) du fichier attaque.txt
def get_myAttaque_Atributes(myAttaque):
    split_myAttaque = myAttaque.split("\t")
    nom         = split_myAttaque[0]
    description = split_myAttaque[1]
    element     = split_myAttaque[2]
    puissance   = int(split_myAttaque[3])
    precision   = int(split_myAttaque[4])
    cout        = int(split_myAttaque[5])
    return nom, description, element, puissance, precision,cout

# get_myAttaque_Atributes(): renvois les composants d'une seule ligne(compétence) du fichier defense.txt
def get_myDefense_Atributes(myDefense):
    #myDefense = myDefense.replace('\t\t' , '\t')
    split_myDefense = myDefense.split("\t")
    
    nom         = split_myDefense[0]
    description = split_myDefense[1]
    element     = split_myDefense[2]
    
    soin        = split_myDefense[3]
    if soin != "":
        soin        = [ int( soin.split("-")[0] ), int( soin.split("-")[1] ) ] # vecteur = [soinMin, soinMax]
    else : 
        soin = [0 , 0]
         
    energie     =  split_myDefense[4]
    if energie != "":
        energie     = [  int( energie.split("-")[0]) , int( energie.split("-")[1] ) ]
    else:
        energie     = [0 , 0]
    
    cout        = int(split_myDefense[5])
    return nom, description, element, soin, energie ,cout

def get_myPokemon_Atributes(myPokemon):
    split_myPokemon = myPokemon.split("\t")
    nom     = split_myPokemon[0]
    avant   = split_myPokemon[1]
    apres   = split_myPokemon[2]
    element = split_myPokemon[3]
    niveau    = int ( split_myPokemon[4].split("-")[0] )
    niveauMax = int ( split_myPokemon[4].split("-")[1] )
    vieMin    = int ( split_myPokemon[5].split("-")[0] )
    vieMax    = int ( split_myPokemon[5].split("-")[1] )
    energieMin      = int ( split_myPokemon[6].split("-")[0] )
    energieMax      = int ( split_myPokemon[6].split("-")[1] )
    regenerationMin = int ( split_myPokemon[7].split("-")[0] )
    regenerationMax = int ( split_myPokemon[7].split("-")[1] )
    resistanceMin   = int ( split_myPokemon[8].split("-")[0] )
    resistanceMax   = int ( split_myPokemon[8].split("-")[1] )
    competances = (split_myPokemon[9].rstrip("]\n")).lstrip("[")
    split_competances = competances.split(",")

    return nom, avant, apres, element, niveau, niveauMax, vieMin, vieMax, energieMin, energieMax, regenerationMin, regenerationMax, \
        resistanceMin, resistanceMax, split_competances
    
    
# La fonction instanciate_my_attaques() lit le fichier contenant les attaques et leurs caractéristiques.
# La fonction  renvois une liste d'objets de type COMPETENCE, 
# chaque objet represente dans le cas de cette fonction une compétence d'attaque  
def creer_mesAttaques():
    myAttaque_file= open("data/attaque.txt", "r", encoding='utf-8', errors='ignore')
    mes_attaques = myAttaque_file.readlines()
    for i in range(1,len(mes_attaques)):
        nom, description, element, puissance, precision, cout = get_myAttaque_Atributes(mes_attaques[i])
          
        if i == 1:
            attaquesDictionary = { 
                nom : (nom, description, element, puissance, precision, cout) 
                }
        else :
            attaquesDictionary[nom] = (nom, description, element, puissance, precision, cout) 
    myAttaque_file.close()
    return attaquesDictionary


def creer_mesDefenses():
    myDefense_file= open("data/defense.txt", "r", encoding='utf-8', errors='ignore')
    mes_defenses = myDefense_file.readlines()
    for i in range(1,len(mes_defenses)):
        nom, description, element, soin, energie ,cout = get_myDefense_Atributes(mes_defenses[i])

        if i == 1:
            defensesDictionary = { 
                nom : (nom, description, element, soin, energie ,cout) 
                }
        else :
            defensesDictionary[nom] = (nom, description, element, soin, energie ,cout) 
              
    myDefense_file.close()
    return defensesDictionary

#################################################################################################################################

def creer_mesPokemons():
    myPokemons_file = open("data/pokemon.txt","r", encoding='utf-8', errors='ignore')
    myPokemons = myPokemons_file.readlines()

    for i in range(1,len(myPokemons)):
        nom, avant, apres, element, niveau, niveauMax, vieMin, vieMax, energieMin, energieMax, regenerationMin, regenerationMax, \
                                  resistanceMin, resistanceMax, split_competances = get_myPokemon_Atributes(myPokemons[i])
        # def _init_(self, nom, element, vieMax, energieMax, regeneration, resistance, experience,competences):
        if i == 1:
            pokemonDictionary = { 
                nom : (nom, avant, apres, element, niveau, niveauMax, vieMin, vieMax, energieMin, energieMax, regenerationMin, regenerationMax, \
                                  resistanceMin, resistanceMax, split_competances)
                }
        else :
            pokemonDictionary[nom] = (nom, avant, apres, element, niveau, niveauMax, vieMin, vieMax, energieMin, energieMax, regenerationMin, regenerationMax, \
                                  resistanceMin, resistanceMax, split_competances)
    myPokemons_file.close()            
    return pokemonDictionary

    
    
