import itertools

def calculate_cost(path, distance_matrix):
    total_cost = 0
    for i in range(len(path)):
        total_cost += distance_matrix[path[i]][path[(i + 1) % len(path)]]
    return total_cost

def tsp_brute_force(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    
    min_cost = float('inf')
    best_path = None
    
    # Generate all possible paths (permutations)
    for perm in itertools.permutations(cities):
        cost = calculate_cost(perm, distance_matrix)
        if cost < min_cost:
            min_cost = cost
            best_path = perm
            
    return min_cost, best_path

def main():
    distance_matrix = [
        [float('inf'), 20, 30, 10, 11],
        [15, float('inf'), 16, 4, 2],
        [3, 5, float('inf'), 2, 4],
        [19, 6, 18, float('inf'), 3],
        [16, 4, 7, 16, float('inf')]
    ]
    
    min_cost, best_path = tsp_brute_force(distance_matrix)
    
    print("Minimum Path")
    for i in range(len(best_path)):
        city_from = best_path[i] + 1  # to make it 1-indexed
        city_to = best_path[(i + 1) % len(best_path)] + 1  # to make it 1-indexed
        cost = distance_matrix[best_path[i]][best_path[(i + 1) % len(best_path)]]
        if i == len(best_path) - 1:
            print(f"{city_from} – {city_to} = {cost}")  # Last to first
        else:
            print(f"{city_from} – {city_to} = {cost}")

    print(f"\nMinimum cost: {min_cost}")
    path_taken = ' - '.join(str(city + 1) for city in best_path) + ' - ' + str(best_path[0] + 1)
    print(f"Path Taken: {path_taken}")

if __name__ == "__main__":
    main()
