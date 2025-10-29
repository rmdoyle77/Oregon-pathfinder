import math
import time
import heapq
from typing import Dict, Tuple, List, Any
from graph import Graph


def reconstruct_path(parent: Dict[str, Tuple[str, str, float]], start: str, goal: str) -> List[str]:
   
    if start == goal:
        return [start]

    if goal not in parent:
        return []

    path = [goal]
    cur = goal
    while cur != start:
        cur = parent[cur][0]
        path.append(cur)
    path.reverse()
    return path


def dijkstra(graph: Graph, start: str, goal: str) -> Dict[str, Any]:
    
    start_time = time.perf_counter()

    dist: Dict[str, float] = {city: math.inf for city in graph.coords}
    dist[start] = 0.0

    parent: Dict[str, Tuple[str, str, float]] = {}
    parent[start] = (start, None, 0.0)

    pq: List[Tuple[float, str]] = [(0.0, start)]

    vertices_explored = 0  
    edges_evaluated = 0    

    visited = set()

    while pq:
        g_cost, city = heapq.heappop(pq)

        if city in visited:
            continue
        visited.add(city)

        vertices_explored += 1

        if city == goal:
            break

        for (nbr, highway, edge_dist) in graph.neighbors(city):
            edges_evaluated += 1

            new_cost = g_cost + edge_dist
            if new_cost < dist[nbr]:
                dist[nbr] = new_cost
                parent[nbr] = (city, highway, edge_dist)
                heapq.heappush(pq, (new_cost, nbr))

    end_time = time.perf_counter()

    path = reconstruct_path(parent, start, goal)
    total_distance = dist[goal]

    if total_distance == math.inf:
        total_distance = None

    return {
        "algorithm": "Dijkstra's Algorithm",
        "path": path,
        "distance": total_distance,
        "vertices_explored": vertices_explored,
        "edges_evaluated": edges_evaluated,
        "execution_time": end_time - start_time
    }


def greedy_best_first(graph: Graph, start: str, goal: str) -> Dict[str, Any]:


    start_time = time.perf_counter()

   
    g_cost: Dict[str, float] = {city: math.inf for city in graph.coords}
    g_cost[start] = 0.0

    parent: Dict[str, Tuple[str, str, float]] = {}
    parent[start] = (start, None, 0.0)

    pq: List[Tuple[float, str]] = [(graph.haversine(start, goal), start)]

    vertices_explored = 0
    edges_evaluated = 0

    visited = set()

    while pq:
        h_val, city = heapq.heappop(pq)

        if city in visited:
            continue
        visited.add(city)

        vertices_explored += 1

        if city == goal:
            break

        for (nbr, highway, edge_dist) in graph.neighbors(city):
            edges_evaluated += 1


            maybe_cost = g_cost[city] + edge_dist
            if maybe_cost < g_cost[nbr]:
                g_cost[nbr] = maybe_cost
                parent[nbr] = (city, highway, edge_dist)

            if nbr not in visited:
                priority = graph.haversine(nbr, goal)
                heapq.heappush(pq, (priority, nbr))

    end_time = time.perf_counter()

    path = reconstruct_path(parent, start, goal)
    total_distance = g_cost[goal]
    if total_distance == math.inf:
        total_distance = None

    return {
        "algorithm": "Greedy Best-First Search",
        "path": path,
        "distance": total_distance,
        "vertices_explored": vertices_explored,
        "edges_evaluated": edges_evaluated,
        "execution_time": end_time - start_time
    }


def astar(graph: Graph, start: str, goal: str) -> Dict[str, Any]:

    start_time = time.perf_counter()

    g_cost: Dict[str, float] = {city: math.inf for city in graph.coords}
    g_cost[start] = 0.0

    parent: Dict[str, Tuple[str, str, float]] = {}
    parent[start] = (start, None, 0.0)

    def f_score(city: str) -> float:
        return g_cost[city] + graph.haversine(city, goal)

    pq: List[Tuple[float, str]] = [(f_score(start), start)]

    vertices_explored = 0
    edges_evaluated = 0

    visited = set()

    while pq:
        f_val, city = heapq.heappop(pq)

        if city in visited:
            continue
        visited.add(city)

        vertices_explored += 1

        if city == goal:
            break

        for (nbr, highway, edge_dist) in graph.neighbors(city):
            edges_evaluated += 1

            tentative_g = g_cost[city] + edge_dist

            if tentative_g < g_cost[nbr]:
                g_cost[nbr] = tentative_g
                parent[nbr] = (city, highway, edge_dist)
                heapq.heappush(pq, (tentative_g + graph.haversine(nbr, goal), nbr))

    end_time = time.perf_counter()

    path = reconstruct_path(parent, start, goal)
    total_distance = g_cost[goal]
    if total_distance == math.inf:
        total_distance = None

    return {
        "algorithm": "A* Search",
        "path": path,
        "distance": total_distance,
        "vertices_explored": vertices_explored,
        "edges_evaluated": edges_evaluated,
        "execution_time": end_time - start_time
    }
