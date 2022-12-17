from turing import *
from reader import *
import sys
import os
import time

def un_pas(formel, mot):
    Tur = Machine(formel, mot)


    etat = formel["qi"]
    Tur.pas()
    etat = Tur.get_etatActu()
    print(etat)

def exec(formel, mot, affiche = True):
    Tur = Machine(formel, mot)

    etat = formel["qi"]
    os.system("cls")
    while etat != formel["qf"]:
        Tur.pas()
        etat = Tur.get_etatActu()
        if affiche:
            print(etat)
            affichage(Tur)
            time.sleep(0.2)
            os.system("cls")
        if etat == "Non accepté":
            break
    print("Etat: ", etat)
    affichage(Tur)


def affichage(tur):
    bandes = tur.get_bandes().get_list()
    for elem in bandes:
        pointeur = ["---" if _ != 15 else " ^ " for _  in range(31)]
        ruban = [" - " for _  in range(31)]
        indice = 1
        for lettre in elem["mot"]:
            ind = 15 - elem["pos"] + indice - 1
            #
            if ind < 0:
                ind = 0
            elif ind > 30:
                ind = 30
            #
            if lettre == "#" or lettre == "+":
                lettre = "-"
            ruban[ind] = " " + lettre + " "
            #print(ruban)
            indice += 1
        sys.stdout.write("/".join(map(str, ruban)) + "\n")
        sys.stdout.write("-".join(map(str, pointeur)) + "\n")
    print("\n")


    """
    for elem in bandes:
        a = ["---" if _ != 15 else " ^ " for _  in range(31)]
        b = [" - " for _  in range(31)]
        i = 0
        print(elem.get_mot())
        for elem2 in "".join(map(str, elem.get_mot())).strip("+"):
            
            ind = 15 - elem.get_pos() + 1 + i
            if ind < 0:
                ind = 0
            elif ind > 30:
                ind = 30
            if elem2 == "#":
                elem2 = "-"
            b[ind] = " " + elem2 + " "
            i += 1

        sys.stdout.write("/".join(map(str, b)) + "\n")
        sys.stdout.write("-".join(map(str, a)) + "\n")
    print("\n")
    """


if __name__ == "__main__":
    formel = CodeTuring("turs\\TRI_BINAIRE.tur").get_auto()
    exec(formel, "~10#11#11#00#01#11#00#11#11#00#01#11#00~")
    pass