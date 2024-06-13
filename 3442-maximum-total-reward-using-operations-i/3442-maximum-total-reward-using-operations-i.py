class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        possible = set()
        
        for r in rewardValues:
            dp = possible.copy()
            for val in possible:
                if val<r:
                    dp.add(val+r)
            dp.add(r)
            possible = dp
            
        return max(possible)