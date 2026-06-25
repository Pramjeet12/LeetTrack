class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = nums[0]
        for i in range(0, len(nums)):
            if smallest > nums[i]:
                smallest = nums[i]
            else:
                smallest = smallest
            
        largest = nums[0]
        for i in range(0, len(nums)):
            if largest < nums[i]:
                largest = nums[i]
            else:
                largest = largest

        frequency = {}
        for i in range(0, len(nums)):
            frequency[nums[i]] = 1

        missing = []
        for i in range(smallest, largest+1):
            if i not in frequency:
                missing.append(i)

        return missing