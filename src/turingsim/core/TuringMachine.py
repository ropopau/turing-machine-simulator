import time
from copy import *
from ..utils.misc import clear_screen
from .Tapes import Tapes

class TuringMachine:
    def __init__(self, formel):
        # Ecriture formelle de a machine
        self.__formel = formel
        # Objet bande qui contient toute les tapes d'une machine
        self.tapes = Tapes(formel["nbr"])
        # l'état actuelle
        self.__etatActu = self.__formel["qi"]
        # Pile qui sera utilisé lors de la lecture des lettres:
        # elle se remplie puis se vide à chaque transition
        self.__pile = []

    # Un pas de la machine. 
    def pas(self):
        self.tapes.verification()
        
        ## Récupérations des lettres lu à l'état actuel
        for ruban in self.tapes.tapes_and_pos:
            a = ruban["mot"][ruban["pos"]]
            
            self.__pile.append(a)

        # Etat dont une transition s'en suit
        lu_actu = list(self.__formel["dico"][self.__etatActu].keys())
        a = tuple(["%" for _ in range(self.__formel["nbr"])])

        # Pour les transitions etoile
        for lu in lu_actu:
            if list(lu).count("*")  == 1 :
                for indice in range(len(lu)):
                    if lu[indice] == "*":
                        lettre_etoile = self.__pile[indice]
                if lettre_etoile == "#":
                    break
                info = deepcopy(self.__formel["dico"][self.__etatActu][lu])
                ch = list(info["change"])
                for i in range(len(ch)):
                    if ch[i] == "*":
                        ch[i] = lettre_etoile
                info["change"] = ch
                self.__formel["dico"][self.__etatActu][tuple(self.__pile)] = info
                lu_actu.append(tuple(self.__pile))
            elif list(lu).count("*") > 1:
                print("il y a trop plus d'un carcatère étoile.")
                quit()
        
        # Il ne peut pas avoir plus de deux étoile par transitions: Une étoile = Un caractère appartenant a l'alphabet.
        if tuple(self.__pile) in lu_actu or a in lu_actu:
            if a in lu_actu:
                pile_temp = a
                nvllettres = tuple(self.__pile)
                nvlmvts = self.__formel["dico"][self.__etatActu][a]["mvt"]
            # Si il est présent alors cela veut dire qu'il existe une transition pour ces lettres
            # On détermine alors les nvl lettres et mouvements
            else:
                pile_temp = tuple(self.__pile)
                nvllettres = self.__formel["dico"][self.__etatActu][tuple(self.__pile)]["change"]
                nvlmvts = self.__formel["dico"][self.__etatActu][tuple(self.__pile)]["mvt"]
            # Pour toute les tapes, 
            for i in range(len(self.__pile)):
                listrub = self.tapes
                if tuple(nvllettres) != tuple(["%" for _ in range(self.__formel["nbr"])]):
                    listrub.set_lettre(i, nvllettres[i])
                #print(listrub.get_mot(0))
                listrub.set_pos(i, nvlmvts[i])
            # Changement de l'état actuel
            self.__etatActu = self.__formel["dico"][self.__etatActu][pile_temp]["dest"]
        else:
            self.__etatActu = "Non accepté"
        # On vide la pile pour l'itération suivante
        self.__pile.clear()

    # Exécute la machine jusqu'à la fin
    def exec(self, mot, vitesse, tailleterm):
        global taillet
        taillet = tailleterm
        self.set_word(mot)
        etat = self.__formel["qi"]

        steps = []
        steps.append(deepcopy(self.tapes.tapes_and_pos))

        self.affichage(etat, vitesse)
        while etat != self.__formel["qf"]:
            self.pas()
            etat = self.__etatActu

            print(etat)
            steps.append(deepcopy(self.tapes.tapes_and_pos))

            self.affichage(etat, vitesse)
            if etat == "Non accepté":
                break
        
        steps.append(deepcopy(self.tapes.tapes_and_pos))

        self.affichage(etat, vitesse)
        return steps

    # Affiche les rubans à chaques étapes. Elle s'adapte à la taille du terminal sur lequel le programme est éxécuté.
    @clear_screen
    def affichage(self, state: str = "", speed = 1, tapes = None):
        global taillet
        if tapes == None:
            tapes = self.tapes.tapes_and_pos
        

        for elem in tapes:
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
            print("/".join(map(str, ruban)) + "\n", end="")
            print("-".join(map(str, pointeur)) + "\n", end="")
        print("\n")
        print("Etat: {0}".format(state))
        time.sleep(speed)


    def set_word(self, word: str):
        self.tapes.init_word(word)

    @property
    def tapes(self) -> Tapes:
        return self._tapes

    @tapes.setter
    def tapes(self, value: Tapes):
        self._tapes = value