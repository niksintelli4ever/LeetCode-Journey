class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmin=1
        cmax=1
        res=max(nums)
        for i in nums:
            if i==0:
                cmin=1
                cmax=1
            
            temp=cmax*i
            cmax=max(temp,cmin*i,i)
            cmin=min(temp,cmin*i,i)
            res=max(cmax,cmin,res)
        return res
            
        