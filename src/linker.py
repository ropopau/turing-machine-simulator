from reader import *
from turing import *
from os import listdir


# Choisie une machine qui appelle pour en créer une machine sans appel et créée un nouveau fichier .tur avec.
def linker(auto):
    listappel = []
    for etat, sousdic in auto["dico"].items():
        for lu, info in sousdic.items():
            if type(info["change"]) != tuple:
                listappel.append({"etat": etat, "lu": lu, "appelee": info["change"], "dest": info["dest"]})
    
    if not listappel:
        print("La machine n'appelle aucune machine")
        exit()
    else:
        a = listdir("turs")
        possible = True
        for elem in listappel:
            if elem["appelee"]+".tur" not in a:
                print("Il n'existe pas de fichier correspondant à la machine appelée: ",elem["appelee"]," dans le répertoire")
                possible = False
            
        if possible:
            link()
        else:
            print("Veuillez ajouter les fichiers *.tur nécessaire pour utiliser le linker.")
    
def link():
    print("link")

if __name__ == "__main__":
    read = CodeTuring("turs\\TEST_LINKER.tur")
    auto = read.get_auto()
    linker(auto)