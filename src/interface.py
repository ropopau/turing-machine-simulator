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
    form_b = reader(open_file)
    res = linker(form_b)

    writer(res)


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
