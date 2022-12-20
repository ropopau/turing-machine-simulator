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

def simplification(tur):
    dico = tur["dico"]
    nbr_rub = tur["nbr"]
    for etat, sousdic in dico.items():
        for lu, info in sousdic.items():
            if info["dest"] != tur["qf"]:
                if info["mvt"] == tuple(["-" for _ in range(nbr_rub)]) and lu in dico[info["dest"]].keys():
                    nvdest = dico[info["dest"]][lu]["dest"]
                    nvchange = dico[info["dest"]][lu]["change"]
                    nvmvt = dico[info["dest"]][lu]["mvt"]
                    dico[etat][lu] = {"dest": nvdest, "change": nvchange, "mvt": nvmvt}
    return tur

def elim(tur):
    dico = tur["dico"]
    ltrans = []
    ldest = []

    for etat0, sousdic0 in dico.items():
        for lu0, info0 in sousdic0.items():
            ltrans.append((etat0, lu0))
            if info0["dest"] not in ldest:
                ldest.append((info0["dest"], info0["change"]))
    for elem in ltrans:
            
        if elem not in ldest and elem[0] != tur["qi"]:
            del dico[elem[0]][elem[1]]
        if len(dico[elem[0]]) == 0:
            del dico[elem[0]]
    return tur






if __name__ == "__main__":
    pass
