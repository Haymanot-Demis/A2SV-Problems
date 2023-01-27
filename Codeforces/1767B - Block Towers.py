def BlockTower(tower:list):
    tower = [int(value) for value in tower]
    sortedTowers = sorted(tower[1:])
    for value in sortedTowers:
        if tower[0] < value:
            tower[0] += (value - tower[0] + 1)//2
    print(tower[0])

testcases = int (input())
towers = []
for _ in range(testcases):
    length = int (input())
    towers.append(input().split(" ")[:length])
for tower in towers:
    BlockTower(tower)