from AOCD4 import *

def test_blank():
    assert True

def test_turnToDict():
    liTest = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
              "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
              "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
              "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
              "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
              "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
    assert turnToDict(liTest) == {"Card 1": ["41 48 83 86 17", "83 86  6 31 17  9 48 53"],
                                  "Card 2": ["13 32 20 16 61", "61 30 68 82 17 32 24 19"],
                                  "Card 3": [" 1 21 53 59 44", "69 82 63 72 16 21 14  1"],
                                  "Card 4": ["41 92 73 84 69", "59 84 76 51 58  5 54 83"],
                                  "Card 5": ["87 83 26 28 32", "88 30 70 12 93 22 82 36"],
                                  "Card 6": ["31 18 13 56 72", "74 77 10 23 35 67 36 11"]}
    
def test_findingNumOfSame():
    assert findingNumOfSame("41 48 83 86 17", "83 86  6 31 17  9 48 53") == 4
    assert findingNumOfSame("13 32 20 16 61", "61 30 68 82 17 32 24 19") == 2
    assert findingNumOfSame(" 1 21 53 59 44", "69 82 63 72 16 21 14  1") == 2
    assert findingNumOfSame("41 92 73 84 69", "59 84 76 51 58  5 54 83") == 1
    assert findingNumOfSame("87 83 26 28 32", "88 30 70 12 93 22 82 36") == 0
    assert findingNumOfSame("31 18 13 56 72", "74 77 10 23 35 67 36 11") == 0

def test_score():
    assert score(4) == 8
    assert score(2) == 2
    assert score(2) == 2
    assert score(1) == 1
    assert score(0) == 0
    assert score(0) == 0

def test_probLogic():
    inp = {"Card 1": ["41 48 83 86 17", "83 86  6 31 17  9 48 53"],
            "Card 2": ["13 32 20 16 61", "61 30 68 82 17 32 24 19"],
            "Card 3": [" 1 21 53 59 44", "69 82 63 72 16 21 14  1"],
            "Card 4": ["41 92 73 84 69", "59 84 76 51 58  5 54 83"],
            "Card 5": ["87 83 26 28 32", "88 30 70 12 93 22 82 36"],
            "Card 6": ["31 18 13 56 72", "74 77 10 23 35 67 36 11"]}
    assert probLogic(inp) == 13

#---------------------------Part 2---------------------------

def test_probLogicP2():
    inp = {"Card 1": ["41 48 83 86 17", "83 86  6 31 17  9 48 53"],
            "Card 2": ["13 32 20 16 61", "61 30 68 82 17 32 24 19"],
            "Card 3": [" 1 21 53 59 44", "69 82 63 72 16 21 14  1"],
            "Card 4": ["41 92 73 84 69", "59 84 76 51 58  5 54 83"],
            "Card 5": ["87 83 26 28 32", "88 30 70 12 93 22 82 36"],
            "Card 6": ["31 18 13 56 72", "74 77 10 23 35 67 36 11"]}
    assert probLogicP2(inp) == 30