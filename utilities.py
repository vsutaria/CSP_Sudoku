from cell import Cell

def create_2d_list_from_sudoku(sudoku):
    n = len(sudoku)
    sudoku_2d = []

    for i in range(n):
        sudoku_2d.append([])
        for j in range(n):
            sudoku_2d[i].append(sudoku[i][j].get_domain()[0])

    return sudoku_2d

def create_sudoku_from_2d_list(sudoku_2d):
    default_domain = [1,2,3,4,5,6,7,8,9]
    n = len(sudoku_2d)
    sudoku = []

    for i in range(n):
        sudoku.append([])
        for j in range(n):
            if sudoku_2d[i][j] is None:
                c = Cell(i, j, default_domain.copy())
            else:
                c = Cell(i, j, [sudoku_2d[i][j]])
            
            sudoku[i].append(c)

    return sudoku

def is_solved(solution):
    n = len(solution)
    solved = True

    for i in range(n):
        for j in range(n):
            if len(solution[i][j].get_domain()) != 1:
                solved = False
                break
    
    return solved

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
        line_no = 0
        default_domain = [1,2,3,4,5,6,7,8,9]

        for line in f:
            line = line.strip().split(",")
            
            row = []
            for i in range(len(line)):
                if line[i] == "None":
                    c = Cell(line_no, i, default_domain.copy())
                    row.append(c)
                else:
                    c = Cell(line_no, i, [int(line[i])])
                    row.append(c)

            parsed_sudoku.append(row)
            line_no += 1
    
    return parsed_sudoku

def set_neighbors(sudoku_grid):
    """
    Set the neighbors for the cells in the sudoku grid

    Parameters
    ----------
    sudoku_grid: 2D-array of Cell objects representing a sudoku puzzle

    Returns
    -------
    Add the neighbors of each cell to the Cell objects in the 2D-array
    """
    
    grid_size = 9

    for x in range(grid_size):
        for y in range(grid_size):

            # Add neighbors in the same box

            box_x=x//3
            box_y=y//3
            setx = [0,1,2]
            sety = [0,1,2]

            for n in setx:
                for m in sety:
                    if (box_y*3 + m) != y or (box_x*3 + n) != x:
                        sudoku_grid[x][y].add_neighbor(sudoku_grid[box_x*3+n][box_y*3+m])

            for i in range(grid_size):
                # Add neighbors on the same row
                if i != y:
                    sudoku_grid[x][y].add_neighbor(sudoku_grid[x][i])

                # Add neighbors in the same column
                if i != x:
                    sudoku_grid[x][y].add_neighbor(sudoku_grid[i][y])

def print_sudoku(sudoku):
    n = len(sudoku)
    for i in range(n):
        for j in range(n):
            print(sudoku[i][j].get_domain(), end=" ")

        print()