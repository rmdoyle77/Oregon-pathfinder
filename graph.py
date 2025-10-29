import math
from typing import Dict, List, Tuple


class Graph:


    def __init__(self):
        self.adjacency: Dict[str, List[Tuple[str, str, float]]] = {}
        self.coords: Dict[str, Tuple[float, float]] = {}

    def add_vertex(self, name: str, lat: float, lon: float):
        self.coords[name] = (lat, lon)
        if name not in self.adjacency:
            self.adjacency[name] = []

    def add_edge(self, src: str, dst: str, highway: str, dist_miles: float):
        if src not in self.adjacency:
            self.adjacency[src] = []
        self.adjacency[src].append((dst, highway, dist_miles))

    def neighbors(self, city: str) -> List[Tuple[str, str, float]]:
        return self.adjacency.get(city, [])

    def has_city(self, name: str) -> bool:
        return name in self.coords

    def haversine(self, a: str, b: str) -> float:

        if a not in self.coords or b not in self.coords:
            return 0.0

        (lat1, lon1) = self.coords[a]
        (lat2, lon2) = self.coords[b]

        R = 3959.0  # Earth radius in miles

        phi1, lam1, phi2, lam2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dphi = phi2 - phi1
        dlam = lam2 - lam1

        hav_a = math.sin(dphi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * (math.sin(dlam / 2.0) ** 2)
        c = 2.0 * math.asin(math.sqrt(hav_a))

        return R * c


def load_vertices(graph: Graph, filename: str):

    with open(filename, "r") as f:
        first = True
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if first:
                # skip header
                first = False
                continue

            parts = line.split(",")
            if len(parts) < 3:
                continue
            city = parts[0].strip()
            lat = float(parts[1].strip())
            lon = float(parts[2].strip())
            graph.add_vertex(city, lat, lon)


def load_edges(graph: Graph, filename: str):

    with open(filename, "r") as f:
        first = True
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if first:
                first = False
                continue

            parts = line.split(",")
            if len(parts) < 4:
                continue
            src = parts[0].strip()
            dst = parts[1].strip()
            highway = parts[2].strip()
            dist = float(parts[3].strip())
            graph.add_edge(src, dst, highway, dist)
