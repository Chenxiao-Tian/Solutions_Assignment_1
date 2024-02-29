def bellman_ford_with_path(adj_matrix, source):
    V = len(adj_matrix)
    distance = [float('inf')] * V
    distance[source] = 0
    predecessor = [-1] * V  # Store predecessors to reconstruct path

    # Relax all edges V-1 times
    for _ in range(V - 1):
        for i in range(V):
            for j in range(V):
                if adj_matrix[i][j] != 0 and distance[i] + adj_matrix[i][j] < distance[j]:
                    distance[j] = distance[i] + adj_matrix[i][j]
                    predecessor[j] = i

    # Check for negative-weight cycles
    for i in range(V):
        for j in range(V):
            if adj_matrix[i][j] != 0 and distance[i] + adj_matrix[i][j] < distance[j]:
                print("Graph contains negative weight cycle")
                return None, None

    # Reconstruct paths from predecessor array
    paths = []
    for i in range(V):
        path = []
        current = i
        while current != -1:
            path.insert(0, current + 1)  # Convert to 1-indexed
            current = predecessor[current]
        paths.append(path)

    return "Distance: "+str(distance),"Shortest Paths from Node 1: " +str(paths)



# Given weighted adjacency matrix
adj_matrix = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 2, 3, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 3, 1, 0, 2],
    [0, 0, 0, 2, 0, 0, 0]
]

# Compute shortest paths from the first node (index 0)
source_node = 0
print( bellman_ford_with_path(adj_matrix, source_node))
