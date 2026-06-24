class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        frequency = {}
        for i in range(0, len(nums)):
            if nums[i] in frequency:
                frequency[nums[i]] += 1
            else:
                frequency[nums[i]] = 1

        j = 0
        for key in frequency:
            if key == val:
                continue
            for _ in range(0, frequency[key]):
                nums[j] = key           
                j = j + 1
            
        return j