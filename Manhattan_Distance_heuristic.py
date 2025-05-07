import heapq
import copy


class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state  # Current status
        self.parent = parent
        self.g = cost # g(n)
        self.h = self.manhattan_distance() # h(n)
        self.f = self.g + self.h # f(n)

    def __lt__(self, other):
        return self.f < other.f

    # Calculate the total Manhattan distance
    def manhattan_distance(self):
        total = 0
        for i in range(puzzle_size):
            for j in range(puzzle_size):
                val = self.state[i][j]
                if val != 0:
                    goal_i, goal_j = goal_positions[val]
                    total += abs(i - goal_i) + abs(j - goal_j)
        return total

# find the blank(0) position
def find_blank(state):
    for i in range(puzzle_size):
        for j in range(puzzle_size):
            if state[i][j] == 0:
                return i, j

# Search for the next possible child nodes of the current node
def expand(node, operators):
    children = []
    x, y = find_blank(node.state)
    for move in operators:
        nx, ny = x + move[0], y + move[1]
        if 0 <= nx < puzzle_size and 0 <= ny < puzzle_size:
            new_state = copy.deepcopy(node.state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            child_node = Node(new_state, node, node.g + 1)
            children.append(child_node)
    return children

# Put all the child nodes obtained in the previous step into the heap, and the heap will be automatically sorted
def queueing_function(queue, successors):
    for s in successors:
        heapq.heappush(queue, s)
    return queue

# Main Function Following General-Search Pseudocode
def general_search(queueing_function):
    nodes = [Node(initial_state)]
    heapq.heapify(nodes)
    while True:
        if not nodes:
            return "failure"
        node = heapq.heappop(nodes)
        if node.state == final_state:
            return node
        nodes = queueing_function(nodes, expand(node, operators))

def set_parameter(initial, final, size, goal):
    global initial_state, final_state, puzzle_size, operators, goal_positions
    initial_state = initial
    final_state = final
    puzzle_size = size
    goal_positions = goal
    operators = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right


# Print Solution Path
def print_solution(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    path.reverse()
    for step in path:
        for row in step.state:
            print(row)
        print(f"g(n) = {step.g}, h(n) = {step.h}, f(n) = {step.f}")
        print("----")

