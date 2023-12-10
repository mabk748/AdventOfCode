from AOCD3 import *

def test_blank():
    assert True

def test_inlargingInp():
    test = ["123456789",
            "123456789",
            "123456789"]
    assert inlargingInp(test) == [["." for _ in range(11)],
                                    [*".123456789."],
                                    [*".123456789."],
                                    [*".123456789."],
                                    ["." for _ in range(11)]]
                            
def test_fillingTempMat():
    test = [["." for _ in range(11)],
            [*".123456789."],
            [*".123456789."],
            [*".123456789."],
            ["." for _ in range(11)]]
    assert fillingTempMat(test, (1, 1)) == ([["." for _ in range(11)], [*".123456789."], [*".123456789."]], len(test[1]))

def test_areThereSymbols():
    assert areThereSymbols([["." for _ in range(11)], [*".123456789."], [*".123456789."]]) == False
    assert areThereSymbols([["." for _ in range(11)], [*".123456789."], [*".1234&6789."]]) == True

def test_numberInMat():
    assert numberInMat([["." for _ in range(11)], [*".123456789."], [*".123456789."]]) == "123456789"

def test_gameLogic():
    test = ["467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."]
    assert gameLogic(test) == 4361

#---------------------------Part 2---------------------------

def test_findingStars():
    test = inlargingInp(["467..114..",
                        "...*......",
                        "..35..633."])
    assert findingStars(test) == [(2, 4)]

def test_fillingTempMat9el():
    test = inlargingInp(["467..114..",
                        "...*......",
                        "..35..633."])
    assert fillingTempMat9el(test, (2,4)) == [[*"7.."], [*".*."], [*"35."]]

def test_comparingInd():
    assert comparingInd([(0, 1), (2, 0)], 0) == True
    assert comparingInd([(0, 1), (2, 0)], 1) == False

def test_areThereNumbers():
    assert areThereNumbers([[*"7.."], [*".*."], [*"35."]]) == True
    assert areThereNumbers([[*"..."], [*".*."], [*"..."]]) == False

