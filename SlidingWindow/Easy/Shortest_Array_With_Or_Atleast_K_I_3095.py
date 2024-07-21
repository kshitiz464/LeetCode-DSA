class Solution:
	def minimumSubarrayLength(nums: List[int], k: int) -> int:		
		N= len(nums)
        Inf = 10**20
        ans=Inf

        for left in range(N):
            curr=0
            for right in range(left,N):
                curr|=nums[right]
                if curr>=k:
                    ans = min(ans, right-left+1)
        return ans if ans!=Inf else -1
