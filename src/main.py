from turing import *
from reader import *
import sys
import os
import time
from tkinter import Tk, filedialog

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
    global TailleTerminal
    bandes = tur.get_bandes().get_list()
    for elem in bandes:
        pointeur = ["---" if _ != (TailleTerminal // 5) // 2 else " ^ " for _  in range(TailleTerminal // 5)]
        ruban = [" - " for _  in range(TailleTerminal // 5)]
        indice = 1
        for lettre in elem["mot"]:
            ind = (TailleTerminal // 10) - elem["pos"] + indice - 1
            #
            if ind < 0:
                ind = 0
            elif ind > TailleTerminal // 5 - 1:
                ind = TailleTerminal // 5 - 1
            #
            if lettre == "#" or lettre == "+":
                lettre = "-"
   
            ruban[ind] = " " + lettre + " "
            #print(ruban)
            indice += 1
        sys.stdout.write("/".join(map(str, ruban)) + "\n")
        sys.stdout.write("-".join(map(str, pointeur)) + "\n")
    print("\n")



if __name__ == "__main__":
    #formel = CodeTuring("turs\\TRI_BINAIRE.tur").get_auto()
    #exec(formel, "~10#11#11#00#01#11#00#11#11#00#01#11#00~")
    size = os.get_terminal_size()
    TailleTerminal = size.columns

    root = Tk()
    root.withdraw()

    root.attributes('-topmost', True)
    open_file = filedialog.askopenfilename(filetypes=[("Turing code", ".tur")])
    formel = CodeTuring(open_file).get_auto()
    exec(formel, "~10#11#11#00#01#11#00#11#11#00#01#11#00~")

