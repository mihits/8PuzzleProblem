import heapq

class node:  
      
    def __init__(self, parent, mat, level, cost):  
                      
        #Store parent of given node
        self.parent = parent  
  
        # Useful for Storing the matrix  
        self.mat = mat 
  
        # Store cost function of node
        self.cost= cost  

        # Store number of moves to reach given node
        self.level = level
    
    #comparison function based on which priority queue is maintained i.e minimum cost 
    def __lt__ (self,next):
        return self.cost < next.cost
    

def copy(mat):
    """ Copy function to create a similar matrix of the given node"""
    temp = []
    for i in mat:
        t = []
        for j in i:
            t.append(j)
        temp.append(t)
    return temp 

def find(mat,val):
    """ Obtain position of given value in matrix"""
    for i in range(0,3):
        for j in range(0,3):
            if(mat[i][j] ==  val):
                return [i,j]
    

def successors(root,goal):
    """ Inputs : root - current node
                 goal - final node
        Returns: list of valid children nodes of current nodes   """

    temp_mat = copy(root.mat)    #stores copy of matrix of current node  

    old_pos = find(temp_mat,0)   #find position of empty tile
    change_in_pos = [[0,1],[1,0],[-1,0],[0,-1]]

    children = []   #list of child nodes 

    for i in change_in_pos:
        new_pos = [sum(x) for x in zip(old_pos,i)]  #store possible new positions of empty tile
        if(isValid(new_pos)):   
            temp_mat[old_pos[0]][old_pos[1]] , temp_mat[new_pos[0]][new_pos[1]] = temp_mat[new_pos[0]][new_pos[1]],temp_mat[old_pos[0]][old_pos[1]]
  
            cost = calcCost(temp_mat,goal)
            level = root.level + 1   #level of child node = level of parent node +1 

            child = node(root,temp_mat,level,cost+level)  #creation of child node

            children.append(child)
            temp_mat = copy(root.mat)  
    
    return children


def calcCost(mat,goal):
    """Cost/Heuristic is Manhattan Distance:
        The sum of the distances (sum of the vertical and horizontal distance) from the blocks to their goal positions
        """

    cost = 0
    for i in range(0,3):
        for j in range(0,3):
            if(mat[i][j]!=0):
                ideal_pos = find(goal,mat[i][j])
                cost = cost + (abs(ideal_pos[0]-i) + abs(ideal_pos[1] - j))
    return cost


def isValid(pos):
    """ Checks if position falls within bounds of 3x3 matrix"""
    if(pos[0] >= 0 and pos[0]<3 and pos[1]>=0 and pos[1] < 3):
        return True
    else :
        return False



def storePath(node):
    """Return list of nodes originating from initial node till current node"""
    global path 
    path = []
    if node == None:  
        return  

    storePath(node.parent)  
    path.append(node)    

    return path
   

def printPath(node_path):
    """ Prints out all elements in path sequentially"""

    for step in node_path:
        for i in range(0,3):
                    for j in range(0,3):
                    	if(step.mat[i][j] == 0):
                    		print("_", end = " ")
                    	else :
                        	print(step.mat[i][j],end =" ")
                    print()
        print()
   			 
                    
def inversions(mat):
    """ Returns number of inversions in given matrix """
    ans = 0
    for i in range(3):
        for j in range(3):
            if(mat[i][j]!=0):
                for m in range(0,3):
                    if(m<i):
                        continue
                    for n in range(0,3):
                        if(mat[m][n]==0):
                            continue
                        if(m==i and n <= j):
                            continue
                        if(mat[i][j] >  mat[m][n]):
                            ans = ans +1 
    return ans


def isSolvable(input,goal):
    """ Checks if parity of inversions of input and goal matrix equal"""
    return (inversions(input)%2)== (inversions(goal)%2)

#Main code


#Taking input from user

print("Enter start configuration")
print("Note: Input must consist of 3 lines where each line contains 3 elements each seperated by a whitespace")
print("      Empty tile in puzzle must be represented as 0")


#store initial configuration in inp list 
inp = []
for i in range(0,3):
    temp = input().split(" ")
    temp_int = []
    for i in temp:
        temp_int.append(int(i))
    inp.append(temp_int)
          
#store goal configuration in goal list
print("Enter goal configuration")
goal = []
for i in range(0,3):
    temp = input().split(" ")
    temp_int = []
    for i in temp:
        temp_int.append(int(i))
    goal.append(temp_int)



if isSolvable(inp,goal):

        root_node = node(None,inp,0,calcCost(inp,goal)) #creation of root node 

        visited = []  #list of already visited nodes
        pq = []       #initialising priority queue
        pq.append(root_node)

        heapq.heapify(pq)    #creates heap from given list

        visited.append(root_node)

        while len(pq)!=0:
            cur_node = heapq.heappop(pq)  #accessing node of minimum cost from priority queue

            #if goal configuration reached
            if(cur_node.mat == goal ):     
                node_path = storePath(cur_node)   #store list of nodes from intial to goal node
                step_num = len(node_path)-1      #store number of steps from intial to goal

                print("The number of steps required is ",step_num)
                inp_char = input("If you would to like print out all the steps: enter Y else enter N:  ")

                while True:
                    if inp_char == 'Y':
                        printPath(node_path)   #print all nodes from inital to goal config
                        break
                    elif inp_char == 'N':
                        break
                    else :
                        inp_char = input("Kindly enter Y or N:  ")

                break

            #expanding current node 
            children = successors(cur_node,goal)   #accessing all children of currrent node i.e all valid configurations originating from current node
            for child in children :
                if child not in visited:
                    heapq.heappush(pq,child)   #adding node to priority queue
                    visited.append(child)  

else:
    print("Goal is not reachable")


