def is_valid_state(state):
    left_missionaries, left_cannibals, boat, right_missionaries, right_cannibals = state
    if left_missionaries < 0 or left_cannibals < 0 or right_missionaries < 0 or right_cannibals < 0:
        return False
    if (left_missionaries > 0 and left_missionaries < left_cannibals) or \
       (right_missionaries > 0 and right_missionaries < right_cannibals):
        return False
    return True
def is_goal_state(state, initial_state):
    return state == (0, 0, 0, initial_state[0], initial_state[1])
def generate_next_states(current_state):
    next_states = []
    left_missionaries, left_cannibals, boat, right_missionaries, right_cannibals = current_state
    if boat == 1:  
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (left_missionaries - m, left_cannibals - c, 1 - boat, right_missionaries + m, right_cannibals + c)
                    if is_valid_state(new_state):
                        next_states.append(new_state)
    else:  
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (left_missionaries + m, left_cannibals + c, 1 - boat, right_missionaries - m, right_cannibals - c)
                    if is_valid_state(new_state):
                        next_states.append(new_state)
    return next_states
def dfs_search(initial_state):
    visited = set()
    stack = [(initial_state, [])]
    while stack:
        current_state, path = stack.pop()
        visited.add(current_state)
        if is_goal_state(current_state, initial_state):
            return path + [current_state]
        for next_state in generate_next_states(current_state):
            if next_state not in visited:
                stack.append((next_state, path + [current_state]))
    return None
def print_solution(solution):
    for state in solution:
        left_missionaries, left_cannibals, boat, right_missionaries, right_cannibals = state
        print(f"Left side: {left_missionaries}M-{left_cannibals}C, Boat: {'←' if boat == 0 else '→'}, Right side: {right_missionaries}M-{right_cannibals}C")
initial_state = (3, 3, 1, 0, 0)
solution = dfs_search(initial_state)
if solution:
    print_solution(solution)
else:
    print("No solution found.")
