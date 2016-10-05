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
corner. The heuristic is admissible since if there were no walls in 
between the current position and the closest corner, then the L2 norm is
precisely the cost to reach that corner. The same logic can be applied 
when doing the subsequent calculations to the other corners. This 
heuristic has the nice property of going for the corner that will yield
the lowest total path rather than just the closest corner. This 
heuristic was the most successful one tested out of considering the max
corner distance, min corner distance, sum of all corner distances.

This heuristic is also consistent given the following proof:
Assume that moving for any point to its neighbors incurs a cost of 1.
Then consider 2 point on the maze z and z' s.t. the closest corner for 
both of them is the same. Without loss of generality(WLOG), let z' be closer 
and let c and c' represent the L2 norm for z and z' respectively (this is
equivalent to the overall heuristic as the rest of the heuristic is 
calculated from the rest of the corner is the same order since both points
have the same closest corner). Thus in order to prove consistency, we
must show that c - c' <= 1 as 1 is the cost from getting to z to z' and 
the heuristic must decrease no more than the cost between the two points.

Proof for c - c' <= 1:
WLOG, let x and y represent the side lengths of the triangles between c, c'
and the closest corner and let the x value for c' be 1 less than the x 
value for c. 

Thus, c - c' <= 1 can be rewritten as 
sqrt(x^2 + y^2) - sqrt((x-1)^2 + y^2) <= 1,  =>
sqrt(x^2 + y^2) <= 1 + sqrt((x-1)^2 + y^2), square both sides 
x^2 + y^2 <= 1 + (x-1)^2 + y^2 + 2sqrt((x-1)^2 + y^2), cancel like terms
0 <= -2x + 2 + 2sqrt((x-1)^2 + y^2) =>
x <= 1 + sqrt((x-1)^2 + y^2) =>
x -1 <= c' which is true since c' = sqrt((x-1)^2 + y^2) since y^2 >= 0 QED.

So the heuristic is consistent.
Problem 7

For this problem, the state was left as just the position of pacman. For
the heuristic, I created a list of the distances to all food and got the
maximum distance to any food. By choosing nodes based on reducing this 
number, the distance traveled should be minimized. This was not my first thought
as I thought that summing all distances would favor keeping the overall
path cost reduced like in Problem 6 however, while this method solved the
problem in less 10 seconds, it did not lead to the optimal solution. Using
min resulted in a timeout and thus I tried max and it worked better than
expected.

This heuristic is consistent since given node N any successors P are at 
cost 1 away and their pathway to the most distant node either goes through N 
(thus h(P) = 1 + h(N)) or it does not (thus h(P) = h(N) - 1). This will
hold true even if the further node changes for P since we can simply swap
the roles of N and P.

Problem 8
For this problem, I let the goal state be checking whether where we
currently are is the closest food since this is only true once we hit
the last food. I used manhattan distance as my way of sorting the food
since we are not necessarily guaranteed to have any successors and the
manhattan distance is a good approximation of the maze distance (since
I can't use that function due to not having gameState argument).

I simply used BFS as my search algorithm since the goal state
is one of the closest food and will be more consistent is finding the food
vs DFS (ucs and A* offer minimal improvement that I did not feel like
coding). 

Simply going for the closest dot does not yield the shortest path.

____________________________________________________________________
| F4                                F2       O    F1              F3|
---------------------------------------------------------------------
In this example, the closest food will algorithm will go for the food in
the following order: F1, F2, F3, F4. Thus the total distance traveled, 
D is D = O->F1 + F1->F2 + F2->F3 + F3->F4. However simply going for F3 
first yields a distance D' = O->F3 + F3->F4. Then D -> D' = 2 (S->F1). 
So D travels the distance S->F1 2 more than necessary and thus is not 
optimal.