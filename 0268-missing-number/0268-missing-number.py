class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missingnumber=(len(nums)*(len(nums)+1))//2 - sum(nums)
        return missingnumber
        