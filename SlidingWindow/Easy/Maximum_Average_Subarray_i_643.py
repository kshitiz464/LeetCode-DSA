class Solution:
    def findMaxAverage(nums: list[int], k: int) -> float:
        n = len(nums)
        val=-1000000
        valm=-1000000
        left=0
        right=0
        curr=0
        while right<n:
            diff= right-left+1

            if diff > k:
                curr-=nums[left]
                # print("diff>k curr",curr)
                left+=1
                # print("diff>k",nums[left],nums[right])
            elif diff == k:
                curr += nums[right] 
                if curr == abs(curr):
                    val=max(val,curr)
                else:
                    valm=max(valm,curr)
            # print("diff==k",nums[left],nums[right])
            # print("diff==k curr",curr)
                right+=1



            else:
                curr+= nums[right]
                # print("diff<k curr",curr)
                # print("diff<k",nums[left],nums[right])
                right+=1
           
        return valm/k if val==-1000000 else val/k
arr=[-1]
# print(len(arr))
print(Solution.findMaxAverage(arr,1))


        # for right in range(left+1,n):
        #     # curr=0
        #     diff= right-left+1
        #     if diff > k:
        #         left+=1
        #         print("diff>k",nums[left],nums[right])
        #     elif diff<k:
        #         curr+= nums[right]
        #         print("diff<k",nums[left],nums[right])
        #     else:
        #          curr += nums[right] 
        #          print(curr)
        #          val=max(val,curr)
        #          print("diff==k",nums[left],nums[right])
        # return val
