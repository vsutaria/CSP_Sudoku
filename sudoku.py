n= 9
inside_n=3
sudoku=[[None,None,None,2,6,None,7,None,1],
 [6,8,None,None,7,None,None,9,None],
 [1,9,None,None,None,4,5,None,None],
 [8,2,None,1,None,None,None,4,None],
 [None,None,4,6,None,2,9,None,None],
 [None,5,None,None,None,3,None,2,8],
 [None,None,9,3,None,None,None,7,4],
 [None,4,None,None,5,None,None,3,6],
 [None,None,3,None,1,8,2,5,None]]

domains=[None]*9
#constraints= [[[1,2,3,4,5,6,7,8,9]]*n]*n
for x in range(n):
  domains[x]=[None]*9
  for y in range(n):
    domains[x][y]=[1,2,3,4,5,6,7,8,9]

for x in range(n):
  print(sudoku[x])


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
      if ((i== x)or(j==y)) and sudoku[i,j] ==value:
        result=False        
      elif (i>=(inside_i-3) and i<(inside_i)) and (j>=(inside_j-3)and j<(inside_j)):
        if sudoku[i,j]==value:
          result=False
      else:
        continue
      j+=1
    i+=1
  return result

unsolved=[]

for i in range(n):
#  temp=input().split(",")
  for j in range(n):
#      temp[j]=int(temp[j])
#      if temp[j] !=0:
    
    if sudoku[i][j]!=None:
#      print(domains[i][j],i,j)
      domains[i][j]=[sudoku[i][j]]
    unsolved.append([i,j])
#  print(domains[i], "indexed domain out of loop",i)
   

for x in range(n):
  print(domains[x])

print(" ")
for val in unsolved:
  print(val)
