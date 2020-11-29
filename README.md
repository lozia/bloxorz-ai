# bloxorzAI
Project 1 for CSCI Artificial Intelligence. A* algorithm with a heuristic estimation function.

Description of my program:
  My program layout followed the overall layout from the Project Requirements precisely, nothing speciall or new other than in the requirements. In my heuristic, I grouped the conditions into 2 that, one is either the distance of x or y to goal is smaller than 3, the other one is distance of x and y divided by two. Since if the blox is within a 3x3 square with goal, the min move is 3, however, if it is out of the 3x3 square of the goal, it can have min of 2 moves. Yet, more to explore.

This program used the Pandas model to generate the html table.

Q1) Why doesn't DFS work?
DFS doesn't work since it isn't the shortest path, got a->b->d->g.
DFS will also get stuck in an infinite loop.

Q2) Can you solve your board from above? 
My board is objectively unsolvable, however, my method passed the test.

Q3) What about the boards in boards.zip?
I can solve those who have a solution.

Q4) What happens when you use A-Star with a heuristic function that always returns 0?
According to my output, the one always returns 0 gives a lot of expansions more than the one with dynamic heuristic fn, especially when the board comes large.

Q4 Output:
Testing problem <bloxorz_problem.BloxorzProblem object at 0x000001EBC6F65D90>  :
1259 paths have been expanded and 1880 paths remain in the frontier
Path found: ((0, 1), (0, 1))
   --R--> ((1, 1), (2, 1))
   --U--> ((1, 0), (2, 0))
   --L--> ((0, 0), (0, 0))
   --D--> ((0, 1), (0, 2))
   --R--> ((1, 1), (1, 2))
   --R--> ((2, 1), (2, 2))
   --U--> ((2, 0), (2, 0))
   --L--> ((0, 0), (1, 0))
   --D--> ((0, 1), (1, 1))
   --R--> ((2, 1), (2, 1))
Testing problem <bloxorz_problem.BloxorzProblem object at 0x000001EBC6F65D90>  :
16 paths have been expanded and 0 paths remain in the frontier
Path found: ((0, 1), (0, 1))
   --R--> ((1, 1), (2, 1))
   --U--> ((1, 0), (2, 0))
   --L--> ((0, 0), (0, 0))
   --D--> ((0, 1), (0, 2))
   --R--> ((1, 1), (1, 2))
   --R--> ((2, 1), (2, 2))
   --U--> ((2, 0), (2, 0))
   --L--> ((0, 0), (1, 0))
   --D--> ((0, 1), (1, 1))
   --R--> ((2, 1), (2, 1))
