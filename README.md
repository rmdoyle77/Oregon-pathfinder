# 🌲 Oregon Pathfinder

> An algorithmic routing engine comparing **Dijkstra's Algorithm**, **Greedy Best-First Search**, and **A\* Search** across an adjacency network of 22 Oregon cities and 52 interconnecting highway corridors.

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](#tech-stack)
[![Algorithms](https://img.shields.io/badge/Domain-Graph%20Search%20%26%20Pathfinding-2ea44f?style=for-the-badge)](#algorithms-compared)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

---

## 🎯 Overview

**Oregon Pathfinder** models geographic waypoints and highway transit corridors across Oregon as a weighted adjacency graph. It implements, instruments, and benchmark-tests three foundational pathfinding algorithms to evaluate the performance trade-offs between heuristic goal direction, optimality guarantees, and vertex exploration efficiency.

---

## 🔬 Algorithms Compared

| Algorithm | Optimality Guarantee | Heuristic Used | Primary Trade-Off |
| :--- | :--- | :--- | :--- |
| **Dijkstra's Algorithm** | Guaranteed Shortest Path | None (Explores unweighted frontiers) | Reliable and optimal, but expands unnecessary vertices radially. |
| **Greedy Best-First Search** | No (Approximation) | Haversine Straight-Line Distance ($h$) | Extremely fast and goal-directed, but vulnerable to sub-optimal detours. |
| **A\* Search** | Guaranteed Shortest Path | Admissible Haversine Heuristic ($f = g + h$) | The gold standard: combines Dijkstra's accuracy with Greedy's goal direction. |

---

## 📊 Benchmark & Performance Analysis

Testing across routes like **Portland → Salem**, **Portland → Eugene**, and **Portland → Ashland** demonstrates distinct algorithmic behaviors:

### 1. Short Route: Portland → Salem (Direct I-5 corridor)
- **Dijkstra's:** 47.0 miles | 3 vertices explored | 6 edges evaluated | ~0.00012s
- **A\*:** 47.0 miles | 3 vertices explored | 6 edges evaluated | ~0.00012s

### 2. Medium Route: Portland → Eugene
- **Dijkstra's:** 111.0 miles | 7 vertices explored | 17 edges evaluated | ~0.00025s
- **A\*:** 111.0 miles | 4 vertices explored | 10 edges evaluated | ~0.00016s

### 3. Long Route: Portland → Ashland (283 miles)
- **Dijkstra's Algorithm:** Guarantees the shortest path (283 miles), but expands outward in all directions, evaluating many irrelevant cities.
- **Greedy Best-First Search:** Prioritizes nodes that appear geometrically closer via Haversine distance, leading to a sub-optimal **297-mile path** (an extra 14-mile detour).
- **A\* Algorithm:** Achieves the identical optimal **283-mile path** as Dijkstra while cutting node expansions nearly in half.

> **Admissibility of the Heuristic:**  
> The Haversine straight-line distance function acts as an **admissible heuristic** because straight-line Euclidean distance between two geographic coordinates never exceeds actual road driving distance ($h(n) \le h^*(n)$), mathematically guaranteeing that A* finds the optimal path without overestimating costs.

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/rmdoyle77/oregon-pathfinder.git
cd oregon-pathfinder
```

### 2. Run the Interactive CLI
```bash
python3 main.py
```

### 3. Example Interaction
```text
Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
Enter choice (1-3): 3

Enter start city: Portland
Enter destination city: Ashland

>>> Path found: Portland → Salem → Albany → Eugene → Roseburg → Grants_Pass → Medford → Ashland
>>> Total distance: 283.0 miles
>>> Vertices explored: 8
>>> Edges evaluated: 21
>>> Execution time: 0.000210 seconds
```

---

## 🛠️ File Structure

- `main.py` — Interactive CLI entry point and menu driver.
- `search.py` — Implementations of Dijkstra, Greedy Best-First, and A* search algorithms.
- `graph.py` — Graph representation, adjacency structures, and Haversine distance calculations.
- `vertices_v1.txt` — Oregon city coordinates (latitude / longitude).
- `graph_v2.txt` — Weighted highway edge definitions between Oregon vertices.

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
