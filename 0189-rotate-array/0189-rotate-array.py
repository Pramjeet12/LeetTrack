class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        rotations = k%len(nums)
        for i in range(0, rotations):
            lastdigit = nums.pop()
            nums.insert(0, lastdigit)
        