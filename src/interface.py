from tkinter import Tk, filedialog
from reader import *
from modifier import *
from linker import *
from turing import *
from main import exception
import os

# Ouvre une fenêtre de choix de fichier .tur
def choix_fichier():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    while True:
        open_file = filedialog.askopenfilename(filetypes=[("Turing code", ".tur")])
        if open_file.strip() != "":
            break
        
    return open_file

# Lance l'éxécution d'une machine
def interface_e():
    size = os.get_terminal_size()
    TailleTerminal = size.columns
    if TailleTerminal < 20:
        print("La fenêtre est trop petite pour afficher correctement les rubans")
    else:
        open_file = choix_fichier()
        formel = reader(open_file)
        
        if formel in list(exception.keys()):
            return formel
        else:
            # Pour vérifier si il appelle une autre machine ou non.
            verifappel = verif(formel)
            if verifappel:
                return 7
            
            mot = input("Choisissez un mot. Les cases vides sont représentées par '#'..\n")
            while True:
                vitesse = input("Choisissez une vitesse entre 0 et 5(temps d'attente en seconde)\n")
                if vitesse in ["0","1","2","3","4","5"]:
                    vitesse = float(vitesse)
                    break
                
            exec(formel, mot, vitesse, TailleTerminal)
            re = input("Voulez-vous utiliser une autre machine?o/*\n")
            if re == "o" or re == "O":
                os.system("cls")
                interface_e()

# Lance l'éxécution du linker
def interface_l():
    open_file = choix_fichier()
    form_b = reader(open_file)
    if form_b in list(exception.keys()):
        return form_b
    else:
        res = linker(form_b)
        return res

# Lance l'éxécution des optimisations
def interface_o():
    open_file = choix_fichier()
    form = reader(open_file)
    if form in list(exception.keys()):
        return form
    else:
        if verif(form):
            return 7
        rep = input("Simplifier: S\nElimination: E\nLes deux: B\n")
        match rep:
            case "S" | "s":
                a = simplification(form)
                return a
            case "E" | "e":
                a = elim(form)
                return a
            case "B" | "b":
                b = simplification(form)
                a = elim(b)
                return a
            case _:
                exception[form]

