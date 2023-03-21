try:
    while True:
        inNum, inSet = map(int, input().split())
        goal = list(map(int, (input().split())))
        for i in range(inSet):
            inChose = list(input().split())
            if inChose[0] == 'Q':
                stay, end = sorted([int(inChose[1]), int(inChose[2])])
                print(max(goal[(stay - 1):end]))
            else:
                goal[int(inChose[1]) - 1] = int(inChose[2])
except:
    pass
