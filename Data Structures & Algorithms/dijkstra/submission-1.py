from collections import defaultdict
import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # convert to adjacency list
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        distances = {}
        for i in range(n):
            distances[i] = -1
        
        heap = [(0, src)]

        while heap:
            dist1, curr = heapq.heappop(heap)
            if distances[curr] != -1:
                continue
            distances[curr] = dist1
            
            for neighbor, dist2 in adj[curr]:
                if distances[neighbor] == -1:
                    heapq.heappush(heap, (dist1 + dist2, neighbor))
        
        return distances

