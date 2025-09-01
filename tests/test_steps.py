import pytest

from src.turingsim.utils.reader import reader
from src.turingsim.core.TuringMachine import TuringMachine


def test_exec():
    r = reader("tests/code_test/TEST_STEPS.tur")
    t = TuringMachine(r)
    res = t.exec("11001", 0, 20)
    assert "".join(res[0]) == "#00110#"


def test_un_pas():
    r = reader("tests/code_test/TEST_STEPS.tur")
    t = TuringMachine(r)
    t.set_word("11001")
    t.pas()  # un seul pas
    assert "".join(t.tapes.tapes[0]) == "#01001"


def test_etoile():
    r = reader("tests/code_test/TEST_STEPS_etoile.tur")
    t = TuringMachine(r)
    res = t.exec("11001", 0, 20)
    # Vérifie la bande 2
    assert "".join(res[1]) == "#11001#"


def test_pourcent():
    r = reader("tests/code_test/TEST_STEPS_pourcent.tur")
    t = TuringMachine(r)
    res = t.exec("1124423", 0, 20)
    # Vérifie la bande 1
    assert "".join(res[0]) == "#1120022#"

