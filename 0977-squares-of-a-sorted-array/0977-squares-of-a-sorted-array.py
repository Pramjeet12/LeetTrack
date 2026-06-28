class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square = []
        for i in range(0, len(nums)):
            squarevalue = nums[i]*nums[i]
            square.append(squarevalue)

        square.sort()
        return square