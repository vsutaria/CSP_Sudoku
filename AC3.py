def AC3(domains,unsolved): 
  unsolved.sort(key=len(domains[unsolved[0]][unsolved[1]]),reverse = True) #idk if this works but check changes done to sudoku aswell
  while not unfinished:
    current=finished.pop(0)
    if len(domains[current[0]][current[1]])==1:
      if not apply_constraints(domains,current):
        revert = stateStack.pop(0)
        domains = revert.domains
        unsolved = revert.unsolved
        unfinished.append(current)
    else:
      possibilities = domains[current[0]][current[1]].copy
      for x in possibilities:
        domains[current[0]][current[1]] = [x]
        state = State(domains.copy,unsolved.copy)
        stateStack.append(state)
      unfinished.append(current)



def apply_constraints(domains,current):
    n=9
    x=current[0]
    y=current[1]

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
        domains[box_y*3+m][box_x*3+n].remove(domains[current[0]][current[1]])
        if (not domains[box_y*3+m][box_x*3+n]):
          return false

    for i in range(n-1):
      if not i==y:
        domains[i][x].remove(domains[current[0]][current[1]]) 
        if (not domains[i][x]):
          return false
      if not i==x:
        domains[y][i].remove(domains[current[0]][current[1]])
        if (not domains[y][i]):
          return false
    return true

class State:
  def __init__(domains, unsolved):
    self.domains = domains
    self.unsolved = unsolved