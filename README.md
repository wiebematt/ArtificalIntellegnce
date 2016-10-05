# ArtificalIntellegnce
Repo for CS5100

Problem 1
Made a generic graph search function that takes in the problem and a data
structure and solves the problem using the data structure based on the . 
For DFS, I passed in a stack since we want to expand the children of the
node that we are currently expanding. A stack will put this node's 
children at the the front.

Problem 2
Using the generic graph search function for BFS, I passed in a queue since
we want to all nodes at this level before we expand any of their children.
The queue solves this by putting the children at the back and we will only
reach the children once all the children from all nodes on this level have
been expanded.

Problem 3
Using the generic graph search function for UCS, I passed a priority queue
with function structure with the provided function getCostOfActions so 
that each node would be expanded in order of cost to reach that node.

Problem 4
Using the generic graph search function for A*, I passed a priority queue
with function structure with the provided function getCostOfActions and 
a heuristic which takes in the current position (the first element of my
state tuple) and the problem. So each node will be expanded according to 
its cost and the heuristic provided.

Problem 5
For this problem much like before, I let state be a tuple: 
(current position, list of remaining corners) and thus the goal state is
when the list is empty. In getSuccessors, I check if the next position 
would remove a corner and adjust a copy of the corners list so and then 
push these elements as a tuple on the successors list. This state only
keeps track of relevant information, like where we are and where we need
to go.

Problem 6

The cornersHeuristic function uses calculates the L2 norm between the 
current position and the nearest corner and then does the same operation
only changing what is considered current position to be the last closest
corner. The heureistic is admissible since if there were no walls in 
between the current position and the closest corner, then the L2 norm is
precisely the cost to reach that corner. The same logic can be applied 
when doing the subsequent calculations to the other corners. This 
heuristic has the nice property of going for the corner that will yield
the lowest total path rather than just the closest corner. This 
heuristic was the most successful one tested out of considering the max
corner distance, min corner distance, sum of all corner distances.

This heuristic is also consistent since if there were not walls, taking 
actions will reduce the 

Problem 7



Problem 8
For this problem, I let the goal state be checking whether where we
currently are is the closest food since this is only true once we hit
the last food. I simply used bfs as my search algo since the goal state
is one of the closest foo