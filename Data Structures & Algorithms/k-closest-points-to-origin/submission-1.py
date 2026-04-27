class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x1 = 0
        y1 = 0
        dist = []
        for point in points:
            distance = math.pow((math.pow((0-point[0]),2)+(math.pow((0-point[1]),2))),0.5)
            dist.append([distance,point[0],point[1]])
        heapq.heapify(dist)
        ans = []
        for i in range(k):
            distance = heapq.heappop(dist)
            ans.append([distance[1],distance[2]])
        return ans