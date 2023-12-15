from AOCD8 import *

def test_blank():
    assert True

def test_nextNode():
    assert nextNode("R", "LNN") == "FGF"
    assert nextNode("L", "CNV") == "QKQ"
    assert nextNode("R", "DTG") == "DBK"
    assert nextNode("L", "JNB") == "BPJ"

def test_gameLogic():
    nodes1 = {"AAA": ("BBB", "BBB"), "BBB" : ("AAA", "ZZZ"), "ZZZ" : ("ZZZ", "ZZZ")}
    nodes2 = {"AAA": ("BBB", "CCC"),
              "BBB": ("DDD", "EEE"),
              "CCC": ("ZZZ", "GGG"),
              "DDD": ("DDD", "DDD"),
              "EEE": ("EEE", "EEE"),
              "GGG": ("GGG", "GGG"),
              "ZZZ": ("ZZZ", "ZZZ")}
    nodes3 = {"AAA": ("BBB", "CCC"),
              "BBB": ("DDD", "EEE"),
              "CCC": ("DDD", "GGG"),
              "DDD": ("DDD", "ZZZ"),
              "EEE": ("EEE", "EEE"),
              "GGG": ("GGG", "GGG"),
              "ZZZ": ("ZZZ", "ZZZ")}
    assert gameLogic("LLR", "AAA", "ZZZ", nodes1) == 6
    assert gameLogic("RL", "AAA", "ZZZ", nodes2) == 2
    assert gameLogic("RL", "AAA", "ZZZ", nodes3) == 3
