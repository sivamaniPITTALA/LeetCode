class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        excepted = sorted(heights)
        count =0
        for i in range(len(heights)):
            count += int(excepted[i] != heights[i])
        return count
        