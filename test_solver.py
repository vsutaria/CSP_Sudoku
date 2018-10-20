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

def test_is_solution_valid():
    input_solution1 = [[4,3,5,2,6,9,7,8,1],
                      [6,8,2,5,7,1,4,9,3],
                      [1,9,7,8,3,4,5,6,2],
                      [8,2,6,1,9,5,3,4,7],
                      [3,7,4,6,8,2,9,1,5],
                      [9,5,1,7,4,3,6,2,8],
                      [5,1,9,3,2,6,8,7,4],
                      [2,4,8,9,5,7,1,3,6],
                      [7,6,3,4,1,8,2,5,9]]
    output1 = is_solution_valid(input_solution1)
    expected1 = True

    assert output1 == expected1

    input_solution2 = [[5,5,5,5,5,5,5,5,5],
                      [6,8,2,5,7,1,4,9,3],
                      [1,9,7,8,3,4,5,6,2],
                      [8,2,6,1,9,5,3,4,7],
                      [3,7,4,6,8,2,9,1,5],
                      [9,5,1,7,4,3,6,2,8],
                      [5,1,9,3,2,6,8,7,4],
                      [2,4,8,9,5,7,1,3,6],
                      [7,6,3,4,1,8,2,5,9]]
    output2 = is_solution_valid(input_solution2)
    expected2 = False

    assert output2 == expected2

    input_solution3 = [[5,3,5,2,6,9,7,8,1],
                      [5,8,2,5,7,1,4,9,3],
                      [5,9,7,8,3,4,5,6,2],
                      [5,2,6,1,9,5,3,4,7],
                      [5,7,4,6,8,2,9,1,5],
                      [5,5,1,7,4,3,6,2,8],
                      [5,1,9,3,2,6,8,7,4],
                      [5,4,8,9,5,7,1,3,6],
                      [5,6,3,4,1,8,2,5,9]]
    output3= is_solution_valid(input_solution3)
    expected3 = False

    assert output3 == expected3

def test_sudoku_solver():
    input_sudoku1 = [[None,None,None,2,6,None,7,None,1],
                     [6,8,None,None,7,None,None,9,None],
                     [1,9,None,None,None,4,5,None,None],
                     [8,2,None,1,None,None,None,4,None],
                     [None,None,4,6,None,2,9,None,None],
                     [None,5,None,None,None,3,None,2,8],
                     [None,None,9,3,None,None,None,7,4],
                     [None,4,None,None,5,None,None,3,6],
                     [None,None,3,None,1,8,2,5,None]]
    output1 = None # Solve the sudoku here
    expected1 = [[4,3,5,2,6,9,7,8,1],
                 [6,8,2,5,7,1,4,9,3],
                 [1,9,7,8,3,4,5,6,2],
                 [8,2,6,1,9,5,3,4,7],
                 [3,7,4,6,8,2,9,1,5],
                 [9,5,1,7,4,3,6,2,8],
                 [5,1,9,3,2,6,8,7,4],
                 [2,4,8,9,5,7,1,3,6],
                 [7,6,3,4,1,8,2,5,9]]

    assert output1 == expected1

    input_sudoku2 = [[None,2,None,None,None,None,None,None,None],
                     [None,None,None,6,None,None,None,None,3],
                     [None,7,4,None,8,None,None,None,None],
                     [None,None,None,None,None,3,None,None,2],
                     [None,8,None,None,4,None,None,1,None],
                     [6,None,None,5,None,None,None,None,None],
                     [None,None,None,None,1,None,7,8,None],
                     [5,None,None,None,None,9,None,None,None],
                     [None,None,None,None,None,None,None,4,None]]
    output2 = None # Solve the sudoku here
    expected2 = [[1,2,6,4,3,7,9,5,8],
                 [8,9,5,6,2,1,4,7,3],
                 [3,7,4,9,8,5,1,2,6],
                 [4,5,7,1,9,3,8,6,2],
                 [9,8,3,2,4,6,5,1,7],
                 [6,1,2,5,7,8,3,9,4],
                 [2,6,9,3,1,4,7,8,5],
                 [5,4,8,7,6,9,2,3,1],
                 [7,3,1,8,5,2,6,4,9]]

    assert output2 == expected2