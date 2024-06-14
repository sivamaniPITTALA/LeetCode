class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        counter = Counter(nums)
        max_num = max(nums)
        min_num = min(nums)
        zero_counted = []
        for i in range(max_num):
            if i not in counter and i > min_num:
                zero_counted.append(i)
        count = 0
        indx = 0
        curr_max = max_num + 1
        for num in sorted(counter.keys()):
            while counter[num] > 1 and indx < len(zero_counted):
                if zero_counted[indx] > num:
                    count += zero_counted[indx] - num
                    counter[num] -= 1
                indx += 1
            while counter[num] > 1:
                count += curr_max - num
                counter[num] -= 1
                curr_max += 1
        return count