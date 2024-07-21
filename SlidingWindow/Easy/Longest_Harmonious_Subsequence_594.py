class Solution:
    def findLHS(self, nums: list[int]) -> int:
        #291ms, 18.04mb
        nums.sort()
        l,r=0,1
        sum=0
        while (r<len(nums)):
            diff= nums[r] - nums[l]
            if diff==1:
                sum = max(sum,r-l+1)
            if diff<=1:
                r+=1
            else:
                l+=1
        return sum










# First Approach
# 385mb,18.2mb
#         ma={}
#         sum=0
#         for i in nums:
#             if i in ma:
#                 ma[i]+=1
#             else:
#                 ma[i]=1
#         for i in ma:
#             if i+1 in ma:
#                 sum=max(sum,ma[i]+ma[i+1])
#         return sum
