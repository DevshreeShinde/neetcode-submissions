class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')]*(n+1)
        adj = [[] for _ in range(n+1)]
        for u,v,time in times:
            adj[u].append([v,time])
        st = []
        heapq.heapify(st)
        heapq.heappush(st,(0,k))
        dist[k]=0
        while st:
            cost,city=heapq.heappop(st)
            if cost>dist[city]:
                continue
            for nei,wt in adj[city]:
                if wt+cost<dist[nei]:
                    dist[nei]=wt+cost
                    heapq.heappush(st,(wt+cost,nei))
        count=0
        ans = max(dist[1:])

        if ans == float('inf'):
            return -1

        return ans