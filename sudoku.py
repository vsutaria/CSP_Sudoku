#from graphics import *
from utilities import read_input_file, set_neighbors, is_solved, create_2d_list_from_sudoku, is_solution_valid
from AC3_new import ac3, backtracking_search
from sys import setrecursionlimit

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

def check_num_placement(x,y,value):
  result= True
  i=0

  inside_i =0
  inside_j =0
  if x>3:
    inside_i=3
  elif x<5:
    inside_i=9
  else:
    inside_i=6
  
  if y>3:
    inside_j=3
  elif y<5:
    inside_j=9
  else:
    inside_j=6
  while (i < n) or (result == True):
    j=0
    while (j < n) or (result == True):
      if ((i== x)or(j==y)) and sudoku[i][j] ==value:
        result=False        
      elif (i>=(inside_i-3) and i<(inside_i)) and (j>=(inside_j-3)and j<(inside_j)):
        if sudoku[i][j]==value:
          result=False
      else:
        continue
      j+=1
    i+=1
  return result

if __name__ == "__main__":

  sudoku = read_input_file("input.txt")
  set_neighbors(sudoku)
  
  ac3_result = ac3(sudoku)
  print("First AC3 result: {}".format(ac3_result))

  backtrack_result = True
  if ac3_result == True and not is_solved(sudoku):
    backtrack_result = backtracking_search(sudoku)
#    print("Backtrack result: {}".format(backtrack_result))
    print("Backtrack result:")
    for i in backtrack_result:
        for j in i:
            print(j.get_domain())

  if ac3_result == True and backtrack_result == True:
    sudoku_2d = create_2d_list_from_sudoku(sudoku)

    print("Is the solution valid? {}".format(is_solution_valid(sudoku_2d)))
    print(sudoku_2d)
  else:
    print("Something went wrong")

  # solved = solve_sudoku(sudoku)

  # print(solved)

  # for x in range(n):
  #   print(sudoku[x])

  # for x in range(n):
  #   print(domains[x])

  # print(" ")
  # for val in unsolved:
  #   print(val)
