def sourcesAndSinks(nodes, adjacency_matrix):
    sources = []
    sinks = []
    for i in range(nodes):
        if sum(adjacency_matrix[i]) == 0:
            sinks.append(i + 1)
    j = 1
    for column in zip(*adjacency_matrix):
        if sum(list(column)) == 0:
            sources.append(j)
        j += 1
    return sources, sinks
    
nodes = int(input())
adjacency_matrix = []
for _ in range(nodes):
    adjacency_matrix.append(list(map(int, input().split())))

sources, sinks = sourcesAndSinks(nodes, adjacency_matrix)

print(len(sources), end=" ")
for source in sorted(sources):
    print(source, end=" ")
print()
print(len(sinks), end=" ")
for sink in sorted(sinks):
    print(sink, end=" ")
