from AOCD7 import *

def test_blank():
    assert True

def test_whereInHand():
    assert whereInHand("QQQJA") == {"Q": [0, 1, 2], "J": [3], "A": [4]}
    assert whereInHand("KTJJT") == {"K": [0], "T": [1, 4], "J": [2, 3]}
    assert whereInHand("KK677") == {"K": [0, 1], "6": [2], "7": [3, 4]}
    assert whereInHand("32T3K") == {"3": [0, 3], "2": [1], "T": [2], "K": [4]}

def test_defineCombine():
    assert defineCombines(whereInHand("32T3K")) == "One pair"
    assert defineCombines(whereInHand("T55J5")) == "Three of a kind"
    assert defineCombines(whereInHand("KK677")) == "Two pair"
    assert defineCombines(whereInHand("KTJJT")) == "Two pair"
    assert defineCombines(whereInHand("QQQJA")) == "Three of a kind"
    assert defineCombines(whereInHand("AAAAA")) == "Five of a kind"
    assert defineCombines(whereInHand("AAAJA")) == "Four of a kind"
    assert defineCombines(whereInHand("23456")) == "High card"

def test_strongerHand():
    assert strongerHand("32T3K", "23456") == "32T3K"
    assert strongerHand("AAAJA", "AAAAA") == "AAAAA"
    assert strongerHand("KK677", "KTJJT") == "KK677"
    assert strongerHand("2AAAA", "33332") == "33332"

def test_gameLogic():
    assert gameLogic(["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]) == 6440

#---------------------------Part 2---------------------------

def test_whereInHandP2():
    assert whereInHandP2("QQQJA") == {"Q": [0, 1, 2, 3], "A": [4]}
    assert whereInHandP2("KTJJT") == {"K": [0], "T": [1, 4, 2, 3]}
    assert whereInHandP2("KK677") == {"K": [0, 1], "6": [2], "7": [3, 4]}
    assert whereInHandP2("32T3K") == {"3": [0, 3], "2": [1], "T": [2], "K": [4]}
    assert whereInHandP2("JJJJJ") == {"J": [0, 1, 2, 3, 4]}

def test_defineCombineP2():
    assert defineCombines(whereInHandP2("32T3K")) == "One pair"
    assert defineCombines(whereInHandP2("T55J5")) == "Four of a kind"
    assert defineCombines(whereInHandP2("KK677")) == "Two pair"
    assert defineCombines(whereInHandP2("KTJJT")) == "Four of a kind"
    assert defineCombines(whereInHandP2("QQQJA")) == "Four of a kind"
    assert defineCombines(whereInHandP2("AAAAA")) == "Five of a kind"
    assert defineCombines(whereInHandP2("AAAJA")) == "Five of a kind"
    assert defineCombines(whereInHandP2("23756")) == "High card"
    assert defineCombines(whereInHandP2("23J56")) == "One pair"

def test_strongerHandP2():
    assert strongerHandP2("32T3K", "23456") == "32T3K"
    assert strongerHandP2("AAAJA", "AAA7A") == "AAAJA"
    assert strongerHandP2("KK677", "KTJJT") == "KTJJT"
    assert strongerHandP2("2AAAA", "33332") == "33332"

def test_gameLogicP2():
    assert gameLogicP2(["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]) == 5905