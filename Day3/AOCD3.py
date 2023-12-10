"""
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""

with open("/home/mohamed/Desktop/Projects/AdventOfCode/Day3/inpd3.txt") as f:
    lines = [word.replace('\n', '') for word in f.readlines()]

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def inlargingInp(inp: list[str]) -> list[list[str]]:
    mat = [[*inp[i]] for i in range(len(inp))]
    for i in range(len(mat)):
        mat[i].insert(0, ".")
        mat[i].append(".")
    mat.insert(0, ["." for _ in range(len(mat[0]))])
    mat.append(["." for _ in range(len(mat[0]))])
    return mat

def fillingTempMat(mat: list[list[str]], indexes: tuple[int, int]) -> tuple[list[list[str]], int]:
    temp = [[], [], []]
    count = 0
    for i in range(len(mat[0])):
        if mat[indexes[0]][indexes[1] + i] in NUMBERS:
            count += 1
        else:
            break
    temp[0].append(mat[indexes[0] - 1][indexes[1] - 1])
    temp[1].append(mat[indexes[0]][indexes[1] - 1])
    temp[2].append(mat[indexes[0] + 1][indexes[1] - 1])
    for i in range(count):
        temp[0].append(mat[indexes[0] - 1][indexes[1] + i])
        temp[1].append(mat[indexes[0]][indexes[1] + i])
        temp[2].append(mat[indexes[0] + 1][indexes[1] + i])
    temp[0].append(mat[indexes[0] - 1][indexes[1] + count])
    temp[1].append(mat[indexes[0]][indexes[1] + count])
    temp[2].append(mat[indexes[0] + 1][indexes[1] + count])
    endIndx = indexes[1] + count + 1
    return (temp, endIndx)


def areThereSymbols(mat: list[list[str]]) -> bool:
    isIt = False
    for l in mat:
        res = [i for i in l if i != "." and i not in NUMBERS]
        if len(res) > 0:
            isIt = True
    return isIt

def numberInMat(mat: list[list[str]]) -> str:
    num = ""
    for i in range(1, len(mat[1])-1):
        num += mat[1][i]
    return num

def gameLogic(inp: list[str]) -> int:
    mat = inlargingInp(inp)
    savedNums = []
    for i in range(1, len(mat) - 1):
        j = 1
        while(j<len(mat[i])):
            if mat[i][j] not in NUMBERS:
                j += 1
            else:
                temp = fillingTempMat(mat, (i, j))
                if areThereSymbols(temp[0]):
                    savedNums.append(int(numberInMat(temp[0])))
                j = temp[1]
    return sum(savedNums)

print(gameLogic(lines))