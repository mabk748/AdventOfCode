bag = {"red": 12, "green": 13, "blue": 14}

with open("inpd2.txt") as f:
    games = [game.replace('\n', '') for game in f.readlines()]

dgames = {}
for i in games:
    dgames[i.split(":")[0]] = [v.split(",") for v in i.split(":")[1].split(";")]


def is_possible(inp):
    isit = True
    for i in inp:
        for j in range(len(i)):
            if bag[i[j].split(" ")[2]] < int(i[j].split(" ")[1]):
                isit = False
    return isit


ddgames = {}

for k in range(1, 101):
    ddgames['Game ' + str(k)] = {}
    ddgames['Game ' + str(k)]["red"] = []
    ddgames['Game ' + str(k)]["green"] = []
    ddgames['Game ' + str(k)]["blue"] = []
    for i in dgames['Game ' + str(k)]:
        for j in range(len(i)):
            ddgames['Game ' + str(k)][i[j].split(" ")[2]].append(int(i[j].split(" ")[1]))

print(ddgames)

count = 0
for k in range(1, 101):
    count += max(ddgames['Game ' + str(k)]["red"]) * max(ddgames['Game ' + str(k)]["green"]) * max(ddgames['Game ' + str(k)]["blue"])
print(count)

# count = 0
# for i in range(1, 101):
#     if is_possible(dgames['Game ' + str(i)]) == True:
#         print(str(i) + " : " + str(dgames['Game ' + str(i)]))
#         count += i
# print(count)