class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
            l=i+1
            r=len(nums)-1
            while l<r:
                t=nums[i]+nums[l]+nums[r]
                if abs(res-target)>abs(t-target):
                    res=t
                if t>target:
                    r-=1
                elif t<target:
                    l+=1
                else:
                    return t
        return res
        
        