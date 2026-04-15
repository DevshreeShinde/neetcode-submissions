class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals)
        for i in range(len(intervals)):
            if ans == []:
                ans.append(intervals[i])
            else:
                start,end = ans.pop()
                if intervals[i][0]<=end:
                    end = max(end,intervals[i][1])
                    ans.append([start,end])
                else:
                    ans.append([start,end])
                    ans.append(intervals[i])
        return ans

        