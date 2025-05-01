import numpy as np

def is_safe_8queens_short(placement, col):
    row = placement[col]
    return not np.any((placement[:col] == row) | (np.abs(placement[:col] - row) == np.abs(np.arange(col) - col)))

def solve_8queens_util_short(col, placement, solutions):
    n = 8
    if col == n:
        solutions.append(list(placement))
        return
    for row in range(n):
        placement[col] = row
        if is_safe_8queens_short(placement, col):
            solve_8queens_util_short(col + 1, placement, solutions)

def solve_8queens_numpy_short():
    solutions = []
    placement = np.zeros(8, dtype=int)
    solve_8queens_util_short(0, placement, solutions)
    return [np.array(sol) for sol in solutions]

def print_board(solution):
    n = len(solution)
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("-" * (2 * n - 1))

# Solve for the 8 Queens problem
solutions_8queens_short = solve_8queens_numpy_short()
print(f"Number of solutions for 8 Queens (Short NumPy): {len(solutions_8queens_short)}")

# Print all the solutions in the board format
if solutions_8queens_short:
    print("first solution")
    print_board(solutions_8queens_short[0])
