import os

def writer(tur):
    fichier = input("Choisissez un nom de fichier.\n")
    if os.path.exists("turs\\"+fichier+".tur"):
        rep = input("Un fichier de ce nom existe déjà. Voulez-vous le supprimer?o/*")
        if rep == "O" or rep == "o":
            os.remove("turs\\"+fichier+".tur")
            nom = input("Choisissez un nom pour la machine de turing.\n")
        else:
            writer(tur)
    else:
        nom = input("Choisissez un nom pour la machine de turing.\n")  
    pathee = os.path.join("turs", fichier+".tur")
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
                
def reader(fichier):
    nom = None # ok
    Si = [] # ok
    Ga = [] # ok
    Qe = [] # ok
    qi = None # ok
    qf = None # ok
    Dedico = {} # A faire
    nbr = None # ok

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
                    nom = temp[1]
                case 'init':
                    qi = temp[1]
                case 'accept':
                    qf = temp[1]
                case 'nbr':
                    nbr = int(temp[1])
        # Toute les transitions
        else:
            temp = b[ind].split(",") # Premiere ligne
            temp2 = b[ind + 1].split(",") # Deuxieme ligne

            # Ajout des etats
            if temp[0] not in Qe:
                Qe.append(temp[0])
            if temp2[0] not in Qe:
                Qe.append(temp2[0])

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

            if etat not in Dedico.keys():
                Dedico[etat] = {}
                if lu not in Dedico[etat].keys():
                    Dedico[etat][lu] = sous_dico
                else:
                    print("une transition est écrite deux fois")
                    break
            else:
                if lu not in Dedico[etat].keys():
                    Dedico[etat][lu] = sous_dico
                else:
                    print("une transition est écrite deux fois")
                    break
            ind += 1
        ind += 1
    
    return {"Si":Si, "Ga":Ga, "Qe":Qe, "qi": qi, "qf": qf, "dico": Dedico, "nbr": nbr}

if __name__ == "__main__":
    a = reader("turs\\TEST_LINKER.tur")    ## Racine du projet + ...
    print(a)


    