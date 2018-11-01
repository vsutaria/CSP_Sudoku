from utilities import is_solved
from copy import deepcopy

def revise(csp,X_1,X_2):
  
  revised=False
  
  for x in X_1.get_domain():
    count=0
    for y in X_2.get_domain():
      if x!=y:
        count+=1
    if count == 0:
      X_1.remove_from_domain(x)
      revised =True
        
  return revised
        
def make_constraint(i,j):
    result = (i,j)
    return result

def initialize_constraints(csp):
    queue = []

    n = len(csp)
    for i in range(n):
        for j in range(n):
            queue = queue + csp[i][j].generate_constraints()

    return queue

def ac3(csp):
    result=True
    queue=initialize_constraints(csp)

    while queue:
        current_constraint=queue.pop(0)
        X_i=current_constraint[0]
        X_j=current_constraint[1]
        if revise(csp,X_i,X_j):
            if len(X_i.get_domain())==0:
                result=False
                break
            for neighbour in X_i.get_neighbors():
                if not (neighbour == X_j):
                    queue.append(make_constraint(neighbour,X_i))
    return result

def m_ac3(csp, v):
    """
    Maintain arc consistency using AC3 algorithm.
    This AC3 will start with all arcs (X, Y) such that
    Y is unassigned and Y is a neighbor of X
    Parameters
    ----------
    csp: The current CSP
    v: X in the (X, Y) pair
    Returns
    -------
    True if the CSP is consistent, False otherwise
    """

    result=True
    queue=[]

    neighbors = v.get_neighbors()
    for neighbor in neighbors:
        if len(neighbor.get_domain()) > 1:
            queue.append(make_constraint(v, neighbor))

    while queue:
        current_constraint=queue.pop(0)
        X_i=current_constraint[0]
        X_j=current_constraint[1]
        if revise(csp,X_i,X_j):
            if len(X_i.get_domain())==0:
                result=False
                break
            for neighbour in X_i.get_neighbors():
                if not (neighbour == X_j):
                    queue.append(make_constraint(neighbour,X_i))
    return result

def backtracking_search(csp):
     return backtrack([],csp)

def backtrack(assignment, csp):
    if len(assignment)==81:
        return csp
    #if is_solved(csp):
    #    return csp
    
    v = select_unassigned_variable(csp)
    v_position = v.get_position()
    v_domain = v.get_domain()

    for val in v_domain:
        csp_original = csp.copy()

        if is_valid_assignment(val, v_position[0], v_position[1], csp):
            csp[v_position[0]][v_position[1]].set_value(val)
            assignment.append([v_position[0], v_position[1],val])
           
            inference_result = m_ac3(csp, v)
            if inference_result != False:

                backtrack_result = backtrack(assignment,csp)
                if backtrack_result != False:
                    return backtrack_result

        csp = csp_original
        assignment.remove([v_position[0], v_position[1],val])

    return False

def select_unassigned_variable(csp):
    """
    Select next variable using the minium remaining values (MRV) heurisic
    """
    n = len(csp)
    v = csp[0][0]
    v_domain_len = len(v.get_domain())

    for i in range(n):
        for j in range(n):
            if len(csp[i][j].get_domain()) < v_domain_len:
                v = csp[i][j]
                v_domain_len = len(v.get_domain())

    return v

def is_valid_assignment(val, x, y, csp):
    """
    Check if an assignment for a variable violates any of its constraints
    Return True if no constraint is violated, False otherwise
    """
    grid_size = len(csp)

    # Check if value is valid in its box

    box_x=x//3
    box_y=y//3
    setx = [0,1,2]
    sety = [0,1,2]

    for n in setx:
        for m in sety:
            if (box_y*3 + m) != y or (box_x*3 + n) != x:
                domain = csp[box_x*3+n][box_y*3+m].get_domain()
                if len(domain) == 1 and domain[0] == val:
                    return False
                    

    for i in range(grid_size):
        # Check if value is valid in its row
        if i != y:
            domain = csp[x][i].get_domain()
            if len(domain) == 0 and domain[0] == val:
                return False

        # Check if value is valid in its column
        if i != x:
            domain = csp[i][y].get_domain()
            if len(domain) == 0 and domain[0] == val:
                return False

    return True
  def num_freq(X):
    x_dom=X.get_domain()
    x_neb= X.get_neighbors()

    temp_doms=[]
    for neb in x_neb:
        temp_doms=temp_doms+neb.get_domain()


    count={x: temp_doms.count(x) for x in x_dom}
    temp_dom, c = count.keys(), count.values()
    #print(temp_dom)
    sorted_x=sorted(count.items(),key=operator.itemgetter(1))
    result=[]
    for i in sorted_x:
        result.append(i[0])
    return result
