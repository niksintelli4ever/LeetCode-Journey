class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        resmax=float("inf")
        res=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                sum1=nums[i]+nums[l]+nums[r]
                if sum1==target:
                    return sum1
                if abs(sum1-target) < abs(res-target):
                    res=sum1
                if sum1>target:
                    r-=1
                elif sum1<target:
                    l+=1
            
        return res
                
                    
                