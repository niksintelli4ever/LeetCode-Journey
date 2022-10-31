class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        dict1={}
        res=[]
        for i in nums1:
            dict1[i]=1+dict1.get(i,0)
        l=0
        for r in range(len(nums2)):
            if nums2[r] in dict1 and dict1[nums2[r]]>=1:
                res.append(nums2[r])
                dict1[nums2[r]]-=1
        
        return res
                
        
        