n= 9
inside_n=3
sudoku=[]

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
      if ((i= x)or(j=y)) and sudoku[i,j] ==value:
        result=False        
      elif (i>=(inside_i-3) and i<(inside_i)) and (j>=(inside_j-3)and j<(inside_y)):
        if sudoku[i,j]==value:
          result=False
      else:
        continue
      j++
    i++
  return result


print("enter the number for the (9 3X3) like so 2,1,3,4,5,4,0,4,9:")
for i in range(n):
  temp=input().split(",")
  for j in range(n):
      temp[j]=int(temp[j])

  sudoku.append(temp)
print(sudoku) 

