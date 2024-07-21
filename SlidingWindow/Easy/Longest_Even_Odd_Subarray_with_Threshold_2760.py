class Solution:
    def longestAlternatingSubarray( nums: list[int], threshold: int) -> int:
        curr=0
        length=0

        for i in range(len(nums)):
            if nums[i] > threshold:
                curr = 0
            elif nums[i]%2==0 and curr == 0:
                curr = 1
            elif curr>0 and nums[i]%2 != nums[i-1]%2:
                curr +=1
            else:
                curr = 1 if nums[i]%2 == 0 else 0
            length = max(length,curr)
        return length




        #         if nums[i+1]%2 and nums[i]<=threshold and nums[i - 1]<=threshold:
        #         l,r=r,r+1
        #         if length==0:
        #             length+=2
        #             print(length)
        #         else:
        #             length+=1
        #             print(length)
        # return length
print(Solution.longestAlternatingSubarray([3,2,5,4],5))
