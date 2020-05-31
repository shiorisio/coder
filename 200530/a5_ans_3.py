t = input()

before_and_max = [[0, 0, 0] for i in range(len(t))]

for i in range(len(t)):
    if i == 0:
        if t[0] == "0":
            before_and_max[0][0] = 0
            before_and_max[0][1] = 0
            before_and_max[0][2] = 0
        else:
            before_and_max[0][0] = 1
            before_and_max[0][1] = 1
            before_and_max[0][2] = 0
    else:
        if t[i] == "0":
            before_and_max[i][0] = before_and_max[i - 1][0] + max(before_and_max[i-1][1], before_and_max[i-1][2])
            before_and_max[i][1] = max(before_and_max[i-1][1], before_and_max[i-1][2])
            before_and_max[i][2] = max(before_and_max[i-1][1], before_and_max[i-1][2])
        else:
            before_and_max[i][0] = before_and_max[i - 1][0] + ((i + 1) // 2 + (i + 1) % 2)
            before_and_max[i][1] = before_and_max[i - 1][2] + 1
            before_and_max[i][2] = before_and_max[i - 1][1]

print(before_and_max[len(t) - 1][0])
