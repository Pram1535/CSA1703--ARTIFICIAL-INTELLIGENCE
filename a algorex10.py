import heapq
class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic
    def total_cost(self):
        return self.cost + self.heuristic
def astar_search(initial_state, goal_state, successors, heuristic):
    open_list = []
    closed_set = set()
    initial_node = Node(initial_state, None, None, 0, heuristic(initial_state, goal_state))
    heapq.heappush(open_list, (initial_node.total_cost(), id(initial_node), initial_node))
    while open_list:
        _, _, current_node = heapq.heappop(open_list)
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.insert(0, current_node.action)
                current_node = current_node.parent
            return path
        if current_node.state in closed_set:
            continue
        closed_set.add(current_node.state)
        for action, next_state, step_cost in successors(current_node.state):
            if next_state in closed_set:
                continue
            new_cost = current_node.cost + step_cost
            new_node = Node(next_state, current_node, action, new_cost, heuristic(next_state, goal_state))
            heapq.heappush(open_list, (new_node.total_cost(), id(new_node), new_node))
    return None
def simple_heuristic(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])
def grid_successors(state):
    x, y = state
    successors = []
    for dx, dy, action in [(1, 0, 'right'), (-1, 0, 'left'), (0, 1, 'down'), (0, -1, 'up')]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 5 and 0 <= new_y < 5:
            successors.append((action, (new_x, new_y), 1))
    return successors
initial_state = (0, 0)
goal_state = (4, 4)
path = astar_search(initial_state, goal_state, grid_successors, simple_heuristic)
if path:
    print("Shortest Path:", path)
else:
    print("No path found")
