from graphics import *
from utilities import read_input_file, set_neighbors, is_solved, create_2d_list_from_sudoku, is_solution_valid,\
                      print_sudoku
from AC3_new import ac3, backtracking_search
from sys import setrecursionlimit
import time

n = 9
inside_n=3

def display_solution(solved_sudoku):
  win = GraphWin('Face', 361, 361) # give title and dimensions


  for i in range(9):
  #     x=x+i+40
  #     y=0    
      x = i * 40 + 20
      for j in range(9):
  #         y=y+j+40
          y = j * 40 + 20
          num=Text(Point(x,y),solved_sudoku[i][j])
          test=Rectangle(Point(x-20,y-20),Point(x+20,y+20))
          test.draw(win)
          num.draw(win)

  win.getMouse()
  win.close()

# def solve_sudoku(input_sudoku):

#   # Initialize domains
#   domains=[None]*9
#   #constraints= [[[1,2,3,4,5,6,7,8,9]]*n]*n
#   for x in range(n):
#     domains[x]=[None]*9
#     for y in range(n):
#       domains[x][y]=[1,2,3,4,5,6,7,8,9]
  
#   # Initialize list of unsolved cell indices
#   unsolved=[]

#   for i in range(n):
#   #  temp=input().split(",")
#     for j in range(n):
#   #      temp[j]=int(temp[j])
#   #      if temp[j] !=0:
      
#       if input_sudoku[i][j]!=None:
#   #      print(domains[i][j],i,j)
#         domains[i][j]=[input_sudoku[i][j]]
#       unsolved.append([i,j])
#   #  print(domains[i], "indexed domain out of loop",i)

#   solved = AC3(domains, unsolved)

#   return solved

if __name__ == "__main__":

  sudoku = read_input_file("input_hard.txt")
  set_neighbors(sudoku)
  
  ac3_result = ac3(sudoku)
  print("First AC3 result: {}".format(ac3_result))

  # print_sudoku(sudoku)

  backtrack_result = True
  if ac3_result == True :
    if not is_solved(sudoku):
      backtrack_result = backtracking_search(sudoku)

      if backtrack_result != False:
        solution = []
        for i in range(9):
          solution.append([])
          for j in range(9):
            solution[i].append(backtrack_result[(i,j)])
            print(backtrack_result[(i,j)], end=" ")
          print()

        print("Is solution valid? {}".format(is_solution_valid(solution)))
        # print_sudoku(sudoku)
      else:
        print("Something went wrong")
    else:
      sudoku_2d = create_2d_list_from_sudoku(sudoku)
      print(sudoku_2d)
      print("Is the solution valid? {}".format(is_solution_valid(sudoku_2d)))

  # if ac3_result == True and backtrack_result == True:
  #   sudoku_2d = create_2d_list_from_sudoku(sudoku)

  #   print("Is the solution valid? {}".format(is_solution_valid(sudoku_2d)))
  #   print(sudoku_2d)
  # else:
  #   print("Something went wrong")

  # solved = solve_sudoku(sudoku)

  # print(solved)

