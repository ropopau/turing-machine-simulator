from src import reader, turing
import unittest

class TestReader(unittest.TestCase):
    def test_doublons(self):
        r = reader.reader("tests\\code_test\\TEST_READER_DOUBLONS.tur")
        self.assertEqual(r, 101)

    def test_header(self):
        r = reader.reader("tests\\code_test\\TEST_READER_HEADER.tur")
        self.assertEqual(r, 100)

    def test_nbr(self):
        r = reader.reader("tests\\code_test\\TEST_READER_NBR.tur")
        self.assertEqual(r, 103)
    
    def test_transitions(self):
        r = reader.reader("tests\\code_test\\TEST_READER_TRANSITION.tur")
        self.assertEqual(r, 102)
    
    def test_read_Ok(self):
        r = reader.reader("tests\\code_test\\TEST_READER_Ok.tur")
        res = turing.exec(r, "11001", 0, 20, False)
        self.assertEqual(res.get_bandes().get_mot_str(1), "33223")  
