from graphics import *
from AC3 import AC3

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

def solve_sudoku(input_sudoku):

  # Initialize domains
  domains=[None]*9
  #constraints= [[[1,2,3,4,5,6,7,8,9]]*n]*n
  for x in range(n):
    domains[x]=[None]*9
    for y in range(n):
      domains[x][y]=[1,2,3,4,5,6,7,8,9]
  
  # Initialize list of unsolved cell indices
  unsolved=[]

  for i in range(n):
  #  temp=input().split(",")
    for j in range(n):
  #      temp[j]=int(temp[j])
  #      if temp[j] !=0:
      
      if input_sudoku[i][j]!=None:
  #      print(domains[i][j],i,j)
        domains[i][j]=[input_sudoku[i][j]]
      unsolved.append([i,j])
  #  print(domains[i], "indexed domain out of loop",i)

  solved = AC3(domains, unsolved)

  return solved

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
  
  sudoku=[[None,None,None,2,6,None,7,None,1],
          [6,8,None,None,7,None,None,9,None],
          [1,9,None,None,None,4,5,None,None],
          [8,2,None,1,None,None,None,4,None],
          [None,None,4,6,None,2,9,None,None],
          [None,5,None,None,None,3,None,2,8],
          [None,None,9,3,None,None,None,7,4],
          [None,4,None,None,5,None,None,3,6],
          [None,None,3,None,1,8,2,5,None]]

  solved = solve_sudoku(sudoku)

  print(solved)

  # for x in range(n):
  #   print(sudoku[x])

  # for x in range(n):
  #   print(domains[x])

  # print(" ")
  # for val in unsolved:
  #   print(val)
