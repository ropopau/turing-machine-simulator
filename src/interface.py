from tkinter import Tk, filedialog
from reader import *
from modifier import *
from linker import *
from turing import *
from os import listdir

def choix_fichier():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    open_file = filedialog.askopenfilename(filetypes=[("Turing code", ".tur")])
    return open_file

def interface_e():
    size = os.get_terminal_size()
    TailleTerminal = size.columns
    if TailleTerminal < 20:
        print("La fenêtre est trop petite pour afficher correctement les rubans")
    else:
        open_file = choix_fichier()
        mot = input("Choisissez un mot. Les cases vides sont représentées par '#'..\n")
        vitesse = float(input("Choisissez une vitesse entre 0 et 5(temps d'attente en seconde)\n"))
        formel = reader(open_file)
        exec(formel, mot, vitesse, TailleTerminal)
        re = input("Voulez-vous utiliser une autre machine?o/*\n")
        if re == "o" or re == "O":
            os.system("cls")
            interface_e()

def interface_l():
    open_file = choix_fichier()
    form = reader(open_file)
    auto = marqueur(form, "MAIN")
    listappel = []
    for etat, sousdic in auto["dico"].items():
        for lu, info in sousdic.items():
            if type(info["change"]) != tuple:
                listappel.append({"etat": etat, "lu": lu, "appel": info["change"], "dest": info["dest"], "mvt": info["mvt"]})
    if not listappel:
        print("La machine n'appelle aucune machine")
        exit()
    else:
        a = listdir("turs")
        possible = True
        for elem in listappel:
            if elem["appel"]+".tur" not in a:
                print("Il n'existe pas de fichier correspondant à la machine appelée: ",elem["appel"]," dans le répertoire")
                possible = False     
        if possible:
            a = link(auto, listappel)
            writer(a)
        else:
            print("Veuillez ajouter les fichiers *.tur nécessaire pour utiliser le linker.")


def interface_o():
    open_file = choix_fichier()
    form = reader(open_file)
    rep = input("Simplifier: S\nElimination: E\nLes deux: B\n")
    match rep:
        case "S" | "s":
            writer(simplification(form))
        case "E" | "e":
            writer(elim(form))
        case "B" | "b":
            writer(elim(simplification(form)))
