class Solution:
    def minimumDifference(nums: list, k: int) -> int:
        l = 0
        r = 0
        for i in nums[l:r+1]:
            return i+3+k


print(Solution.minimumDifference([1, 22, 3], 5))
