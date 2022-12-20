from reader import *
from modifier import *

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