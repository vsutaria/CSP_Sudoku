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

def read_input_file(file_name):
    """
    Given a path to a file, return a 2D-array that represents a sudoku puzzle.
    If a cell in the puzzle is empty, the value of that cell in the array will be None.

    The input file is a comma-delimited file. Each line in the file represents a row
    in the puzzle. Empty cells in the puzzle should have None in its position.
    E.g: None,None,None,2,6,None,7,None,1

    Parameters
    ----------
    file_name: path to the input file

    Returns
    -------
    parsed_sudoku: 2D-array that represents the sudoku puzzle
    """
    parsed_sudoku = []

    with open(file_name) as f:
        for line in f:
            line = line.strip().split(",")
            
            row = []
            for val in line:
                if val == "None":
                    row.append(None)
                else:
                    row.append(int(val))

            parsed_sudoku.append(row)
    
    return parsed_sudoku