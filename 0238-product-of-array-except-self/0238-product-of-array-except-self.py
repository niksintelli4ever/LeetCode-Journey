class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nonzeroprod=1
        prod=1
        zerocount=0
        res=[0]*len(nums)
        for i in nums:
            prod*=i
            if i==0:
                zerocount+=1
            else:
                nonzeroprod*=i
        
        if zerocount>1:
            return res
        for i in range(len(nums)):
            if nums[i]==0:
                res[i]=nonzeroprod
            else:
                res[i]=prod//nums[i]
        
        return res