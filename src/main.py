import os
import sys
from interface import *

if __name__ == "__main__":
    os.system("cls")
    # Détermine la taille du terminal pour adapter l'affichage

    # choix interface pour executer ou pour fusionner deux machines appelant et appelé
    while True:
        os.system("cls")
        rep = input("Utiliser le linker: L\nExécuter une machine: E\nOptimiser un code de turing: O\nQuitter: Q\n")
        match rep:
            case "E" | "e":
                os.system("cls")
                sys.stdout.write("Vous avez choisie l'éxécution d'une machine !\n")
                interface_e()
                os.system("cls")
            case "L" | "l":
                os.system("cls")
                sys.stdout.write("Vous avez choisie d'utiliser le linker pour deux machine !\n")
                interface_l()
                os.system("cls")
            case "O" | "o":
                os.system("cls")
                sys.stdout.write("Vous avez choisie l'optimisation d'une machine !\n")
                interface_o()
            case "Q" | "q":
                os.system("cls")
                sys.stdout.write("Aurevoir...")
                exit()
            
            

            

