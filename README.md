# 8PuzzleProblem



How to execute:
	User must carefully enter input of initial and goal configuration.
	
	User must enter 3 lines where each line contains 3 values each separated by a single whitespace (3x3 matrix format).
	
        0 must be entered at the position of the blank tile.

	Example: 
	Enter start configuration
	Note: Input must consist of 3 lines where each line contains 3 elements each separated by a whitespace
	      Empty tile in puzzle must be represented as 0
	1 2 3
	4 5 6
	7 8 0
	Enter goal configuration
	1 2 3
	4 0 5
	7 8 6
	The number of steps required is  2
	If you would to like print out all the steps: enter Y else enter N:  N
	
	
Explanation of code:
	Class node defined whose object has attributes are its parent node, matrix representation, cost to reach goal node, steps to reach given node
	We then define various functions
	copy is used to obtain exact replica of a matrix 
	find is used to obtain the position of a certain value in a matrix
	successors is used to obtain a list of all valid configurations which can arise from a given configuration (only 1 step allowed)
	calcCost is used to calculate Manhattan Distance of a given matrix and goal matrix which is the heuristic we use to decide which node must be expanded
	isValid is used to check if position is valid in a 3x3 matrix with zero indexing
	storePath stores the path from initial configuration to goal configuration in a list
	printPath prints the path from initial to goal in appropriate format
	inversions returns the number of inversions in a matrix( an inversion is any pair of tiles i and j where i < j but i appears after j when considering the board in row-major order)
	isSolvable is used to check if it is possible to reach goal configuration
	
	In the main function -
	Input initial and goal configuration in 3x3 list
	If not solvable, print Goal not reachable and program terminates
	If solvable,
	Root node is created whose parent is set to null and matrix equal to that of initial configuration
	Priority queue and list of visited nodes is initialised
	Initially, root node added to priority queue
	
	The node with minimum cost function is removed from the priority queue and its children which haven't been previously visited are added to the priority queue.
	This goes on until goal configuration reached.
	Then, the number of steps required to reach goal is printed and user is given a choice to print all steps to reach goal from initial.
	
