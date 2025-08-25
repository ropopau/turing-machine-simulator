
# Pour utiliser le linker, il faudra marquer les etats de chaques machine par une meme lettre afin d'éviter les doublons.
def marqueur(dicos, char):
    Si = dicos["Si"]
    Ga = dicos["Ga"]
    Qe = [x + char for x in dicos["Qe"]]
    qi = dicos["qi"] + char
    qf = dicos["qf"] + char
    transi = dicos["dico"]
    nbr = dicos["nbr"]

    newTransi = {}
    for etat, soudic in transi.items():
        newsousdic = {}
        for lu, info in soudic.items():
            info["dest"] = info["dest"] + char
            newsousdic[lu] = info
        newTransi[etat + char] = newsousdic

    return {"Si":Si, "Ga":Ga, "Qe":Qe, "qi": qi, "qf": qf, "dico": newTransi, "nbr": nbr}


# Supprime les liaisons inutiles, qui n'apporte aucune modification.
def simplification(tur):
    dico = tur["dico"]
    nbr_rub = tur["nbr"]
    allmvt = tuple(["-" for _ in range(nbr_rub)])
    changepct = tuple(["%" for _ in range(nbr_rub)])
    for etat, sousdic in dico.items():
        for lu, info in sousdic.items():
            # Si les caractères lu et écrits sont les même et que les mouvements sont "-", et lu =/= changepct
            if lu == info["change"] and info["mvt"] == allmvt and lu != changepct:
                dest = info["dest"]
                if dest != tur["qf"]:
                    dico[etat][lu]["dest"] = dico[dest][lu]["dest"]
                    dico[etat][lu]["mvt"] = dico[dest][lu]["mvt"] 
            
    return tur

# Elimine le code mort
def elim(tur):
    dico = tur["dico"]
    etat_possible = {x:False for x in tur["Qe"]}
    for sousdic in dico.values():
        for info in sousdic.values():
            etat_possible[info["dest"]] = True
    for key, value in etat_possible.items():
        if value == False:
            tur["Qe"].remove(key)
            del dico[key]
    return tur

if __name__ == "__main__":
    import reader
    a = reader.reader("C:\\Users\\dsang\\OneDrive\\Documents\\TDL\\TDL\\turs\\TRI_BINAIRE.tur")
    print(a["dico"])
    b = simplification(a)

