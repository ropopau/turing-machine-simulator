from typing import List, Tuple
class Tapes:
     # Initie une bande avec nbr nombre de rubans
    def __init__(self, nbr):
        self.tapes_nbr = nbr
        self.tapes: Tuple[List] = tuple([[] for _ in range(nbr)])
        self.tapes_pos = [0 for _ in range(nbr)]

    def init_word(self, mot):
        empty_tape: str = "#" * len(mot)
        self.tapes[0].extend(mot)
        for ind in range(1, self.tapes_nbr):
            self.tapes[ind].extend(empty_tape)

    # Vérifie qu'il y a au moins une case vide avant et après la position actuelle
    def verification(self):

        for ind in range(self.tapes_nbr):
            if self.tapes_pos[ind] == 0:
                self.tapes[ind].insert(0, "#")
                self.tapes_pos[ind] += 1
            elif self.tapes_pos[ind] == len(self.tapes[ind]):
                self.tapes[ind].append("#")
                

    # Getters et setters
    @property
    def tapes_and_pos(self):
        return [{"mot": self.tapes[ind], "pos": self.tapes_pos[ind]} for ind in range(self.tapes_nbr)]
    
    @property
    def tapes(self):
        return self._tapes
    
    @tapes.setter
    def tapes(self, value):
        self._tapes = value

    def set_lettre(self, quelRuban, lettre):
        self.tapes[quelRuban][self.tapes_pos[quelRuban]] = lettre

    def set_pos(self, quelRuban, mvt):
        if mvt == "<":
            self.tapes_pos[quelRuban] -= 1
        elif mvt == ">":
            self.tapes_pos[quelRuban] += 1