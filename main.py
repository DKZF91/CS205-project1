import Manhattan_Distance_heuristic
import Misplaced_Tile_heuristic
import Uniform_Cost_Search

initial_state = [
    [1, 3, 6],
    [5, 0, 2],
    [4, 7, 8]
]


if __name__ == "__main__":
    # Select the model you need
    model = int(input(
        "Please choose your model "
        "(1 for Manhattan_Distance_heuristic, "
        "2 for Misplaced_Tile_heuristic, "
        "3 for Uniform_Cost_Search (default is 3))：") or 3)

    # Select the size of the puzzle
    puzzle_size = int(input("Please enter the size of the puzzle (default is 3)")or 3)

    input_initial_state = []
    final_state = []

    # generate the final(goal) state
    nums = list(range(1, puzzle_size * puzzle_size)) + [0]
    for i in range(puzzle_size):
        row = nums[i * puzzle_size : (i + 1) * puzzle_size]
        final_state.append(row)

    goal_positions = {}
    for i in range(puzzle_size):
        for j in range(puzzle_size):
            val = final_state[i][j]
            goal_positions[val] = (i, j)

    # User input initial state
    print(f"Please enter each row of the matrix by row, "
          f"a total of {puzzle_size} rows, "
          f"each row has {puzzle_size} numbers (separated by spaces)")

    for i in range(puzzle_size):
        row = list(map(int, input(f"Line {i+1}:").split()))
        if not row:
            custom_matrix = initial_state
            break
        input_initial_state.append(row)

    # Use the default initial state
    if input_initial_state:
        initial_state = input_initial_state[:]

    if model == 1:
        Manhattan_Distance_heuristic.set_parameter(initial_state, final_state, puzzle_size, goal_positions)
        result = Manhattan_Distance_heuristic.general_search(Manhattan_Distance_heuristic.queueing)
        if result != "failure":
            Manhattan_Distance_heuristic.print_solution(result)
        else:
            print("No solution found.")
    elif model == 2:
        Misplaced_Tile_heuristic.set_parameter(initial_state, final_state, puzzle_size, goal_positions)
        result = Misplaced_Tile_heuristic.general_search(Misplaced_Tile_heuristic.queueing)
        if result != "failure":
            Misplaced_Tile_heuristic.print_solution(result)
        else:
            print("No solution found.")
    elif model == 3:
        Uniform_Cost_Search.set_parameter(initial_state, final_state, puzzle_size, goal_positions)
        result = Uniform_Cost_Search.general_search(Uniform_Cost_Search.queueing)
        if result != "failure":
            Uniform_Cost_Search.print_solution(result)
        else:
            print("No solution found.")
    else:
        print("Wrong model selection! Exit program.")


