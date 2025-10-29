from graph import Graph, load_vertices, load_edges
from search import dijkstra, greedy_best_first, astar


def pretty_print_result(result: dict):
    
    algo_name = result.get("algorithm", "Unknown Algorithm")

    path_list = result.get("path", [])
    if not path_list:
        path_str = "(no path found)"
    else:
        path_str = " \u2192 ".join(path_list) 

    dist = result.get("distance", None)
    if dist is None:
        dist_str = "unreachable"
    else:
        dist_str = f"{dist:.1f} miles"

    vertices_explored = result.get("vertices_explored", 0)
    edges_evaluated = result.get("edges_evaluated", 0)
    exec_time = result.get("execution_time", 0.0)

    print(f"\nAlgorithm: {algo_name}")
    print(f"Path found: {path_str}")
    print(f"Total distance: {dist_str}")
    print(f"Vertices explored: {vertices_explored}")
    print(f"Edges evaluated: {edges_evaluated}")
    print(f"Execution time: {exec_time:.6f} seconds\n")


def run_search(graph: Graph, algo_choice: str, start: str, goal: str) -> dict:

    if algo_choice == "1":
        return dijkstra(graph, start, goal)
    elif algo_choice == "2":
        return greedy_best_first(graph, start, goal)
    elif algo_choice == "3":
        return astar(graph, start, goal)
    else:
        raise ValueError("Invalid algorithm selection.")


def main():
    g = Graph()
    load_vertices(g, "vertices_v1.txt")
    load_edges(g, "graph_v2.txt")

    print("Welcome to the Oregon Pathfinder!\n")

    while True:
        print("Select pathfinding algorithm:")
        print("1. Dijkstra's Algorithm")
        print("2. Greedy Best-First Search")
        print("3. A* Algorithm")
        algo = input("Enter choice (1-3): ").strip()

        if algo not in ("1", "2", "3"):
            print("Invalid choice. Please enter 1, 2, or 3.\n")
            continue

        start_city = input("\nEnter start city: ").strip()
        dest_city = input("Enter destination city: ").strip()

        if not g.has_city(start_city):
            print(f"Unknown city '{start_city}'. Please check spelling and try again.\n")
            continue
        if not g.has_city(dest_city):
            print(f"Unknown city '{dest_city}'. Please check spelling and try again.\n")
            continue

       
        if algo == "1":
            label = "Dijkstra's Algorithm"
        elif algo == "2":
            label = "Greedy Best-First Search"
        else:
            label = "A* Algorithm"

        print(f"\nRunning {label}...\n")

        try:
            result = run_search(g, algo, start_city, dest_city)
        except Exception as e:
            print(f"Error running search: {e}\n")
            continue

        pretty_print_result(result)

        again = input("Search another route? (y/n): ").strip().lower()
        if again != "y":
            print("\nThank you for using the Oregon Pathfinder!")
            break

        print()  


if __name__ == "__main__":
    main()
