import sys

def dijkstra(graph, start_node):
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start_node] = 0

    for _ in range(n):
        min_distance = sys.maxsize
        min_index = -1

        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                min_index = i

        visited[min_index] = True

        for j in range(n):
            if graph[min_index][j] != float('inf') and not visited[j]:
                new_dist = distance[min_index] + graph[min_index][j]
                if new_dist < distance[j]:
                    distance[j] = new_dist

    return distance

def print_distances(distance, cities):
    print("Source\tDestination\tCost")
    for i in range(len(cities)):
        if distance[i] == sys.maxsize:
            print(f"{cities[0]}\t{cities[i]}\t\t∞")
        else:
            print(f"{cities[0]}\t{cities[i]}\t\t{distance[i]}")

# Define the cities and graph as an adjacency matrix
cities = ['A', 'B', 'C', 'D', 'E']
graph = [
    [0, 20, 30, float('inf'), float('inf')],
    [float('inf'), 0, float('inf'), 15, 25],
    [float('inf'), float('inf'), 0, float('inf'), 25],
    [float('inf'), float('inf'), float('inf'), 0, 10],
    [float('inf'), float('inf'), float('inf'), float('inf'), 0]
]

# Set the starting city
start_city = 'A'
start_node = cities.index(start_city)

# Run Dijkstra's algorithm and print the distances
distances = dijkstra(graph, start_node)
print_distances(distances, cities)
