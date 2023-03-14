class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            if nums[mid+1]>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        
        