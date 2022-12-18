from turing import *
from reader import *
import sys
import os
import time
from tkinter import Tk, filedialog

# Effectue un pas sans afficher les rubans
def un_pas(formel, mot):
    Tur = Machine(formel, mot)
    etat = formel["qi"]
    Tur.pas()
    etat = Tur.get_etatActu()

# Exécute la machine jusqu'à la fin
def exec(formel, mot, affiche = True):
    global vitesse

    Tur = Machine(formel, mot)
    etat = formel["qi"]
    os.system("cls")
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
    #for rubans in Tur.get_bandes().get_list():
     #   sys.stdout.write("".join(map(str, rubans["mot"])) + "\n")


# Affiche les rubans à chaques étapes. Elle s'adapte à la taille du terminal sur lequel le programme est éxécuté.
def affichage(tur):
    global TailleTerminal
    bandes = tur.get_bandes().get_list()
    for elem in bandes:
        pointeur = ["---" if _ != (TailleTerminal // 4) // 2 else " ^ " for _  in range(TailleTerminal // 4)]
        ruban = [" - " for _  in range(TailleTerminal // 4) ]
        indice = 1
        for lettre in elem["mot"]:
            ind = (TailleTerminal // 8) - elem["pos"] + indice - 1
            #
            if ind < 0:
                ind = 0
            elif ind > TailleTerminal // 4 - 1:
                ind = TailleTerminal // 4 - 1
            #
            if lettre == "#" or lettre == "+":
                lettre = "-"
   
            ruban[ind] = " " + lettre + " "
            #print(ruban)
            indice += 1
        sys.stdout.write("/".join(map(str, ruban)) + "\n")
        sys.stdout.write("-".join(map(str, pointeur)) + "\n")
    print("\n")

# Lance une interface minimale dans le terminal permettant de choisir:
# - la vitesse d'éxécution
# - le fichier contenant le code la machine de turing
# - un mot à traiter
def interface_exec():
    global vitesse
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    open_file = filedialog.askopenfilename(filetypes=[("Turing code", ".tur")])
    # Choisie le mot
    mot = input("Choisissez un mot. Les cases vides sont représentées par '#'..\n")

    # Choisie la vitesse
    vitesse = float(input("Choisissez une vitesse entre 0 et 5(temps d'attente en seconde)\n"))
    # ~10#11#11#00~
    formel = CodeTuring(open_file).get_auto()
    exec(formel, mot)

    re = input("Voulez-vous utiliser une autre machine?o/*\n")
    if re == "o" or re == "O":
        interface_exec()

def interface_linker():
    pass

if __name__ == "__main__":
    os.system("cls")
    # Détermine la taille du terminal pour adapter l'affichage
    size = os.get_terminal_size()
    TailleTerminal = size.columns
    if TailleTerminal < 20:
        print("La fenêtre est trop petite pour afficher correctement les rubans")
    else:
        # choix interface pour executer ou pour fusionner deux machines appelant et appelé
        while True:
            rep = input("Utiliser le linker: L\nExécutez une machine: E\nQuitter: Q\n")
            if rep == "E":
                os.system("cls")
                sys.stdout.write("Vous avez choisie l'éxécution d'une machine !\n")
                interface_exec()
                os.system("cls")
            elif rep == "L":
                os.system("cls")
                sys.stdout.write("Vous avez choisie d'utiliser le linker pour deux machine !\n")
                interface_linker()
                os.system("cls")
            elif rep == "Q":
                os.system("cls")
                sys.stdout.write("Aurevoir...")
                exit()

            

