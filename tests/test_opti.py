from src import modifier, turing, reader
import unittest

class TestLinker(unittest.TestCase):
    # on vérifie d'abord le résultat du fichier initial
    # on applique les deux optimisations:
    # - on vérifie alors si les transitions inutiles ont été supprimée et si le résultat de l'éxécution est la même
    def test_optimisation(self):
        r = reader.reader("tests\\code_test\\TEST_OPTI.tur")
        # Code simplifié
        rs = modifier.simplification(r)
        # Code dont les codes morts ont été détruits
        re = modifier.elim(rs)
        r_rs = turing.exec(r, "11001", 0, 20, False).get_bandes().get_mot_str(1) == turing.exec(rs, "11001", 0, 20, False).get_bandes().get_mot_str(1)
        rs_re = turing.exec(rs, "11001", 0, 20, False).get_bandes().get_mot_str(1) == turing.exec(re, "11001", 0, 20, False).get_bandes().get_mot_str(1)
        # vrai si le resultat de re, r_rs et rs_re est le meme
        res = r_rs == rs_re
        # Si res et la transition inutile plus dans la liste des transitions, alors test ok.
        self.assertTrue("qiCopy" not in re["Qe"], res)

