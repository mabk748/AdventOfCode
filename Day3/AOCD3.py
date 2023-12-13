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

#---------------------------Part 2---------------------------

"""
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

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

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""
import math

def findingStars(mat: list[list[str]]) -> list:
    indexes = []
    for i in range(1, len(mat) - 1):
        for j in range(1, len(mat[i]) - 1):
            if mat[i][j] == "*":
                indexes.append((i, j))
    return indexes

def fillingTempMatP2(mat: list[list[str]], indexes: tuple[int, int]) -> list[list[str]]:
    temp = [[], [], []]
    num_ind = []
    for i in [-1, 0, 1]:
        temp[0].append(mat[indexes[0] - 1][indexes[1] + i])
        if mat[indexes[0] - 1][indexes[1] + i] in NUMBERS:
            num_ind.append((indexes[0] - 1, indexes[1] + i))
        temp[1].append(mat[indexes[0]][indexes[1] + i])
        if mat[indexes[0]][indexes[1] + i] in NUMBERS:
            num_ind.append((indexes[0], indexes[1] + i))
        temp[2].append(mat[indexes[0] + 1][indexes[1] + i])
        if mat[indexes[0] + 1][indexes[1] + i] in NUMBERS:
            num_ind.append((indexes[0] + 1, indexes[1] + i))
    num_ind.sort(key=lambda x: x[0])

    """ st1, st2, st3 = False, False, False
    for i in range(indexes[1] + 2, len(mat[0])):
        #print(temp)
        if mat[indexes[0] - 1][i] in NUMBERS and mat[indexes[0] - 1][i - 1] in NUMBERS:
            temp[0].append(mat[indexes[0] - 1][i])
        else:
            st1 = True
        if mat[indexes[0]][i] in NUMBERS and mat[indexes[0]][i - 1] in NUMBERS:
            temp[1].append(mat[indexes[0]][i])
        else:
            st2 = True
        if mat[indexes[0] + 1][i] in NUMBERS and mat[indexes[0] + 1][i - 1] in NUMBERS:
            temp[2].append(mat[indexes[0] + 1][i])
        else:
            st3 = True
        if st1 and st2 and st3:
            break
    
    st1, st2, st3 = False, False, False
    for i in range(indexes[1] - 2, -1, -1):
        #print(temp)
        if mat[indexes[0] - 1][i] in NUMBERS and mat[indexes[0] - 1][i + 1] in NUMBERS:
            temp[0].insert(0, mat[indexes[0] - 1][i])
        else:
            st1 = True
        if mat[indexes[0]][i] in NUMBERS and mat[indexes[0]][i + 1] in NUMBERS:
            temp[1].insert(0, mat[indexes[0]][i])
        else:
            st2 = True
        if mat[indexes[0] + 1][i] in NUMBERS and mat[indexes[0] + 1][i + 1] in NUMBERS:
            temp[2].insert(0, mat[indexes[0] + 1][i])
        else:
            st3 = True
        if st1 and st2 and st3:
            break """
    return (temp, num_ind)

def comparingInd(l: list[tuple], el: int) -> bool:
    for i in l:
        for j in l:
            if i != j:
                if abs(i[el] - j[el]) > 1:
                    return True
    return False

def areThereNumbers(mat: list[list[str]]) -> bool:
    isIt = False
    indexes = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] in NUMBERS:
                indexes.append((i,j))
    if len(indexes) > 1 and (comparingInd(indexes, 0) or comparingInd(indexes, 1)):
            isIt = True
    return isIt

def gettingNumbers(mat: list[str], ind: list[tuple]) -> str:
    data = [[*i] for i in mat]
    nums = []
    for i in ind:
        print(i)
        num = data[i[0]][i[1]]
        r = 1
        l = -1
        for _ in range(len(data[0])):
            if data[i[0]][i[1] + r] in NUMBERS:
                num += data[i[0]][i[1] + r]
                r += 1
            elif data[i[0]][i[1] + l] in NUMBERS:
                num = data[i[0]][i[1] + l] + num
                l -= 1
            else:
                if int(num) not in nums:
                    nums.append(int(num))
                break
    return nums

def gameLogicP2(inp: list[str]) -> int:
    mat = inlargingInp(inp)
    stars = findingStars(mat)
    savedNums = []
    for i in stars:
        temp = fillingTempMatP2(mat, i)
        #print(temp)
        if areThereNumbers(temp[0]):
            nums = gettingNumbers(mat, temp[1])
            if len(nums) == 2:
                #print(gettingNumbers(mat, temp[1]))
                savedNums.append(math.prod(nums))
        #print("-------------------")
    return sum(savedNums)

print(gameLogicP2(lines))