class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return (lambda order=(dict((num, i) for i, num in enumerate(arr2))): sorted(arr1, key=lambda x: (order.get(x, 1000), x)))()