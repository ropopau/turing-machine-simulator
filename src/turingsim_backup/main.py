import os
import sys
from turingsim.interface import *

exception = {0: "La machine n'appelle aucune machine.\n",
            1: "Il n'existe pas de fichier correspondant à la machine appelée dans le répertoire.\n",
            2: "Veuillez ajouter les fichiers *.tur nécessaire pour utiliser le linker.\n",
            100: "Erreur de syntaxe dans l'entête.\n", 
            101: "Une transition est présente plus qu'une fois.\n", 
            102: "Erreur de syntaxe dans une transitions.\n",
            103: "Nombre de ruban incorrect.\n",
            105: "Il y un appel de machine. Utilisez d'abord le linker pour éxécuter cette machine.\n",
            7: "Il y a un appel de machine. Veuillez utiliser le linker avant d'utiliser cette fonctionnalité.\n"
            }

def main():
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
                r = interface_e()
                if r in list(exception.keys()):
                    sys.stdout.write(exception[r])
                    time.sleep(2)
                os.system("cls")
            case "L" | "l":
                os.system("cls")
                sys.stdout.write("Vous avez choisie d'utiliser le linker pour deux machine !\n")
                r = interface_l()
                if r in list(exception.keys()):
                    sys.stdout.write(exception[r])
                    time.sleep(2)
                else:
                    writer(r)
                os.system("cls")
            case "O" | "o":
                os.system("cls")
                sys.stdout.write("Vous avez choisie l'optimisation d'une machine !\n")
                r = interface_o()
                if r in list(exception.keys()):
                    print(exception[r])
                    time.sleep(2)
                else:
                    writer(r)
                os.system("cls")
            case "Q" | "q":
                os.system("cls")
                sys.stdout.write("Aurevoir...")
                exit()
            
            

            

if __name__ == "__main__":
    main()
