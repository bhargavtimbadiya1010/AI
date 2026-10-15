# Goal state; 0 represents the blank space
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Possible positions of the blank for each position
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


# Depth First Search function
def dfs(start, max_depth=12):
    stack = [(start, [])]
    visited = set([start])

    while stack:
        state, path = stack.pop()

        # Check whether the goal state is reached
        if state == goal:
            return path + [state]

        # Stop searching if maximum depth is reached
        if len(path) >= max_depth:
            continue

        # Find the position of the blank space
        zero = state.index(0)

        for move in moves[zero]:
            new_state = list(state)

            # Swap the blank space with the adjacent tile
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                stack.append((new_state, path + [state]))

    return None


# Initial state
start = (1, 2, 3,
         0, 4, 6,
         7, 5, 8)

# Find the solution
solution = dfs(start)

if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")

    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print()
else:
    print("No solution found")
