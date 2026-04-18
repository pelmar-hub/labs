from collections import defaultdict
import heapq
class GameNetworkSolver:
    def __init__(self,input_file='input.txt', output_file='output.txt'):
        self.input_file = input_file
        self.output_file = output_file
        self.n = 0
        self.m = 0
        self.graph = defaultdict(list)
    def read_file(self):
        with open(self.input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            self.n, self.m = map(int, lines[0].split())
            self.clients = set(map(int, lines[1].split()))
            for line in lines[2:]:
                u, v, latency = map(int, line.split())
                self.graph[u].append((v, latency))
                self.graph[v].append((u, latency))
    def _dijkstra(self, start_node):
        distances = {node: float('inf') for node in range(1, self.n + 1)}
        distances[start_node] = 0 
        pq = [(0, start_node)]           
        while pq:
            current_dellay, current_node = heapq.heappop(pq)
            if current_dellay > distances[current_node]:
                continue
            for neighbor, weight in self.graph[current_node]:
                distance = current_dellay + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances

    def solve(self):
        if not self.graph:
            self.read_file()
        candidates = [node for node in range(1, self.n + 1) if node not in self.clients]

        best_max_latency = float('inf')
        
        for candidate in candidates:
            distances = self._dijkstra(candidate)
            max_latency_for_candidate = max(distances[client] for client in self.clients)

            if max_latency_for_candidate < best_max_latency:
                best_max_latency = max_latency_for_candidate

        self._write_result(best_max_latency)
    def _write_result(self, result):
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(str(result) + '\n')

if __name__ == '__main__':
    solver = GameNetworkSolver('gamsrv.in', 'gamsrv.out')
    solver.solve()