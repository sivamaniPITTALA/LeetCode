class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        cumulative_sum = 0
        hashmap = {0: 1}
        for i in range(n):
            cumulative_sum += nums[i]
            remainder = cumulative_sum % k
            if remainder in hashmap:
                count += hashmap[remainder]
            hashmap[remainder] = hashmap.get(remainder, 0) + 1
        return count