with open("inpd3.txt") as f:
    lines = [word.replace('\n', '') for word in f.readlines()]

""" lines = ["467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."] """

ind = {}
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in range(len(lines)):
    ind["line " + str(i)] = {}
    ind["line " + str(i)]["symbols"] = []
    ind["line " + str(i)]["numbers"] = []

for i in range(len(lines)):
    for p, j in enumerate([*lines[i]]):
        if j != ".":
            if j in numbers:
                ind["line " + str(i)]["numbers"].append(p)
            else:
                ind["line " + str(i)]["symbols"].append(p)

adjl = [(0, 1)] + [(i-1, i, i+1) for i in range(1, len(lines)-1)] + [(len(lines)-2, len(lines)-1)]


print(adjl)
print(len(lines))
v = []
for n, i in enumerate(adjl):
        for k in ind["line " + str(n)]["numbers"]:
            #print("line " + str(n))
            #print("k = ", k)
            if (k-1 in [s for l in i for s in ind["line " + str(l)]["symbols"]]) or (k in [s for l in i for s in ind["line " + str(l)]["symbols"]]) or (k+1 in [s for l in i for s in ind["line " + str(l)]["symbols"]]):
                v.append((n, k))
                #print((n, k))


for i in range(len(lines)):
    ind["line " + str(i)]["numbers+ind"] = []
    if len(ind["line " + str(i)]["numbers"]) > 0:
        ind["line " + str(i)]["numbers+ind"].append([ind["line " + str(i)]["numbers"][0]])
        for j in range(1, len(ind["line " + str(i)]["numbers"])):
                if ind["line " + str(i)]["numbers"][j-1] == ind["line " + str(i)]["numbers"][j]-1:
                    ind["line " + str(i)]["numbers+ind"][-1].append(ind["line " + str(i)]["numbers"][j])
                else:
                    ind["line " + str(i)]["numbers+ind"].append([ind["line " + str(i)]["numbers"][j]])

indnums = []
for i in v:
    for k in ind["line " + str(i[0])]["numbers+ind"]:
        if i[1] in k:
            indnums.append((i[0], k))


nums = []
for i in indnums:
    s = ""
    for j in i[1]:
        s += lines[i[0]][j]
    nums.append((i[0], s))

nums = list(set(nums))

#print(nums)
nums.sort(key = lambda x: x[0]) 

print(nums)

count = 0
for i in nums:
    count += int(i[1])

print(count)