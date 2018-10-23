def is_solution_valid(solution):
    """
    Check if a sudoku solution is valid

    Parameters
    ----------
    solution - a 2D-array of size 9 x 9 representing a sudoku solution

    Returns
    -------
    True if the solution is valid, False otherwise
    """

    # Check if rows and columns have unique values
    for i in range(len(solution)):
        row_found = [False, False, False, False, False, False, False, False, False]
        col_found = [False, False, False, False, False, False, False, False, False]

        for j in range(len(solution[i])):

            # There's an unsolved cell
            if solution[i][j] is None:
                return False

            row_index = solution[i][j] - 1
            if row_found[row_index] == False:
                row_found[row_index] = True
            else:
                return False # Found duplicate value
            
            # There's an unsolved cell
            if solution[j][i] is None:
                return False

            col_index = solution[j][i] - 1
            if col_found[col_index] == False:
                col_found[col_index] = True
            else:
                return False # Found duplicate value

    # Check if each 3x3 box has unique values
    for i in range(1, len(solution), 3):
        for j in range(1, len(solution[i]), 3):
            found = [False, False, False, False, False, False, False, False, False]

            if found[solution[i][j] - 1] == False:
                found[solution[i][j] - 1] = True
            else:
                return False

            if found[solution[i][j-1] - 1] == False:
                found[solution[i][j-1] - 1] = True
            else:
                return False

            if found[solution[i][j+1] - 1] == False:
                found[solution[i][j+1] - 1] = True
            else:
                return False

            if found[solution[i-1][j] - 1] == False:
                found[solution[i-1][j] - 1] = True
            else:
                return False

            if found[solution[i+1][j] - 1] == False:
                found[solution[i+1][j] - 1] = True
            else:
                return False

            if found[solution[i-1][j-1] - 1] == False:
                found[solution[i-1][j-1] - 1] = True
            else:
                return False

            if found[solution[i-1][j+1] - 1] == False:
                found[solution[i-1][j+1] - 1] = True
            else:
                return False

            if found[solution[i+1][j-1] - 1] == False:
                found[solution[i+1][j-1] - 1] = True
            else:
                return False

            if found[solution[i+1][j+1] - 1] == False:
                found[solution[i+1][j+1] - 1] = True
            else:
                return False

    return True