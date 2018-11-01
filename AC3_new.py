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
        print("Current queue length of AC3: {}".format(len(queue)))

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
    result={}
    
    # Initialize the queue with all arcs (X,Y) such that 
    # Y is unassigned and Y is a neighbor of X
    queue=[]
    neighbors = v.get_neighbors()
    for neighbor in neighbors:
        if len(neighbor.get_domain()) > 1:
            queue.append(make_constraint(v, neighbor))

    while queue:
        print("Current queue length of AC3: {}".format(len(queue)))
        
        current_constraint=queue.pop(0)
        X_i=current_constraint[0]
        X_j=current_constraint[1]
        if revise(csp,X_i,X_j):
            domain_x_i = X_i.get_domain()
            if len(domain_x_i)==0:
                result=False
                break
            elif len(domain_x_i) == 1:
                result[X_i.get_position()] =  domain_x_i[0]

            for neighbour in X_i.get_neighbors():
                if not (neighbour == X_j):
                    queue.append(make_constraint(neighbour,X_i))

    return result

def backtracking_search(csp):
    assignments = {}
    n = len(csp)
    for i in range(n):
        for j in range(n):
            domain = csp[i][j].get_domain()
            if len(domain) == 1:
                assignments[(i,j)] = domain[0]
    
    # print(assignments)
    # print(len(assignments))

    return backtrack(assignments, csp, True)

def backtrack(assignments, csp, is_first):
    if len(assignments) == 81:
        return assignments
    
    unassigned_var = select_unassigned_var(csp, is_first)
    unassigned_var_domain = unassigned_var.get_domain()
    unassigned_var_position = unassigned_var.get_position()

    for val in unassigned_var_domain:
        # print("{} - trying out value {}".format(unassigned_var_position, val))
        csp_original = deepcopy(csp)
        assignments_original = assignments.copy()

        if is_value_consistent_with_assignments(assignments, val,\
                                                unassigned_var_position):
            assignments[unassigned_var_position] = val
            csp[unassigned_var_position[0]][unassigned_var_position[1]].set_value(val)

            # Add inference here
            inference_result = m_ac3(csp, unassigned_var)
            if inference_result != False:
                assignments.update(inference_result)

                # Recurse on backtrack
                result = backtrack(assignments, csp, False)
                if result != False:
                    return result
        
        # print("{} - {} - backtracking with value {}".format(unassigned_var_position, unassigned_var_domain, val))
        csp = csp_original
        assignments = assignments_original

    return False

def select_unassigned_var(csp, is_first):
    n = len(csp)
    ret_var = None

    # Choose the first variable with the highest number of neighbors
    if is_first:
        max_n_neighbors = -1

        for i in range(n):
            for j in range(n):
                n_neighbors = len(csp[i][j].get_neighbors())
                domain_len = len(csp[i][j].get_domain())
                if domain_len > 1 and n_neighbors > max_n_neighbors:
                    max_n_neighbors = n_neighbors
                    ret_var = csp[i][j]
    else:
        for i in range(n):
            for j in range(n):
                domain = csp[i][j].get_domain()
                if len(domain) > 1 and (i,j):
                    ret_var = csp[i][j]
                    break
    
    return ret_var

def is_value_consistent_with_assignments(assignments, val, pos):
    result = True
    for assignment in assignments.keys():
        # Check row constraints
        if assignment[0] == pos[0] and assignments[assignment] == val:
            result = False
            break
        
        # Check column constraints
        if assignment[1] == pos[1] and assignments[assignment] == val:
            result = False
            break

        # Check box constraints
        assignment_box_x = assignment[0] // 3
        assignment_box_y = assignment[1] // 3
        var_box_x = pos[0] // 3
        var_box_y = pos[1] // 3

        if (assignment_box_x == var_box_x) and \
           (assignment_box_y == var_box_y) and assignments[assignment] == val:
           result = False
           break

    return result

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