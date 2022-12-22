import unittest
from src import linker, reader, turing

class TestLinker(unittest.TestCase):
    def test_pas_dappel(self):
        r = reader.reader("tests\\code_test\\TEST_LINKER_No.tur")
        res = linker.linker(r)
        self.assertEqual(res, 0)

    def test_appel_mais_pas_appelant(self):
        r = reader.reader("tests\\code_test\\TEST_LINKER_Left.tur")
        res = linker.linker(r)
        self.assertEqual(res, 1)

    def test_appel_ok(self):
        r = reader.reader("tests\\code_test\\TEST_LINKER_Copy.tur")
        res = linker.linker(r)
        eq_res = {'Si': ['0', '1', '2'], 
                    'Ga': ['0', '1', '#', '2'], 
                    'Qe': ['qINIT', 'qACCEPT', 'qCopy', 'qACCCopy'], 
                    'qi': 'qINIT', 'qf': 'qACCEPT', 
                    'dico': {'qINIT': {('1', '#'): {'dest': 'qINIT', 'change': ('0', '#'), 'mvt': ('>', '>')}, 
                                        ('0', '#'): {'dest': 'qINIT', 'change': ('1', '#'), 'mvt': ('>', '>')}, 
                                        ('2', '#'): {'dest': 'qCopy', 'change': ('%', '%'), 'mvt': ('>', '>')}, 
                                        ('#', '#'): {'dest': 'qACCEPT', 'change': ('#', '#'), 'mvt': ('-', '-')}}, 
                            'qACCCopy': {('%', '%'): {'dest': 'qINIT', 'change': ('%', '%'), 'mvt': ('>', '>')}}, 
                            'qCopy': {('*', '#'): {'dest': 'qCopy', 'change': ('*', '*'), 'mvt': ('>', '>')}, 
                                    ('#', '#'): {'dest': 'qACCCopy', 'change': ('#', '#'), 'mvt': ('-', '-')}}}, 'nbr': 2}

        ex1 = turing.exec(res, "12001", 0, 20, False)
        ex2 = turing.exec(eq_res, "12001",0, 20, False)
        self.assertEqual(ex1.get_bandes().get_list(), ex2.get_bandes().get_list())
    
    def test_deux_appels(self):
        r = reader.reader("tests\\code_test\\TEST_LINKER_Copy_Erase.tur")
        res = linker.linker(r)
        eq_res = {'Si': ['0', '1', '3', '2'], 
                    'Ga': ['0', '1', '#', '3', '2'], 
                    'Qe': ['qINIT', 'qACCEPT', 'qCopy', 'qAccCopy', 'qErase', 'qAccErase'], 
                    'qi': 'qINIT', 
                    'qf': 'qACCEPT', 
                    'dico': {'qINIT': {('1', '#'): {'dest': 'qINIT', 'change': ('0', '#'), 'mvt': ('>', '>')}, 
                                        ('0', '#'): {'dest': 'qINIT', 'change': ('1', '#'), 'mvt': ('>', '>')}, 
                                        ('3', '#'): {'dest': 'qCopy', 'change': ('%', '%'), 'mvt': ('>', '>')}, 
                                        ('2', '#'): {'dest': 'qErase', 'change': ('%', '%'), 'mvt': ('>', '>')}, 
                                        ('#', '#'): {'dest': 'qACCEPT', 'change': ('#', '#'), 'mvt': ('-', '-')}}, 
                            'qAccCopy': {('%', '%'): {'dest': 'qINIT', 'change': ('%', '%'), 'mvt': ('-', '-')}}, 
                                'qCopy': {('*', '#'): {'dest': 'qCopy', 'change': ('#', '#'), 'mvt': ('>', '>')}, 
                                        ('#', '#'): {'dest': 'qAccCopy', 'change': ('#', '#'), 'mvt': ('-', '-')}}, 
                            'qAccErase': {('%', '%'): {'dest': 'qINIT', 'change': ('%', '%'), 'mvt': ('-', '-')}}, 
                                'qErase': {('*', '#'): {'dest': 'qErase', 'change': ('*', '*'), 'mvt': ('>', '>')}, 
                                        ('#', '#'): {'dest': 'qAccErase', 'change': ('#', '#'), 'mvt': ('-', '-')}}}, 'nbr': 2}
        ex1 = turing.exec(res, "132031", 0, 20, False)
        ex2 = turing.exec(eq_res, "132031",0, 20, False)

        self.assertEqual(ex1.get_bandes().get_list(), ex2.get_bandes().get_list())

if __name__ == '__main__':
    unittest.main()
