class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency = {}
        for i in range(0, len(nums)):
            if nums[i] in frequency:
                frequency[nums[i]] += 1
            else:
                frequency[nums[i]] = 1
        
        for key in frequency:
            if frequency[key] >= 2:
                return True

        return False
