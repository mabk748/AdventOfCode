from AOCD1 import *

def test_blank():
    assert True

def test_findingFirstNumber():
    assert findingFirstNumber("1abc2", "right") == "1"
    assert findingFirstNumber("1abc2", "left") == "2"

def test_gameLogic():
    assert gameLogic("1abc2") == 12
    assert gameLogic("pqr3stu8vwx") == 38
    assert gameLogic("a1b2c3d4e5f") == 15
    assert gameLogic("treb7uchet") == 77

#---------------------------Part 2---------------------------

def test_turningLettersToNumbers():
    assert turningFirstLettersToNumbers("eightwothree", "right") == "8wothree"
    assert turningFirstLettersToNumbers("xtwone3four", "left") == "xtwone34"

def test_gameLogicP2():
    assert gameLogicP2("two1nine") == 29
    assert gameLogicP2("eightwothree") == 83
    assert gameLogicP2("abcone2threexyz") == 13
    assert gameLogicP2("xtwone3four") == 24
    assert gameLogicP2("4nineeightseven2") == 42
    assert gameLogicP2("zoneight234") == 14
    assert gameLogicP2("7pqrstsixteen") == 76