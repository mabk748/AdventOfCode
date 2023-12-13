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

def test_fillingTempMatP2():
    test = inlargingInp(["467..114..",
                        "...*......",
                        "..35..633."])
    test2 = inlargingInp(['484..969.', 
                          '.&....*..', 
                          '...258...'])
    assert fillingTempMatP2(test, (2,4)) == ([[*"7.."], [*".*."], [*"35."]], [(1, 3), (3, 3), (3, 4)])
    assert fillingTempMatP2(test2, (2, 7)) == ([['9', '6', '9'], ['.', '*', '.'], ['8', '.', '.']], [(1, 6), (1, 7), (1, 8), (3, 6)])

def test_comparingInd():
    assert comparingInd([(0, 1), (2, 0)], 0) == True
    assert comparingInd([(0, 1), (2, 0)], 1) == False

def test_areThereNumbers():
    assert areThereNumbers([[*"7.."], [*".*."], [*"35."]]) == True
    assert areThereNumbers([[*"..."], [*".*."], [*"..."]]) == False

def test_gettingNumbers():
    assert gettingNumbers([[*"467.."], [*"...*."], [*"..35."]], [(0, 2), (2, 2)]) == [467, 35]
    assert gettingNumbers([[*"..755."], [*".*...."], [*".598.."]], [(0, 3), (2, 1)]) == [755, 598]

def test_gameLogicP2():
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
    assert gameLogicP2(test) == 467835