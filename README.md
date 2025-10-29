PROJECT 2: Oregon Pathfinder - Ryan Doyle
How to run - When the main.py is run, it will pop up with ‘Select Pathfinding algorithm” and after you choose you type in what your starting city is (Capital Letter Sensitive) and the ending city.
Then the algorithm creates the quickest path way between the cities.
Example Program Interaction:
Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
Enter choice (1-3): 3


Enter start city: Portland
Enter destination city: Ashland




3 Examples of running
1 -
Algorithm: Dijkstra's Algorithm
Path found: Salem → Portland
Total distance: 47.0 miles
Vertices explored: 3
Edges evaluated: 6
Execution time: 0.000126 seconds
2 -
Algorithm: Dijkstra's Algorithm
Path found: Portland → Salem → Eugene
Total distance: 111.0 miles
Vertices explored: 7
Edges evaluated: 17
Execution time: 0.000255 seconds
3 -
Algorithm: Greedy Best-First Search
Path found: Portland → Newport → Florence → Coos_Bay → Roseburg → Medford
Total distance: 397.0 miles
Vertices explored: 6
Edges evaluated: 15
Execution time: 0.000356 seconds


Analysis
The Oregon Pathfinder project compares three pathfinding algorithms Dijkstra’s, Greedy Best-First, and A* on a map of 22 Oregon cities and 52 highways. Each algorithm uses a different strategy to find routes, and testing them on paths such as Portland > Salem, Portland > Eugene, and Portland > Ashland highlights their distinct strengths and weaknesses.
Dijkstra’s algorithm guarantees the shortest path by exploring all routes in order of total distance traveled. On short routes like Portland to Salem (47 miles), it quickly finds the direct I-5 connection. However, on longer trips such as Portland to Ashland (283 miles), it expands many unnecessary cities because it explores evenly in all directions. This makes it reliable but inefficient for large networks.
Greedy Best First Search takes the opposite approach. It ignores accumulated distance and instead moves toward whichever city is geographically closest to the destination using the Haversine straight-line heuristic. This makes it very fast but sometimes inaccurate. On the Portland to Ashland route, it chose a direction that looked closer on the map but led to a longer 297-mile path. Greedy’s advantage is speed, but it cannot guarantee the optimal result.
A* combines the logic of both. It adds Dijkstra’s real distance (g) and Greedy’s heuristic (h) to form f(n) = g + h. This allows A* to stay goal-directed without losing accuracy. In the Oregon tests, A* always found the same optimal path as Dijkstra but explored far fewer vertices, often about half as many on longer routes making it both accurate and efficient.
In terms of complexity, all three run in O((V + E) log V), but A* usually does less work because the heuristic narrows the search area. On a small 22-city map, the differences in runtime are negligible, but on a large national highway system, Dijkstra would slow dramatically while A* would scale efficiently. The Haversine distance serves as an admissible heuristic because the straight-line distance between two points can never exceed the actual driving distance, ensuring A*’s optimality.
Overall, Dijkstra’s Algorithm is best when accuracy is essential, Greedy Best First works for quick approximations, and A* offers the most balanced solution fast, directed, and guaranteed to find the best route. In real navigation systems, A* represents the ideal compromise between precision and performance.

