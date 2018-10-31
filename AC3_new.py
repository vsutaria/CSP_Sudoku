def revise(csp,X_1,X_2):
  
  revised=False
  
  for x in X_1.get_domain():
    count=0
    for y in X_2.get_domain:
      if x!=y:
        count+=1
    if count == 0:
      X_1.remove_from_domain(x)
      revised =True
        
  return revised
        
def make_constraint(i,j):
    result = (i,j)
    return result

def ac3(csp):
    result=True
    queue=[]
    while queue:
        current_constraint=queue.pop(0)
        X_i=current_constraint[0]
        X_j=current_constraint[1]
        if revise(csp,X_i,X_j):
            if X_i.get_domain_len()==0:
                result=False
                break
            for neighbour in X_i.get_neighbours():
                if not (neighbour == X_j):
                    queue.append(make_constraint(neighbour,X_i))
    return result

def backtracking-search(csp):
    return backtrack([],csp)

def backtrack(assignment,csp):
    if not unassigned:
        return assignment
    var=unassigned.pop(0)
    for i in order_domain_values(var,assignment,csp):
        if i in 
