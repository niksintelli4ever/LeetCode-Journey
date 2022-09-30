class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmin=1
        cmax=1
        maxp=max(nums)
        for i in nums:
            if i==0:
                cmin=1
                cmax=1
            temp=cmax*i
            cmax=max(i,temp,cmin*i)
            cmin=min(i,temp,cmin*i)
            maxp=max(cmax,maxp)
        
        return maxp
                
        