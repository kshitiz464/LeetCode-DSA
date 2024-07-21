class Solution:
    def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
        # k=window size
        # The integers with same value should be within the window
        # I will start iterating from Left=0 and R will be from 0 to len
        # If i get same values, then i will return True
        L=0
        window = set()
        for R in range(len(nums)):
            if R-L > k:
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])

        


            

        










print(Solution.containsNearbyDuplicate(nums=[4,1,2,3,1,5],k=3))















# dict1={}
#         for i in range(len(nums)):
#             if nums[i] in dict1:
#                 dict1[nums[i]]+=1
#             else:
#                 dict1.update({nums[i]:1})
#             print(dict1)
        #     flag=False
        #     for j in range(len(nums)):
        #         if abs(i-j)<=k and nums[i] == nums[j] and i!=j :
        #             print(i,j)
        #             flag=True
        #     if flag==True:
        #         break
        # return flag