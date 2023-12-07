from AOCD6 import *

def test_blank():
    assert True

def test_getUsableData():
    assert getUsableData(['first:    1      2', 'second:  3    4']) == [(1, 3), (2, 4)]

def test_gameLogic():
    assert gameLogic((7, 9)) == 4
    assert gameLogic((15, 40)) == 8
    assert gameLogic((30, 200)) == 9

#-------------------------part 2-------------------------

def test_getUsableDataP2():
    assert getUsableDataP2(['first:    1      2', 'second:  3    4']) == [12, 34]