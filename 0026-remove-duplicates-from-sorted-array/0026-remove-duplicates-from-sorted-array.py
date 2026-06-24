class Solution(object):
    def removeDuplicates(self, nums):
        frequency = {}
        for i in range(0, len(nums)):
            frequency[nums[i]] = 0  

        j = 0
        for key in frequency:
            nums[j] = key           
            j = j + 1
            
        return j
