class Tapes:
     # Initie une bande avec nbr nombre de rubans
    def __init__(self):
        self.__listRubans = []

    def init_word(self, nbr, mot):
        self.__listRubans = [{"mot": ["#" for _ in range (len(mot))], "pos":0} for _ in range (nbr)]
        self.__listRubans[0]["mot"] = list(mot)

    # Vérifie qu'il y a au moins une case vide avant et après la position actuelle
    def verification(self):
        for elem in self.__listRubans:
            if elem["pos"] == 0:
                self.ajoute_debut()
            elif elem["pos"] == len(elem["mot"]):
                self.ajoute_fin()
    # Ajoute une case vide au debut et a la fin
    def ajoute_debut(self):
        for elem in self.__listRubans:
            if elem["mot"][0] == "+":
                elem["mot"][0] = "#"
            elem["mot"].insert(0, "+")
            elem["pos"] += 1
    
    def ajoute_fin(self):
        for elem in self.__listRubans:
            if elem["mot"][-1] == "+":
                elem["mot"][-1] = "#"
            elem["mot"].append("+")

    # Getters et setters
    def get_list(self):
        return self.__listRubans

    def get_pos(self, quelRuban):
        return self.__listRubans[quelRuban]["pos"]
    
    def get_mot(self, quelRuban):
        return self.__listRubans[quelRuban]["mot"]
    
    def get_mot_str(self, quelRuban):
        return "".join(map(str, self.get_mot(quelRuban))).strip("+").strip("#")

    def set_lettre(self, quelRuban, lettre):
        rub = self.__listRubans[quelRuban]
        rub["mot"][rub["pos"]] = lettre

    def set_pos(self, quelRuban, mvt):
        if mvt == "<":
            self.__listRubans[quelRuban]["pos"] -= 1
        elif mvt == ">":
            self.__listRubans[quelRuban]["pos"] += 1