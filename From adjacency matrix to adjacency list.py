from collections import defaultdict
vertices = int(input())
adjacency_matrix = []
for _ in range(vertices):
    adjacency_matrix.append(list(map(int, input().split())))

adjacency_list = defaultdict(list)
for i in range(vertices):
    for j in range(vertices):
        if adjacency_matrix[i][j]:
            adjacency_list[i + 1].append(j + 1)
for adjacent in adjacency_list.values():
    print(len(adjacent), end=' ')
    for adj in sorted(adjacent):
        print(adj, end=" ")
    print()