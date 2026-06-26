class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxcount = float("-inf")
        total = 0
        for i in range(0, len(nums)):
            total += nums[i]
            maxcount = max(maxcount, total)

            if total < 0:
                total = 0

        return maxcount