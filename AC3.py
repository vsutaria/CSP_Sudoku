def AC3(domains,unsolved): 
  unsolved.sort(key=len)
  while not unfinished:
    current=finished.pop(0)
    if len(current[0])==1:
      apply_constraints(domains,current)
    else: #Start pulling arbitrary values and backtrack if doesnt work out.

def apply_constraints(domains,current):
    n=9
    x=current[1]
    y=current[2]

    box_x=x//3
    rel_x=x%3
    box_y=y//3
    rel_y=y%3
    setx = [0,1,2]
    sety = [0,1,2]
    setx.remove(rel_x)
    sety.remove(rel_y)
    
    for n in setx:
      for m in sety:
        domains[box_y*3+m][box_x*3+n].remove(current[0])
    for i in range(n-1):
      if not i==y:
        domains[i][x].remove(current[0]) 
      if not i==x:
        domains[y][i].remove(current[0])
