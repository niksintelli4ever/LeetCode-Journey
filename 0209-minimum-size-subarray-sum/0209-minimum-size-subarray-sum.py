class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        sumtillnow=0
        minsize=float("inf")
        for r in range(len(nums)):
            sumtillnow+=nums[r]
            while sumtillnow>=target:
                sumtillnow-=nums[l]
                minsize=min(r-l+1,minsize)
                l+=1
            if sumtillnow<target:
                continue
        
        return 0 if minsize==float("inf") else minsize
                
        