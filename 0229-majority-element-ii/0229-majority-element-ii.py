class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict1={}
        n=len(nums)
        res=[]
        for i in nums:
            dict1[i]=1+dict1.get(i,0)
            if dict1[i] > n/3:
                if i not in res:
                    res.append(i)
            
        return res
        