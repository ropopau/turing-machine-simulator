import unittest
from src import turing, reader

class TestSteps(unittest.TestCase):
    def test_exec(self):
        r = reader.reader("tests\\code_test\\TEST_STEPS.tur")
        res = turing.exec(r, "11001", 0, 20, False)
        self.assertEqual(res.bandes.get_mot_str(0), "00110" )

    def test_un_pas(self):
        r = reader.reader("tests\\code_test\\TEST_STEPS.tur")
        res = turing.un_pas(r, "11001")
        self.assertEqual(res.bandes.get_mot_str(0), "01001" )
    
    def test_etoile(self):
        r = reader.reader("tests\\code_test\\TEST_STEPS_etoile.tur")
        res = turing.exec(r, "11001", 0, 20, False)
        # Verifie la bande 2
        self.assertEqual(res.bandes.get_mot_str(1), "11001" )

    def test_pourcent(self):
        r = reader.reader("tests\\code_test\\TEST_STEPS_pourcent.tur")
        res = turing.exec(r, "1124423", 0, 20, False)
        # Verifie la bande 1
        self.assertEqual(res.bandes.get_mot_str(0), "1120022" )
