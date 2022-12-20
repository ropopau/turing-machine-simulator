import time
from copy import *
import sys
import os
class Bandes(object):
     # Initie une bande avec nbr nombre de rubans
    def __init__(self, nbr, mot):
        self.__listRubans = [{"mot": ["#" for _ in range (len(mot))], "pos":0} for _ in range (nbr)]
        self.__listRubans[0]["mot"] = list(mot)

    def verification(self):
        for elem in self.__listRubans:
            if elem["pos"] == 0:
                self.ajoute_debut()
            elif elem["pos"] == len(elem["mot"]):
                self.ajoute_fin()
            
    def ajoute_debut(self):
        for elem in self.__listRubans:
            if elem["mot"][0] == "+":
                elem["mot"][0] = "#"
            elem["mot"].insert(0, "+")
            elem["pos"] += 1
    
    def ajoute_fin(self):
        for elem in self.__listRubans:
            if elem["mot"][-1] == "+":
                elem["mot"][-1] = "#"
            elem["mot"].append("+")

    # Getters et setters
    def get_list(self):
        return self.__listRubans

    def get_pos(self, quelRuban):
        return self.__listRubans[quelRuban]["pos"]
    
    def get_mot(self, quelRuban):
        return self.__listRubans[quelRuban]["mot"]

    def set_lettre(self, quelRuban, lettre):
        rub = self.__listRubans[quelRuban]
        rub["mot"][rub["pos"]] = lettre

    def set_pos(self, quelRuban, mvt):
        if mvt == "<":
            self.verification()
            self.__listRubans[quelRuban]["pos"] -= 1
        elif mvt == ">":
            self.verification()
            self.__listRubans[quelRuban]["pos"] += 1

class Machine(object):
    def __init__(self, formel, mot):
        self.__formel = formel
        self.__bandes = Bandes(formel["nbr"], mot)

        self.__etatActu = self.__formel["qi"]
        self.__pile = []

    def pas(self):
        ## Récupérations des lettres lu à l'état actuel
        for ruban in self.__bandes.get_list():
            a = ruban["mot"][ruban["pos"]]
            if a == "+":
                a = "#"
            self.__pile.append(a)

        lu_actu = list(self.get_dico()[self.__etatActu].keys())
        a = tuple(["%" for _ in range(self.get_nbrRub())])

        for lu in lu_actu:

            if list(lu).count("*")  == 1 :
                
                for indice in range(len(lu)):
                    if lu[indice] == "*":
                        lettre_etoile = self.__pile[indice]
                if lettre_etoile == "#":
                    break
                info = deepcopy(self.get_dico()[self.__etatActu][lu])
                ch = list(info["change"])
                for i in range(len(ch)):
                    if ch[i] == "*":
                        ch[i] = lettre_etoile
                info["change"] = ch
                self.get_dico()[self.__etatActu][tuple(self.__pile)] = info
                lu_actu.append(tuple(self.__pile))

        print(self.__pile, lu_actu)

        # Il ne peut pas avoir plus de deux étoile par transitions: Une étoile = Un caractère appartenant a l'alphabet.
        if tuple(self.__pile) in lu_actu or a in lu_actu:
            if a in lu_actu:
                pile_temp = a
                nvllettres = tuple(self.__pile)
                nvlmvts = self.get_dico()[self.__etatActu][a]["mvt"]
            # Si il est présent alors cela veut dire qu'il existe une transition pour ces lettres
            # On détermine alors les nvl lettres et mouvements
            else:
                pile_temp = tuple(self.__pile)
                nvllettres = self.get_dico()[self.__etatActu][tuple(self.__pile)]["change"]
                nvlmvts = self.get_dico()[self.__etatActu][tuple(self.__pile)]["mvt"]
            # Pour toute les bandes, 
            for i in range(len(self.__pile)):
                listrub = self.get_bandes()
                if tuple(nvllettres) != tuple(["%" for _ in range(self.get_nbrRub())]):
                    listrub.set_lettre(i, nvllettres[i])
                listrub.set_pos(i, nvlmvts[i])
            # Changement de l'état actuel
            self.__etatActu = self.get_dico()[self.__etatActu][pile_temp]["dest"]
        else:
            self.__etatActu = "Non accepté"
        # On vide la pile pour l'itération suivante
        self.__pile.clear()

    
    # Getters et setters
    def get_etatActu(self):
        return self.__etatActu

    def get_bandes(self):
        return self.__bandes

    def get_alphab(self):
        return self.__formel["Si"]

    def get_alphabT(self):
        return self.__formel["Ga"] 
    
    def get_etats(self):
        return self.__formel["Qe"]
    
    def get_etatI(self):
        return self.__formel["qi"]

    def get_etatF(self):
        return self.__formel["qF"]
    
    def get_dico(self):
        return self.__formel["dico"]
    
    def get_nbrRub(self):
        return self.__formel["nbr"]

# Effectue un pas sans afficher les rubans
def un_pas(formel, mot):
    Tur = Machine(formel, mot)
    _etat = formel["qi"]
    Tur.pas()
    _etat = Tur.get_etatActu()

# Exécute la machine jusqu'à la fin
def exec(formel, mot, vitesse, tailleterm, affiche = True):
    global taillet
    taillet = tailleterm
    Tur = Machine(formel, mot)
    etat = formel["qi"]
    os.system("cls")
    affichage(Tur)
    while etat != formel["qf"]:
        Tur.pas()
        etat = Tur.get_etatActu()
        if affiche:   
            print(etat)
            affichage(Tur)
            time.sleep(vitesse)
            os.system("cls")
        if etat == "Non accepté":
            break
    print("Etat: ", etat)
    affichage(Tur)

# Affiche les rubans à chaques étapes. Elle s'adapte à la taille du terminal sur lequel le programme est éxécuté.
def affichage(tur):
    global taillet
    bandes = tur.get_bandes().get_list()
    for elem in bandes:
        pointeur = ["---" if _ != (taillet // 4) // 2 else " ^ " for _  in range(taillet // 4)]
        ruban = [" - " for _  in range(taillet // 4) ]
        indice = 1
        for lettre in elem["mot"]:
            ind = (taillet // 8) - elem["pos"] + indice - 1
            if ind < 0:
                ind = 0
            elif ind > taillet // 4 - 1:
                ind = taillet // 4 - 1
            if lettre == "#" or lettre == "+":
                lettre = "-"
            ruban[ind] = " " + lettre + " "
            indice += 1
        sys.stdout.write("/".join(map(str, ruban)) + "\n")
        sys.stdout.write("-".join(map(str, pointeur)) + "\n")
    print("\n")


if __name__ == "__main__":
    import reader
    # Machine de turing en écriture formel
    """
    Si = ['a', 'b']
    Ga = ['a', 'b', '#']
    Qe = ["I", "F"]
    qi = "I"
    qf = "F"
    Dedico = {"I": {("a",): {"dest": "I", "change": ("b",), "mvt": (">",)}, 
                    ("b",): {"dest": "I", "change": ("a",), "mvt": (">",)},
                    ("#",): {"dest": "F", "change": ("#",), "mvt": ("-",)}}}
    nbr = 1
    """
    Si = [1, 0]
    Ga = [1, 0, "#"]
    Qe = ["cop", "ret", "tes", "F"]
    qi = "cop"
    qf = "F"
    Dedico = {"cop": {("0", "#",): {"dest": "cop", "change": ("0", "0",), "mvt": (">", ">",)}, 
                    ("1", "#",): {"dest": "cop", "change": ("1", "1",), "mvt": (">", ">",)},
                    ("#", "#",): {"dest": "ret", "change": ("#", "#",), "mvt": ("-", "<",)}},

                "ret": {("#", "0",): {"dest": "ret", "change": ("#", "0",), "mvt": ("-", "<",)}, 
                    ("#", "1",): {"dest": "ret", "change": ("#", "1",), "mvt": ("-", "<",)},
                    ("#", "#",): {"dest": "tes", "change": ("#", "#",), "mvt": ("<", ">",)}},

                "tes": {("0", "0",): {"dest": "tes", "change": ("0", "0",), "mvt": ("<", ">",)}, 
                    ("1", "1",): {"dest": "tes", "change": ("1", "1",), "mvt": ("<", ">",)},
                    ("#", "#",): {"dest": "F", "change": ("#", "#",), "mvt": ("-", "-",)}}}
    nbr = 2
    # Rassemblé
    #Tur = {"Si": Si, "Ga": Ga, "Qe": Qe, "qi": qi, "qf": qf, "dico": Dedico, "nbr": nbr}
    Tur = reader("turs\\COPY12.tur")    ## Racine du projet + ...

    Mac = Machine(Tur, "10011")

    etat = Tur["qi"]
    while etat != Tur["qf"]:
        Mac.pas()
        etat = Mac.get_etatActu()
        print(etat)
        if etat == "Non accepté":
            break

