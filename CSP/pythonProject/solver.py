# Solves a sudoku board using backtracking
def solve(bo):
    """
    Solves a sudoku board using backtracking
    :param bo: 2d list of ints
    :return: solution
    """
    # Find the next empty cell in the board

    find = find_empty(bo)
    if find:
        row, col = find
    else:
        # If no empty cells are found, the board is solved
        return True

    # Try numbers from 1 to 9 in the current empty cell
    for i in range(1, 10):
        if valid(bo, (row, col), i):
            # If the current number is valid, place it in the cell
            bo[row][col] = i

            # Recursively call solve() to solve the rest of the board
            if solve(bo):
                return True

            # If the current placement does not lead to a solution,
            # backtrack by resetting the cell to 0 and try the next number
            bo[row][col] = 0

    # If no number from 1 to 9 leads to a solution, backtrack further
    return False


# Returns if the attempted move is valid
def valid(bo, pos, num):
    """
    Returns if the attempted move is valid
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """

    # Check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


# Finds an empty space in the board
def find_empty(bo):
    """
    Finds an empty space in the board
    :param bo: partially complete board
    :return: (int, int) row col
    """

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j

    return None










# Prints the board
def print_board(bo):
    """
    Prints the board
    :param bo: 2d List of ints
    :return: None
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")
