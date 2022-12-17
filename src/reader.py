from turing import *
from main import *

# Permet de lire un fichier et le convertie 
# en automate lisible par le programme
class CodeTuring(object):
    def __init__(self, fichier):
        self.nom = None # ok
        self.Si = [] # ok
        self.Ga = ["#"] # ok
        self.Qe = [] # ok
        self.qi = None # ok
        self.qf = None # ok
        self.Dedico = {} # A faire
        self.nbr = None # ok

        # Ouverture du fichier
        with open(fichier, "r") as f:
            a = f.readlines()
            b = [x.rstrip("\n") for x in a if not x[0].isspace() and x[0] != "/"]
        ind = 0   

        # Parcours du readlines
        while ind < len(b):
            # Info de la machine
            if b[ind][0] == "&":
                temp = b[ind].lstrip("&").split(": ")
                match temp[0]:
                    case 'name':
                        self.nom = temp[1]
                    case 'init':
                        self.qi = temp[1]
                    case 'accept':
                        self.qf = temp[1]
                    case 'nbr':
                        self.nbr = int(temp[1])
            # Toute les transitions
            else:
                temp = b[ind].split(",") # Premiere ligne
                temp2 = b[ind + 1].split(",") # Deuxieme ligne

                # Ajout des etats
                if temp[0] not in self.Qe:
                    self.Qe.append(temp[0])

                # Ajout de l'alphabet et de l'alphabet de travaille
                z = 1
                while z <= self.nbr:
                    if temp2[z] not in self.Si:
                        self.Si.append(temp2[z])
                        self.Ga.append(temp2[z])

                    if temp[z] not in self.Si:
                        self.Si.append(temp[z])
                        self.Ga.append(temp[z])
                    z += 1

                # Ajout des transitions
                etat = temp[0]
                lu = tuple(temp[1:self.nbr + 1])
                dest = temp2[0]
                change = tuple(temp2[1:self.nbr + 1])
                mvt = tuple(temp2[self.nbr + 1:self.nbr*2 + 1])
                sous_dico = {"dest": dest, "change": change, "mvt": mvt}

                if etat not in self.Dedico.keys():
                    self.Dedico[etat] = {}
                    if lu not in self.Dedico[etat].keys():
                        self.Dedico[etat][lu] = sous_dico
                    else:
                        print("une transition est écrite deux fois")
                        break
                else:
                    if lu not in self.Dedico[etat].keys():
                        self.Dedico[etat][lu] = sous_dico
                    else:
                        print("une transition est écrite deux fois")
                        break
                ind += 1
            ind += 1

    def get_dico(self):
        return self.Dedico
    
    def get_auto(self):
        return {"Si":self.Si, "Ga":self.Ga, "Qe":self.Qe, "qi": self.qi, "qf": self.qf, "dico": self.Dedico, "nbr": self.nbr}

if __name__ == "__main__":
    a = CodeTuring("turs\\TRI_BINAIRE.tur")    ## Racine du projet + ...
    print(a.get_dico())


    