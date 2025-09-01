import pytest

from src.turingsim.utils.reader import reader

def test_doublons():
    r = reader("tests/code_test/TEST_READER_DOUBLONS.tur")
    assert r == 101

def test_header():
    r = reader("tests/code_test/TEST_READER_HEADER.tur")
    assert r == 100

def test_nbr():
    r = reader("tests/code_test/TEST_READER_NBR.tur")
    assert r == 103

def test_transitions():
    r = reader("tests/code_test/TEST_READER_TRANSITION.tur")
    assert r == 102

