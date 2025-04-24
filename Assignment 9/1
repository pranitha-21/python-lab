import random
def is_safe(board,row,col):
    for i in range(row):
        if board[i]==col or board[i]-i==col-row or board[i]+i==col+row:
            return False
    return True
def solve_8_queen(n,board,row,solutions):
    if row==n:
        solutions.append(board[:])
        return
    cols=list(range(n))
    random.shuffle(cols)
    for col in cols:
        if is_safe(board,row,col):
            board[row]=col
            solve_8_queen(n,board,row+1,solutions)
def generate_random_solutions(n=8):
    solutions=[]
    board=[-1]*n
    solve_8_queen(n,board,0,solutions)
    return random.choice(solutions) if solutions else None
def print_board(solution):
    if solution:
        for row in solution:
            line=['.']*8
            line[row]='Q'
            print(''.join(line))
    else:
        print("no solution found")

if __name__=="__main__":
    solution=generate_random_solutions()
    print_board(solution)
