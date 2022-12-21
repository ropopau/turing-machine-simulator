from reader import *
from modifier import *
from os import listdir

def linker(form_b):
    form = marqueur(form_b, "MAIN")
    listappel = []
    for etat, sousdic in form["dico"].items():
        for lu, info in sousdic.items():
            if type(info["change"]) != tuple:
                listappel.append({"etat": etat, "lu": lu, "appel": info["change"], "dest": info["dest"], "mvt": info["mvt"]})
    if not listappel:
        print("La machine n'appelle aucune machine\n")
        return 0
    else:
        a = listdir("turs")
        possible = True
        for elem in listappel:
            if elem["appel"]+".tur" not in a:
                print("Il n'existe pas de fichier correspondant à la machine appelée: ",elem["appel"]," dans le répertoire\n")
                possible = False     
                return 1
        if possible:
            a = link(form, listappel)
            return a
        else:
            print("Veuillez ajouter les fichiers *.tur nécessaire pour utiliser le linker.\n")

def link(d, l):
    # Pour tout les appelées
    z = 0
    for elem in l:
        # Lire le code de l'appelée
        readappel = reader("turs\\"+ elem["appel"] + ".tur")
        new_dic = marqueur(readappel, str(z))
        new_qi = new_dic["qi"]
        new_qf = new_dic["qf"]
        allchar = tuple(["%" for _ in range(d["nbr"])])
        allmvt = tuple(["-" for _ in range(d["nbr"])])
        # Transition de l'état ou est appelée
        etatInit = elem["etat"]
        d["dico"][etatInit][elem["lu"]] = {"dest": new_qi, "change": allchar, "mvt": elem["mvt"]}
        # Transition du dernier état de l'appelée à "dest"
        d["dico"][new_qf] = {}
        d["dico"][new_qf][allchar] = {"dest": elem["dest"], "change": allchar, "mvt": allmvt}     
        z += 1
        # Ajout dans le dictionnaire principale
        d["Qe"] = d["Qe"] + new_dic["Qe"]
        d["dico"] = {**d["dico"], **new_dic["dico"]}

    return d