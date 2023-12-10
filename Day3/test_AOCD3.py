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