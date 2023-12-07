"""
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

with open("inpD1.txt") as f:
    inp = [i.replace("\n", "") for i in f]

def findingFirstNumber(st: str, startDirection: str) -> str:
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if startDirection == "right":
        for i in range(len([*st])):
            if [*st][i] in numbers:
                return [*st][i]
    elif startDirection == "left":
        for i in range(len([*st])-1, -1, -1):
            if [*st][i] in numbers:
                return [*st][i]

def gameLogic(st: str) -> int:
    return int(findingFirstNumber(st, "right") + findingFirstNumber(st, "left"))

print(sum([gameLogic(i) for i in inp]))

#---------------------------Part 2---------------------------

"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

def turningFirstLettersToNumbers(st: str, startDirection: str) -> str:
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numbersInLetters = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if startDirection == "right":
        ind = []
        for i in range(len(numbers)):
            if len(st.split(numbersInLetters[i])) > 0:
                ind.append((i, len(st.split(numbersInLetters[i])[0])))
        ind.sort(key=lambda x: x[1])
        nst = st.replace(numbersInLetters[ind[0][0]], numbers[ind[0][0]])
    if startDirection == "left":
        ind = []
        for i in range(len(numbers)):
            if len(st.split(numbersInLetters[i])) > 0:
                ind.append((i, len(st.split(numbersInLetters[i])[-1])))
        ind.sort(key=lambda x: x[1])
        nst = st.replace(numbersInLetters[ind[0][0]], numbers[ind[0][0]])
    return nst

def findingFirstNumberP2(st: str, startDirection: str) -> str:
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if startDirection == "right":
        nst = turningFirstLettersToNumbers(st, startDirection)
        for i in range(len([*nst])):
            if [*nst][i] in numbers:
                return [*nst][i]
    elif startDirection == "left":
        nst = turningFirstLettersToNumbers(st, startDirection)
        for i in range(len([*nst])-1, -1, -1):
            if [*nst][i] in numbers:
                return [*nst][i]
            
def gameLogicP2(st: str) -> int:
    return int(findingFirstNumberP2(st, "right") + findingFirstNumberP2(st, "left"))

print(sum([gameLogicP2(i) for i in inp]))