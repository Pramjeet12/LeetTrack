class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        frequency = {}
        for i in range(0, len(nums)):
            frequency[nums[i]] = 0

        missing = []
        for i in range(1, len(nums)+1):
            if i not in frequency:
                missing.append(i)

        return missing