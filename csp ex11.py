def is_valid_assignment(region, color, assignment, adjacencies):
    for neighbor in adjacencies.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def backtracking(map, colors, assignment, adjacencies):
    if len(assignment) == len(map):
        return assignment
    region = [r for r in map if r not in assignment][0]
    for color in colors:
        if is_valid_assignment(region, color, assignment, adjacencies):
            assignment[region] = color
            result = backtracking(map, colors, assignment, adjacencies)
            if result:
                return result
            del assignment[region]
    return None
def map_coloring(map, adjacencies, colors):
    assignment = {}
    result = backtracking(map, colors, assignment, adjacencies)
    return result
if __name__ == '__main__':
    regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    adjacent_regions = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"],
        "T": []
    }
    available_colors = ["Red", "Green", "Blue"]
    coloring = map_coloring(regions, adjacent_regions, available_colors)
    if coloring:
        for region, color in coloring.items():
            print(f"{region}: {color}")
    else:
        print("No solution found.")
