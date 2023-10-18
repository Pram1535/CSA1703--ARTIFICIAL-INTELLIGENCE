import itertools
def distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2) ** 0.5
def total_distance(path, cities):
    dist = 0
    for i in range(len(path) - 1):
        dist += distance(cities[path[i]], cities[path[i + 1]])
    dist += distance(cities[path[-1]], cities[path[0]])
    return dist
def tsp_bruteforce(cities):
    num_cities = len(cities)
    if num_cities <= 2:
        return list(range(num_cities)), total_distance(range(num_cities), cities)
    shortest_path = None
    shortest_distance = float('inf')
    for path in itertools.permutations(range(num_cities)):
        dist = total_distance(path, cities)
        if dist < shortest_distance:
            shortest_distance = dist
            shortest_path = path
    return shortest_path, shortest_distance
if __name__ == '__main__':
    cities = [(0, 0), (1, 2), (2, 2), (4, 4), (3, 1)]
    best_path, best_distance = tsp_bruteforce(cities)
    print("Shortest Path:", best_path)
    print("Shortest Distance:", best_distance)
