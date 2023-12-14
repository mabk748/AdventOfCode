from AOCD5 import *
from unittest import TestCase
TestCase.maxDiff = None

def test_blank():
    assert True

def test_createDict():
    testli =["seeds: 79 14 55 13",
            "",
            "seed-to-soil map:",
            "50 98 2",
            "52 50 48",
            "",
            "soil-to-fertilizer map:",
            "0 15 37",
            "37 52 2",
            "39 0 15",
            "",
            "fertilizer-to-water map:",
            "49 53 8",
            "0 11 42",
            "42 0 7",
            "57 7 4",
            "",
            "water-to-light map:",
            "88 18 7",
            "18 25 70",
            "",
            "light-to-temperature map:",
            "45 77 23",
            "81 45 19",
            "68 64 13",
            "",
            "temperature-to-humidity map:",
            "0 69 1",
            "1 0 69",
            "",
            "humidity-to-location map:",
            "60 56 37",
            "56 93 4"]
    TestCase().assertDictEqual(createDict(testli), {"seeds": "79 14 55 13", "seed-to-soil map": ["50 98 2", "52 50 48"], "soil-to-fertilizer map": ["0 15 37", "37 52 2", "39 0 15"], "fertilizer-to-water map": ["49 53 8", "0 11 42", "42 0 7", "57 7 4"], "water-to-light map": ["88 18 7", "18 25 70"], "light-to-temperature map": ["45 77 23", "81 45 19", "68 64 13"], "temperature-to-humidity map": ["0 69 1", "1 0 69"], "humidity-to-location map": ["60 56 37", "56 93 4"]})
    
def test_getSpace():
    assert getSpace((50, 2)) == [50, 51]
    assert getSpace((1, 69)) == [1+i for i in range(69)]

def test_linkingMaps():
    assert linkingMaps([98, 99], [50, 51]) == [[i for i in range(100)], [i for i in range(50)] + [i for i in range(52, 100)] + [50, 51]]

def test_getAdj():
    assert getAdj(79, linkingMaps([98, 99], [50, 51])) == 81
    assert getAdj(14, linkingMaps([98, 99], [50, 51])) == 14
    assert getAdj(55, linkingMaps([98, 99], [50, 51])) == 57
    assert getAdj(13, linkingMaps([98, 99], [50, 51])) == 13