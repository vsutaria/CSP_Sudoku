def AC3(domains,unsolved): 
  stateStack=[]
  # unsolved.sort(key=len(domains[unsolved[0]][unsolved[1]]),reverse = True) #idk if this works but check changes done to sudoku aswell
  while len(unsolved) != 0:
    current=unsolved.pop(0)

    print_sudoku_debug(domains)
    print("\n\n")

    if len(domains[current[0]][current[1]])==1:
      if not apply_constraints(domains,current):
        revert = stateStack.pop(0)
        domains = revert.domains
        unsolved = revert.unsolved
        unsolved.append(current)
    else:
      possibilities = domains[current[0]][current[1]].copy()
      for x in possibilities:
        domains[current[0]][current[1]] = [x]
        state = State(domains.copy(),unsolved.copy())
        stateStack.append(state)
      unsolved.append(current)

  return domains

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
    
    current_set = set(domains[current[0]][current[1]])

    for n in setx:
      for m in sety:

        # Remove current values from the domains of cells
        # that are in the same box
        s = set(domains[box_y*3+m][box_x*3+n])
        set_diff = s - current_set

        domains[box_y*3+m][box_x*3+n] = list(set_diff)
        if (not domains[box_y*3+m][box_x*3+n]):
          return False

    for i in range(n-1):
      # Remove the current values from the domains of cells
      # that are in the same row
      if not i==y:
        s = set(domains[i][x])
        set_diff = s - current_set
        domains[i][x] = list(set_diff)
        if (not domains[i][x]):
          return False

      # Remove the current values from the domains of cells
      # that are in the same column
      if not i==x:
        s = set(domains[y][i])
        set_diff = s - current_set
        domains[y][i] = list(set_diff)
        if (not domains[y][i]):
          return False
    return True

def print_sudoku_debug(domains):
  for i in range(9):
    for j in range(9):
      if len(domains[i][j]) != 1:
        print("0", end=" ")
      else:
        print(domains[i][j][0], end=" ")
      
      if j == 8:
        print()

class State:
  domains=[]
  unsolved=[]
  def __init__(self,domains, unsolved):
    self.domains = domains
    self.unsolved = unsolved
