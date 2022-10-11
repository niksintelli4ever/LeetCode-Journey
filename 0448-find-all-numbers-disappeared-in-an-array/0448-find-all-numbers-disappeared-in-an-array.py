class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            i= abs(nums[i])-1
            nums[i]=-1*abs(nums[i])
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        
        return res
            
        
        
        