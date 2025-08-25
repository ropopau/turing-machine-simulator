import os

# Demande le nom de la machine jusqu'à ce qu'il soit valide.
def demandenom():
    while True:
        nom = input("Choisissez un NOM pour la MACHINE DE TURING.\n")
        if nom.strip() == "":
            print("Veuillez entrer un nom valide.")
        else:
            return nom

# Demande le nom du fichier jusqu'à ce qu'il soit valide.
def demandefichier():
    while True:
        fichier = input("Choisissez un NOM de FICHIER.\n")
        if fichier.strip() == "":
            print("Veuillez entrer un nom valide.")
        else:
            if os.path.exists("turs\\"+fichier+".tur"):
                rep = input("Un FICHIER de ce nom existe déjà. Voulez-vous le supprimer?o/*\n")
                if rep == "O" or rep == "o":
                    os.remove("turs\\"+fichier+".tur")
                    return fichier
            else:
                return fichier
        
# Crée un fichier .tur avec les informations de la variable tur.
def writer(tur):
    fichier = demandefichier()
    nom = demandenom()
    pathee = os.path.join("turs", fichier + ".tur")
    with open(pathee, "a") as f:
        f.write("&name: "+nom+"\n")
        f.write("&init: "+tur["qi"]+"\n")
        f.write("&accept: "+tur["qf"]+"\n")
        f.write("&nbr: "+str(tur["nbr"])+ "\n")
        f.write("\n")
    
        for etat, sousdic in tur["dico"].items():
            for lu, info in sousdic.items():
                q = etat
                rd = ",".join(map(str,list(lu)))
                l1 = "{0},{1}".format(q, rd)
                qdest = info["dest"]
                wr = ",".join(map(str, list(info["change"])))
                mvt = ",".join(map(str, list(info["mvt"])))
                l2 = "{0},{1},{2}".format(qdest,wr,mvt)
                f.write(l1+"\n"+l2+"\n")
                f.write("\n")
                
# Lit un fichier .tur et renvoie la définition formel de la machine sous forme de dictionnaire.
def reader(fichier):
    Si = [] # ok
    Ga = [] # ok
    Qe = [] # ok
    Dedico = {} # A faire
    nom, qi, qf, nbr = None, None, None, None
    # Ouverture du fichier
    with open(fichier, "r") as f:
        a = f.readlines()
        b = [x.rstrip("\n") for x in a if not x[0].isspace() and x[0] != "/"]
    ind = 0   

    # Parcours du readlines
    while ind < len(b):
        if b[ind][0] == "&" and ": " in b[ind]:
            temp = b[ind].lstrip("&").split(": ")
            if len(temp) == 2 and "" not in temp:
                match temp[0]:
                    case 'name':
                        nom = temp[1]
                    case 'init':
                        qi = temp[1]
                    case 'accept':
                        qf = temp[1]
                    case 'nbr':
                        nbr = int(temp[1])
                        if nbr == None:
                            return 100
        # Toute les transitions
        else:
            if type(nbr) == int and nbr >= 1:

                res = read_transi(b, ind, Si, Ga, Qe, Dedico, nbr)
                if res in [101, 102, 103]:
                    return res
                ind += 1
        ind += 1
    if None in [nom, qi, qf, nbr]:
        return 100
    
    return {"Si":Si, "Ga":Ga, "Qe":Qe, "qi": qi, "qf": qf, "dico": Dedico, "nbr": nbr}

# lit les transitions pour les en déduire l'alphabet, l'alphabet de travaille, les états, le nombre de ruban ainsi que le dictionnaire des transitions.
def read_transi(b, ind, Si, Ga, Qe, Dedico, nbr):
    temp = b[ind].split(",") # Premiere ligne
    temp2 = b[ind + 1].split(",") # Deuxieme ligne
    if "" in temp or "" in temp2:
        return 102

    # Ajout des etats
    if temp[0] not in Qe:
        Qe.append(temp[0])
    if temp2[0] not in Qe:
        Qe.append(temp2[0])
    try:
        if len(temp2[1]) == 1:
            # Ajout des transitions
            etat = temp[0]
            lu = tuple(temp[1:nbr + 1])
            dest = temp2[0]
            change = tuple(temp2[1:nbr + 1])
            mvt = tuple(temp2[nbr + 1:nbr*2 + 1])
            sous_dico = {"dest": dest, "change": change, "mvt": mvt}
            z = 1
            while z <= nbr:
                if temp2[z] not in Ga:
                    Ga.append(temp2[z])
                    if temp2[z] != "#":
                        Si.append(temp2[z])
                    

                if temp[z] not in Ga:
                    Ga.append(temp[z])
                    if temp[z] != "#":
                        Si.append(temp[z])
                    
                z += 1
        elif len(temp2[1]) > 1:
            # Ajout des transitions
            etat = temp[0]
            lu = tuple(temp[1:nbr + 1])
            dest = temp2[0]
            change = temp2[1]
            mvt = tuple(temp2[nbr + 1:nbr*2 + 1])
            sous_dico = {"dest": dest, "change": change, "mvt": mvt}
            # Ajout de l'alphabet et de l'alphabet de travaille
            z = 1
            while z <= nbr:
                if temp[z] not in Ga:
                    Ga.append(temp[z])
                    if temp[z] != "#":
                        Si.append(temp[z])
                z += 1
    except:
        return 103
    # Verif si l'état est déjà dans le dico de transition
    if etat not in Dedico.keys():
        # Si non, on initie un dico vide
        Dedico[etat] = {}
        # Si il n'est pas encore dans la liste des caractère pour cet état, on le rajoute
        if lu not in Dedico[etat].keys():
            # On rajoute les information à cet endroit
            Dedico[etat][lu] = sous_dico
        # Sinon, si cette liste de caractère lu est déjà présente, alors on lève une erreur
        else:
            return 101
    else:
        # on considère que l'état possède déjà sa place dans le dictionnaire des transitions

        if lu not in Dedico[etat].keys():
            Dedico[etat][lu] = sous_dico
        else:
            return 101


if __name__ == "__main__":
    a = reader("tests\code_test\TEST_STEPS.tur")    ## Racine du projet + ...


    