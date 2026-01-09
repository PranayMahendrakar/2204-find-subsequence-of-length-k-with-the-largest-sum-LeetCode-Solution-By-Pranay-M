class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Get indices of k largest elements
        indexed = [(num, i) for i, num in enumerate(nums)]
        indexed.sort(reverse=True)
        indices = sorted([i for num, i in indexed[:k]])
        return [nums[i] for i in indices]