class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp=abs(nums[i])-1
            nums[temp]=-1* abs(nums[temp])
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res